# Plant Disease Detection System

## Project Overview
The Plant Disease Detection System is a deep learning application that classifies tomato leaf images into 10 disease and healthy-leaf categories using a Convolutional Neural Network (CNN).

The application provides a simple web interface built with Streamlit. Users can upload a tomato leaf image and view the predicted class, model confidence, class scores, and general plant-care suggestions.

## Objectives
- Develop a CNN model for tomato leaf classification.
- Create a user-friendly image-upload interface.
- Display predictions and confidence scores.
- Provide general information about detected disease categories.
- Evaluate the model using a separate validation dataset.

## Technologies Used
- Python
- TensorFlow and Keras
- Convolutional Neural Network (CNN)
- Streamlit
- NumPy
- Pillow
- Matplotlib
- Scikit-learn

## Dataset
The dataset is organized into training and validation folders and contains 10 tomato leaf classes.

## Model Evaluation
- Validation images: 1,000
- Validation accuracy: 89%
- Macro F1-score: 0.89

These results are based on the current validation dataset and do not guarantee the same performance on real-world images.

## How to Run
1. Install Python and the required project libraries.
2. Open the project directory in VS Code.
3. Activate the virtual environment.
4. Run `python -m streamlit run app.py`.
5. Open the local URL displayed in the terminal.
6. Upload a tomato leaf image and select Detect Disease.

## Limitations
- The current model is designed for tomato leaf images.
- Image quality, lighting, and background may affect predictions.
- A high confidence score does not guarantee a correct diagnosis.
- Plant-care suggestions are general guidance, not a substitute for expert diagnosis.

## Future Scope
- Improve accuracy using transfer learning.
- Support more plant species.
- Deploy the application online.
- Add more detailed disease-management information.
- Test the model on real-world images from different environments.
