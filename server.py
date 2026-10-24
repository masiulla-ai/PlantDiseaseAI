import os
import io
import json
import base64
from pathlib import Path
from typing import Optional

import numpy as np
from PIL import Image
import tensorflow as tf
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel

from disease_info import DISEASE_DATA

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "plant_disease_model.keras"
CLASSES_PATH = BASE_DIR / "class_names.json"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Plant Disease Detection AI",
    description="Deep Learning API for Tomato Foliar Disease Diagnosis",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load classes
if not CLASSES_PATH.exists():
    raise RuntimeError(f"Class names file not found at {CLASSES_PATH}")

with open(CLASSES_PATH, "r") as f:
    CLASS_NAMES = json.load(f)

# Global model holder
model = None

def get_model():
    global model
    if model is None:
        if not MODEL_PATH.exists():
            raise RuntimeError(f"Model file not found at {MODEL_PATH}")
        print("Loading TensorFlow model...")
        model = tf.keras.models.load_model(MODEL_PATH)
        # Warmup prediction
        dummy = np.zeros((1, 128, 128, 3), dtype=np.float32)
        model.predict(dummy, verbose=0)
        print("Model loaded and warmed up successfully.")
    return model

@app.on_event("startup")
async def startup_event():
    get_model()

class Base64PredictRequest(BaseModel):
    image: str

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((128, 128))
        img_array = np.array(img, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image format: {str(e)}")

def run_prediction(img_array: np.ndarray):
    mdl = get_model()
    raw_predictions = mdl.predict(img_array, verbose=0)[0]
    
    best_index = int(np.argmax(raw_predictions))
    predicted_class = CLASS_NAMES[best_index]
    confidence = float(raw_predictions[best_index]) * 100.0

    # Build distribution list
    all_scores = []
    for idx, (cls, score) in enumerate(zip(CLASS_NAMES, raw_predictions)):
        score_pct = round(float(score) * 100.0, 2)
        info = DISEASE_DATA.get(cls, {})
        all_scores.append({
            "class_id": cls,
            "name": info.get("name", cls.replace("Tomato___", "").replace("_", " ")),
            "score": score_pct,
            "is_best": (idx == best_index)
        })
    all_scores.sort(key=lambda x: x["score"], reverse=True)

    disease_info = DISEASE_DATA.get(predicted_class, {
        "id": predicted_class,
        "name": predicted_class.replace("Tomato___", "").replace("_", " "),
        "crop": "Tomato",
        "pathogen_type": "Unknown",
        "pathogen": "N/A",
        "severity": "Moderate",
        "severity_color": "amber",
        "summary": "Detected tomato leaf condition.",
        "symptoms": ["Visible foliage alterations."],
        "organic_treatment": ["Isolate plant and inspect symptoms."],
        "chemical_treatment": ["Consult local agricultural extension."],
        "prevention": ["Practice routine crop sanitation."]
    })

    status_tag = "Healthy" if "healthy" in predicted_class.lower() else "Diseased"

    return {
        "status": "success",
        "prediction": {
            "class_id": predicted_class,
            "name": disease_info["name"],
            "confidence": round(confidence, 2),
            "status_tag": status_tag,
            "is_confident": confidence >= 65.0,
            "details": disease_info,
            "all_scores": all_scores
        }
    }

@app.post("/api/predict")
async def predict_file(file: UploadFile = File(...)):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")
    img_array = preprocess_image(content)
    return run_prediction(img_array)

@app.post("/api/predict-base64")
async def predict_base64(req: Base64PredictRequest):
    data = req.image
    if "," in data:
        data = data.split(",", 1)[1]
    try:
        image_bytes = base64.b64decode(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid base64 payload")
    img_array = preprocess_image(image_bytes)
    return run_prediction(img_array)

@app.get("/api/diseases")
async def get_diseases():
    return {
        "status": "success",
        "count": len(DISEASE_DATA),
        "diseases": list(DISEASE_DATA.values())
    }

@app.get("/api/samples")
async def get_samples():
    samples_dir = STATIC_DIR / "samples"
    samples_list = []
    if samples_dir.exists():
        for cls in CLASS_NAMES:
            img_file = samples_dir / f"{cls}.jpg"
            if img_file.exists():
                info = DISEASE_DATA.get(cls, {})
                samples_list.append({
                    "class_id": cls,
                    "name": info.get("name", cls.replace("Tomato___", "").replace("_", " ")),
                    "pathogen_type": info.get("pathogen_type", "Disease"),
                    "severity": info.get("severity", "Moderate"),
                    "severity_color": info.get("severity_color", "amber"),
                    "image_url": f"/static/samples/{cls}.jpg"
                })
    return {
        "status": "success",
        "samples": samples_list
    }

@app.get("/api/model-info")
async def get_model_info():
    return {
        "status": "success",
        "model_architecture": "Convolutional Neural Network (CNN)",
        "framework": "TensorFlow 2.21 / Keras 3",
        "input_resolution": "128 x 128 x 3 (RGB)",
        "classes_supported": len(CLASS_NAMES),
        "classes": CLASS_NAMES,
        "metrics": {
            "validation_images": 1000,
            "accuracy": 89.10,
            "macro_f1": 0.89,
            "weighted_f1": 0.89
        },
        "confusion_matrix_url": "/static/confusion_matrix.png"
    }

# Mount static directory
if not STATIC_DIR.exists():
    STATIC_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
async def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return JSONResponse({
        "message": "Plant Disease AI Server is running.",
        "api_docs": "/docs",
        "status": "online"
    })

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)
