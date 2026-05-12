# 🖼️ Basic Image Classification using CNN + FastAPI + React

An end-to-end Computer Vision project that classifies images into 10 categories using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset.

---

## 🚀 Project Overview

This project demonstrates a complete AI application pipeline:

1. Train a CNN using TensorFlow/Keras
2. Save the trained model
3. Build a reusable prediction module
4. Expose predictions via FastAPI
5. Create a React frontend for image upload and prediction

---

## 🎯 Supported Classes

The model predicts one of the following CIFAR-10 categories:

* ✈️ Airplane
* 🚗 Automobile
* 🐦 Bird
* 🐱 Cat
* 🦌 Deer
* 🐶 Dog
* 🐸 Frog
* 🐴 Horse
* 🚢 Ship
* 🚚 Truck

---

## 🏗️ Project Architecture

```text
Image Upload
     ↓
Resize to 32×32
     ↓
Convert to RGB
     ↓
Normalize Pixel Values (0–255 → 0–1)
     ↓
CNN Model
     ↓
Softmax Probabilities
     ↓
Predicted Class + Confidence
     ↓
FastAPI Backend
     ↓
React Frontend
```

---

## 📂 Project Structure

```text
basic-image-classification/
│── data/
│── notebooks/
│   └── basic_image_classification.ipynb
│
│── src/
│   ├── predict.py
│   ├── test.jpeg
│   └── testing_images/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── image3.jpg
│
│── models/
│   └── cifar10_cnn.keras
│
│── app/
│   └── api.py
│
│── uploads/
│
│── frontend/
│   ├── src/
│   └── package.json
│
│── requirements.txt
│── README.md
│── .gitignore
```

> Note: Replace `image1.jpg`, `image2.jpg`, and `image3.jpg` with your actual file names if desired.

---

## 🧠 Model Architecture

```text
Input (32×32×3)
      ↓
Conv2D(32, 3×3) + ReLU
      ↓
MaxPooling2D(2×2)
      ↓
Conv2D(64, 3×3) + ReLU
      ↓
MaxPooling2D(2×2)
      ↓
Flatten
      ↓
Dropout
      ↓
Dense(64) + ReLU
      ↓
Dense(10) + Softmax
```

---

## 📊 Dataset

This project uses the CIFAR-10 dataset:

* 60,000 color images
* Image size: 32×32×3
* 50,000 training images
* 10,000 testing images
* 10 classes

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib
* Pillow
* Scikit-learn

### Backend

* FastAPI
* Uvicorn

### Frontend

* React
* Vite
* Axios

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AjaySah61/basic-image-classification.git
cd basic-image-classification
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Open the Jupyter notebook and run all cells:

```bash
jupyter notebook
```

Notebook:

```text
notebooks/basic_image_classification.ipynb
```

The trained model will be saved to:

```text
models/cifar10_cnn.keras
```

---

## 🧪 Test Prediction Script

### Single Test Image

```bash
python src/predict.py src/test.jpeg
```

### Additional Test Images

```bash
python src/predict.py src/testing_images/image1.jpg
python src/predict.py src/testing_images/image2.jpg
python src/predict.py src/testing_images/image3.jpg
```

### Example Output

```python
{
    'predicted_class': 'cat',
    'confidence': 0.873421
}
```

---

## 🚀 Run FastAPI Backend

```bash
uvicorn app.api:app --reload
```

API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### GET /

Returns API health status.

#### Response

```json
{
  "message": "CIFAR-10 Image Classification API is running."
}
```

---

### POST /predict

Upload an image and receive the predicted class and confidence.

#### Response

```json
{
  "predicted_class": "dog",
  "confidence": 0.912345
}
```

---

## ⚛️ Run React Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## 🖥️ Frontend Features

* Upload image
* Preview selected image
* Predict class
* Display confidence score
* Loading state

---

## 📈 Model Performance

Typical performance for this CNN:

|            Metric | Expected Value |
| ----------------: | :------------- |
| Training Accuracy | 70%–80%        |
|     Test Accuracy | 68%–75%        |

> Actual performance may vary depending on training settings and hardware.

---

## 📸 Screenshots

Add screenshots here after pushing the project to GitHub.

### FastAPI Swagger Docs

```text
screenshots/swagger_docs.png
```

### React Frontend

```text
screenshots/frontend.png
```

### Prediction Result

```text
screenshots/prediction_result.png
```

---

## 🧠 Key Learning Outcomes

* Image preprocessing and normalization
* Convolutional Neural Networks (CNNs)
* Softmax-based multi-class classification
* Model serialization with `.keras`
* Reusable prediction modules
* FastAPI backend development
* React frontend integration
* Full-stack AI deployment

---

## 🚀 Future Improvements

* Transfer Learning with MobileNetV2
* Data Augmentation
* Top-3 predictions
* Drag-and-drop image upload
* Docker deployment
* Cloud deployment (Render, Railway, AWS)

---

## 💼 Portfolio Relevance

This project demonstrates skills relevant to:

* Machine Learning Engineer
* AI Engineer
* Computer Vision Engineer
* Data Scientist
* Full-Stack AI Developer

---

## 👨‍💻 Author

**Ajay Sah**

* GitHub: [https://github.com/your-username](https://github.com/your-username)
* LinkedIn: [https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/your-profile)

---

## ⭐ If You Found This Project Useful

Please consider starring the repository.

```text
⭐ Star this repository to support the project.
```
