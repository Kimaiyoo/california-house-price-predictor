from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Load the model
with open("carlifornia_knn_regressor.pkl", "rb") as f:
    model = pickle.load(f)

# Define the input schema
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Create the app
app = FastAPI(title="Carlifornia Housing Price Predictor")

@app.get("/")
def root():
    return {"message": "Welcome to the California Housing Price Prediction API!",
            "usage": "Visit /docs to try the /predict endpoint with sample JSON input using the interactive Swagger UI.",
            "docs_url": "/docs"
    }

@app.post("/predict")
def predict(data: HouseFeatures):
    try:
        features = pd.DataFrame([data.model_dump()])  
        prediction = model.predict(features)[0]

        return {
    
            "predicted_price": f"${prediction * 100000:.2f}"
        }
    except Exception as e:
        return {
            "error": "Prediction failed.",
            "details": str(e)
        }
