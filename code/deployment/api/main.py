from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open('/app/models/titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

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