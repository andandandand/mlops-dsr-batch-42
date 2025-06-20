import torch
import io 
from pydantic import BaseModel 
from fastapi import FastAPI, File, UploadFile, Depends
from torchvision.models import ResNet

# This is a  'data model' for the output of the fruit classifier  
class Result(BaseModel):
    category: str # predicted label for the image
    confidence: float # confidence score for the prediction


app = FastAPI()


@app.get("/")
def read_root():
    return {'message': 
            'Welcome to the Fruit Classifier API, call the endpoint through /predict to classify images'}

@app.post("/predict", response_model=Result)
async def predict(
    input_image: UploadFile = File(...),
    model: ResNet = Depends(load_model),
    ... 