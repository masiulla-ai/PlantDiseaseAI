
from pathlib import Path
import json
import tensorflow as tf
import keras

layers = keras.layers

# Project paths
ROOT = Path(__file__).resolve().parent.parent
TRAIN_DIR = ROOT / "data" / "tomato" / "train"
VAL_DIR = ROOT / "data" / "tomato" / "val"
MODEL_DIR = ROOT / "models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32
SEED = 42

# Load training and validation images
train_ds = keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    seed=SEED
)

val_ds = keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    shuffle=False
)

class_names = train_ds.class_names

# Save the class names for the website
with open(MODEL_DIR / "class_names.json", "w") as f:
    json.dump(class_names, f, indent=4)

# Improve data loading performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# Build a CNN model
model = keras.Sequential([
    layers.Input(shape=(128, 128, 3)),
    layers.Rescaling(1.0 / 255),
    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.4),
    layers.Dense(len(class_names), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Train the model
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)

# Save the trained model
model.save(MODEL_DIR / "plant_disease_model.keras")

print("\nTraining completed!")
print("Model saved to:", MODEL_DIR / "plant_disease_model.keras")
print("Classes:", class_names)
