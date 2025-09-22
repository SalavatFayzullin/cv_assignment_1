from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI()

# Global variable for model
model = None

def load_model():
    global model
    if model is None:
        model_path = '/app/models/titanic_model.pkl'
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")
    return model

class PassengerData(BaseModel):
    pclass: int
    sex: int  # 0 for female, 1 for male
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: int  # 0=S, 1=C, 2=Q

@app.post("/predict")
def predict(data: PassengerData):
    model = load_model()  # Load model lazily
    
    # Map to correct column names
    input_data = pd.DataFrame([{
        'PassengerId': 0,  # Dummy value
        'Pclass': data.pclass,
        'Sex': data.sex,
        'Age': data.age,
        'SibSp': data.sibsp,
        'Parch': data.parch,
        'Fare': data.fare,
        'Embarked': data.embarked
    }])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0].max()
    
    return {
        "prediction": int(prediction),
        "probability": float(probability),
        "survived": bool(prediction)
    }

@app.get("/health")
def health():
    return {"status": "healthy"}