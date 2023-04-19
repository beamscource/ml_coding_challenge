from PIL import Image
from torchvision import transforms
from typing import Optional
import torch
import torch.nn as nn
import torch.nn.functional as F


def set_up_model():
    """A function to define the model and to load trained weights.

    Returns:
        dict: a PyTorch model
    """

    class SimpleNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(12288, 84)
            self.fc2 = nn.Linear(84, 50)
            self.fc3 = nn.Linear(50,3)
        
        def forward(self, x):
            x = x.view(-1, 12288)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # initialize the model and load weights
    model = SimpleNet()
    state_dict = torch.load("src/shoe_model.tar")
    model.load_state_dict(state_dict)
    model.to(device)

    return model

def predict(data: Optional[list] = None) -> dict:
    """A function that takes an image and runs a classification on it.

    Args:
        data (list): prediction data

    Returns:
        dict: predicted probabilities for the categories Boot, Sandal, Shoe
    """
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # transform input image
    transform_function = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225] )
        ])

    image = Image.open("data/test/sandal/Sandal (948).jpg")
    image = transform_function(image).to(device)
    image = torch.unsqueeze(image, 0)

    model = set_up_model()
    model.eval()
    probabilities = F.softmax(model(image), dim=1).cpu().detach().numpy()[0]
    test = {
        "Boot": f'{probabilities[0]:.2f}',
        "Sandal": f'{probabilities[1]:.2f}',
        "Shoe": f'{probabilities[2]:.2f}',
    }
    breakpoint()
    return {
        "Boot": f'{probabilities[0]:.2f}',
        "Sandal": f'{probabilities[1]:.2f}',
        "Shoe": f'{probabilities[2]:.2f}',
    }

data = []
predict(data)