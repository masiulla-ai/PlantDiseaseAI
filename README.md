# Plant Disease Detection System

## Project Overview
The Plant Disease Detection System is a deep learning web application that classifies tomato leaf images into 10 disease and healthy-leaf categories using a Convolutional Neural Network (CNN).

The project includes:
- **Interactive Full-Stack Web Application**: Powered by FastAPI and a modern, responsive Tailwind CSS frontend with drag-and-drop, real-time camera capture, sample testing, confidence visualizer, and detailed disease diagnosis/treatment guides.
- **Streamlit Interface**: Lightweight dashboard for quick testing and model evaluation.

## Objectives
- Develop a CNN model for tomato leaf classification.
- Create user-friendly image-upload and camera diagnostic interfaces.
- Display predictions with confidence scores and class probability distributions.
- Provide comprehensive disease information, organic/chemical treatment, and preventive advice.
- Evaluate the model using a separate validation dataset.

## Technologies Used
- **Backend / Deep Learning**: Python, TensorFlow 2.21, Keras, NumPy, Pillow
- **Web Server & API**: FastAPI, Uvicorn, Python-Multipart
- **Frontend**: HTML5, Tailwind CSS, Chart.js, Lucide Icons
- **Streamlit Application**: Streamlit
- **Model Evaluation**: Scikit-learn, Matplotlib

## Dataset & Classes
The dataset is organized into training and validation folders covering 10 tomato leaf categories:
1. Bacterial Spot (`Tomato___Bacterial_spot`)
2. Early Blight (`Tomato___Early_blight`)
3. Late Blight (`Tomato___Late_blight`)
4. Leaf Mold (`Tomato___Leaf_Mold`)
5. Septoria Leaf Spot (`Tomato___Septoria_leaf_spot`)
6. Spider Mites / Two-spotted Spider Mite (`Tomato___Spider_mites Two-spotted_spider_mite`)
7. Target Spot (`Tomato___Target_Spot`)
8. Tomato Yellow Leaf Curl Virus (`Tomato___Tomato_Yellow_Leaf_Curl_Virus`)
9. Tomato Mosaic Virus (`Tomato___Tomato_mosaic_virus`)
10. Healthy Leaf (`Tomato___healthy`)

## Model Evaluation
- Validation images: 1,000
- Validation accuracy: 89.10%
- Macro F1-score: 0.89

## How to Run

### 1. Modern Web Application (FastAPI + Tailwind CSS)
```bash
# Run the web server
python server.py
# Or with uvicorn directly:
python -m uvicorn server:app --reload --host 0.0.0.0 --port 8000
```
Open your browser and navigate to: `http://localhost:8000`

### 2. Streamlit Dashboard
```bash
python -m streamlit run app.py
```
Open the local URL displayed in the terminal (usually `http://localhost:8501`).

## Limitations
- The model is trained specifically on tomato leaf images.
- Image quality, lighting, and background may affect predictions.
- AI predictions are meant for decision support and not a substitute for certified agronomic lab tests.

## Future Scope
- Support multi-crop classification (potato, pepper, apple, corn).
- Mobile native application using TensorFlow Lite.
- Cloud deployment (Docker / Render / Hugging Face Spaces).
- Weather and humidity integration for localized disease risk prediction.
