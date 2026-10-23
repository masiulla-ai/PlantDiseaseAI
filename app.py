
import json
from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "plant_disease_model.keras"
CLASSES_PATH = ROOT / "models" / "class_names.json"

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

@st.cache_data
def load_classes():
    with open(CLASSES_PATH, "r") as file:
        return json.load(file)


st.title("🌿 Plant Disease Detection System")

st.markdown(
    """
    ### Smart Tomato Leaf Analysis

    Upload an image of a tomato leaf to identify its likely
    disease using a Convolutional Neural Network (CNN).

    **Features**
    - Image-based disease prediction
    - Confidence score and class comparisons
    - Disease information and suggested care
    """
)

st.sidebar.title("About the Project")
st.sidebar.write(
    "A BCA final-year project using Deep Learning "
    "to classify tomato leaf images into 10 classes."
)

st.sidebar.markdown("---")
st.sidebar.write("**Model:** CNN")
st.sidebar.write("**Framework:** TensorFlow")
st.sidebar.write("**Interface:** Streamlit")
st.sidebar.write("**Validation accuracy:** 89%")


if not MODEL_PATH.exists() or not CLASSES_PATH.exists():
    st.error("Model files are missing. Please train the model first.")
    st.stop()

model = load_model()
class_names = load_classes()

uploaded_file = st.file_uploader(
    "Choose a tomato leaf image",
    type=["jpg", "jpeg", "png"]
)

DISEASE_INFO = {
    "Bacterial spot": {
        "cause": "Bacterial infection affecting leaves and fruit.",
        "care": "Avoid overhead watering, remove badly affected plant debris, "
                "and use locally recommended disease-management practices."
    },
    "Early blight": {
        "cause": "A fungal disease that often causes brown, ring-shaped leaf spots.",
        "care": "Remove affected leaves, water near the soil, and avoid wetting foliage."
    },
    "Late blight": {
        "cause": "A destructive disease that can spread rapidly in cool, humid conditions.",
        "care": "Isolate affected plants where practical, remove infected material safely, "
                "and seek local agricultural advice promptly."
    },
    "Leaf Mold": {
        "cause": "A fungal disease favoured by high humidity.",
        "care": "Improve airflow, reduce leaf wetness, and remove infected leaves."
    },
    "Septoria leaf spot": {
        "cause": "A fungal disease causing small spots, often with pale centres.",
        "care": "Remove infected lower leaves, avoid overhead watering, "
                "and clear infected plant debris."
    },
    "Spider mites Two-spotted spider mite": {
        "cause": "Tiny pests that feed on leaves and may cause stippling and webbing.",
        "care": "Inspect leaf undersides, reduce plant stress, and seek suitable pest-control advice."
    },
    "Target Spot": {
        "cause": "A disease that produces circular leaf lesions.",
        "care": "Remove affected foliage where practical, improve airflow, "
                "and avoid prolonged leaf wetness."
    },
    "Tomato Yellow Leaf Curl Virus": {
        "cause": "A viral disease often associated with whitefly transmission.",
        "care": "Manage whiteflies, remove severely infected plants where appropriate, "
                "and use resistant varieties when planting."
    },
    "Tomato mosaic virus": {
        "cause": "A viral disease that can cause mottled leaves and reduced growth.",
        "care": "Clean tools, wash hands after handling plants, and remove infected plants "
                "according to local guidance."
    },
    "healthy": {
        "cause": "The model classified this leaf as healthy.",
        "care": "Continue regular watering, balanced nutrition, and routine plant monitoring."
    }
}


if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded leaf image", width=350)

    if st.button("Detect Disease", type="primary"):
        with st.spinner("Analyzing leaf image..."):
            resized = image.resize((128, 128))
            image_array = np.array(resized, dtype=np.float32)
            image_array = np.expand_dims(image_array, axis=0)

            predictions = model.predict(image_array, verbose=0)[0]
            best_index = int(np.argmax(predictions))
            best_class = class_names[best_index]
            confidence = float(predictions[best_index]) * 100

        disease_name = best_class.replace("Tomato___", "").replace("_", " ")

        st.subheader("Prediction Result")
        st.success(f"Predicted class: {disease_name}")

        info = DISEASE_INFO.get(disease_name)
        if info:
            st.subheader("About this result")
            st.write("**Possible cause:**", info["cause"])
            st.subheader("Suggested care")
            st.write(info["care"])

        st.metric("Model confidence", f"{confidence:.2f}%")

        if confidence < 70:
            st.warning(
                "The prediction is uncertain. Try a clearer leaf image "
                "with good lighting, and verify the result independently."
            )
        else:
            st.info(
                "This is an AI prediction, not a confirmed diagnosis. "
                "Verify the result before taking plant-treatment decisions."
            )

        st.subheader("Class scores")
        for name, score in zip(class_names, predictions):
            clean_name = name.replace("Tomato___", "").replace("_", " ")
            st.write(f"{clean_name}: {score * 100:.2f}%")
            st.progress(float(score))

