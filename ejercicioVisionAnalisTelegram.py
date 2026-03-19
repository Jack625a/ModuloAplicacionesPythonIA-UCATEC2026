import cv2
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
from deepface import DeepFace

tokenTelegram=""

#Cargar el modelo
modelo=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

async def emocion(update:Update,context:ContextTypes.DEFAULT_TYPE):
    camara=cv2.VideoCapture(0)
    captura,imagen=camara.read()
    if not captura:
        update.message.reply_text("Error no se pudo obtener la foto")
        camara.release()
        return
    
    #Guardar la imagen de manera temporal
    cv2.imwrite("foto.jpg",imagen)
    try:
        resultado=DeepFace.analyze(img_path="foto.jpg",actions=["emotion"],enforce_detection=False)
        emocion=resultado[0] 
    except: 
        emocion="No se detecto correctamente"
    cv2.putText(imagen,emocion["dominant_emotion"],(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imwrite("foto.jpg",imagen)
    await update.message.reply_photo(photo=open("foto.jpg","rb"))
    camara.release()
    

app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(CommandHandler("foto",emocion))

print("Bot iniciado...")

app.run_polling()