import torch
from torchvision import models,transforms
from PIL import Image
from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler,filters,ContextTypes

tokenTelegram=""

#CARGAR EL MODELO DE RED NEURONAL PREENTRENADO
modelo=models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
modelo.eval()

#Transformadores ()
transformadores=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

#with open("imagenet_classes.txt") as f:
    #clases=[line.strip() for line in f.readlines()]

obtencion=models.ResNet50_Weights.DEFAULT
clases=obtencion.meta["categories"]

async def clasificar(update:Update, context:ContextTypes.DEFAULT_TYPE):
    foto=await update.message.photo[-1].get_file()
    await foto.download_to_drive("imagen.jpg")
    imagen=Image.open("imagen.jpg")
    imagenTransformada=transformadores(imagen)
    perdida=imagenTransformada.unsqueeze(0)

    with torch.no_grad():
        salida=modelo(perdida)
    valores,indices=torch.max(salida,1)

    resultado=clases[indices.item()]
    print(resultado)

    await update.message.reply_text(f"Se detecto objeto {resultado}")


app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.PHOTO,clasificar))
print("El bot co Resnet esta activo")

app.run_polling()