from pathlib import Path
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.predict import PROJECT_ROOT, predict_image

app = FastAPI(title="CIFAR-10 Image Classification API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Temporary uploads directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOAD_DIR = PROJECT_ROOT / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def home():
    return {"message": "CIFAR-10 Image Classification API is running..."}

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    # Save uploaded file temporary
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Predict 
    result = predict_image(file_path)

    # Delete temporary file 
    file_path.unlink(missing_ok=True)

    return result