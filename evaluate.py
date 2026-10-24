
from pathlib import Path
import json

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score
)

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "plant_disease_model.keras"
VAL_DIR = ROOT / "data" / "tomato" / "val"
MODEL_DIR = ROOT / "models"

IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32

print("Loading trained model...")
model = tf.keras.models.load_model(MODEL_PATH)

with open(MODEL_DIR / "class_names.json", "r") as f:
    class_names = json.load(f)

print("Loading validation images...")
val_ds = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

y_true = np.concatenate([
    labels.numpy() for _, labels in val_ds
])

print("Predicting validation images...")
predictions = model.predict(val_ds, verbose=1)
y_pred = np.argmax(predictions, axis=1)

accuracy = accuracy_score(y_true, y_pred)

report = classification_report(
    y_true,
    y_pred,
    labels=list(range(len(class_names))),
    target_names=class_names,
    zero_division=0
)

print(f"\nValidation accuracy: {accuracy * 100:.2f}%")
print("\nClassification report:\n")
print(report)

# Save the evaluation results
report_path = MODEL_DIR / "evaluation_report.txt"

with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"Validation accuracy: {accuracy * 100:.2f}%\n\n")
    f.write(report)

# Generate a confusion matrix
cm = confusion_matrix(
    y_true,
    y_pred,
    labels=list(range(len(class_names)))
)

fig, ax = plt.subplots(figsize=(12, 10))

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        name.replace("Tomato___", "").replace("_", " ")
        for name in class_names
    ]
)

display.plot(
    ax=ax,
    xticks_rotation=90,
    colorbar=False
)

plt.title("Tomato Disease Detection - Confusion Matrix")
plt.tight_layout()

plt.savefig(
    MODEL_DIR / "confusion_matrix.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close(fig)

print("\nEvaluation completed!")
print("Report saved:", report_path)
print("Confusion matrix saved:", MODEL_DIR / "confusion_matrix.png")
