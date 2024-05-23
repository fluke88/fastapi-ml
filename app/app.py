from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass

from ml.model import load_staff

model = None
app = FastAPI()


@dataclass
class CostPrediction:
    score: float


# create a route
@app.get("/")
def index():
    return {"params": "Cost"}


# Register the function to run during startup
@app.on_event("startup")
def startup_event():
    global model
    model = load_staff()


# Your FastAPI route handlers go here
@app.get("/predict")
def predict_cost(params: list):
    cost = model(params)
    print(cost)
    response = CostPrediction(
        score=cost.score,
    )

    return response
