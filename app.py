from fastapi import FastAPI
import numpy as np
from src.prediction import predict

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.post("/score")
async def score() -> dict:
    """Scoring endpoint

    Returns:
        dict: predicted data
    """
    return predict()
