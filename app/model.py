import wandb
import torch
import os
from torchvision.models import ResNet, resnet18
from loadotenv import load_env

wandb_api_key = os.environ.get('WANDB_API_KEY')

if wandb_api_key:
    wandb.login(key=wandb_api_key)
    print("Logged in to Weights & Biases")
