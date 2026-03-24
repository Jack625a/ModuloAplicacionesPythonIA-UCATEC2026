from torchvision import models

modelo=models.ResNet50_Weights.DEFAULT
clases=modelo.meta["categories"]
print(clases)