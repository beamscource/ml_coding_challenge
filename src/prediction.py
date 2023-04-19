from torchvision import transforms
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor


def set_up_model() -> nn.Module:
    """A function to initialize the model and to load trained weights.

    Returns:
        list: a PyTorch model
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

    # initialize the model and load weights
    model = SimpleNet()
    state_dict = torch.load("src/shoe_model.tar")
    model.load_state_dict(state_dict)

    return model

def predict(image: Tensor) -> dict:
    """A function that takes a tensor object of an image and runs a classification
    on it.

    Args:
        image: input image converted to a tensor

    Returns:
        dict: predicted probabilities for the categories boot, sandal, shoe
    """

    # transform the input image
    transform_function = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225] )
        ])
    image = transform_function(image)
    image = torch.unsqueeze(image, 0)

    # get prediction scores
    model = set_up_model()
    model.eval()
    probabilities = F.softmax(model(image), dim=1).detach().numpy()[0]

    return {
        "Boot": f'{probabilities[0]:.2f}',
        "Sandal": f'{probabilities[1]:.2f}',
        "Shoe": f'{probabilities[2]:.2f}',
    }