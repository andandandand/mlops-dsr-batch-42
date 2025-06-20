import wandb
import torch
import os
from torchvision.models import ResNet, resnet18
from loadotenv import load_env

load_env() # Load environment variables from .env file
# comment load_env() when doing the GCP deployment      
wandb_api_key = os.environ.get('WANDB_API_KEY')
model_path = os.environ.get('MODEL_PATH')

if wandb_api_key:
    wandb.login(key=wandb_api_key)
    #print("Logged in to Weights & Biases")

print(model_path)
