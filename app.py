import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from src.prediction import predict
from PIL import Image

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.post("/score")
async def score(file: UploadFile = File(...)):
    """Scoring endpoint to run inference on a provided image file.

    Returns:
        dict: predicted data
    """
    try:
        image = Image.open(file.file)
    except Exception:
        return {"message": "There was an error uploading the file"}

    return predict(image)
