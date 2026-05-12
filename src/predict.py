from pathlib import Path
from tabnanny import verbose
from PIL import Image
from keras.models import load_model
import numpy as np

# CIFAR-10 class names 
CLASS_NAMES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "froq",
    "horse",
    "ship",
    "truck"
]

# Resolve Porject Root 
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load saved model 
model = load_model(PROJECT_ROOT / "models/cifar10_cnn.keras")

def preprocess_image(image_path):
    """
    Load image, resize to 32x32, convert to RGB, 
    normalize to [0, 1], and add batch dimension.
    """
    img = Image.open(image_path).convert("RGB")
    img = img.resize((32, 32))

    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

def predict_image(image_path):
    """
    Predict class name and confidence for an image.
    """
    processed_image = preprocess_image(image_path)

    probabilities = model.predict(processed_image, verbose=0)
    predicted_index = np.argmax(probabilities, axis=1)[0]

    predicted_label = CLASS_NAMES[predicted_index]
    confidence = float(probabilities[0][predicted_index])

    return {
        "predicted_class": predicted_label,
        "confidence": confidence
    }

if __name__ == "__main__":
    import sys
    # if len(sys.argv) < 2:
    #     print(f"Usage: python src/predict.py <image_path>")
    # else:
    result = predict_image(PROJECT_ROOT / "src/test.jpeg")
    print(result)