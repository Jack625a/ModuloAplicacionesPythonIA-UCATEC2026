import cv2
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes

tokenTelegram=""

#Cargar el modelo
modelo=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

async def foto(update:Update,context:ContextTypes.DEFAULT_TYPE):
    camara=cv2.VideoCapture(0)
    captura,imagen=camara.read()
    if not captura:
        update.message.reply_text("Error no se pudo obtener la foto")
        camara.release()
        return
    #Conversion a escalas de gris
    grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    #Detectar rostros
    rostros=modelo.detectMultiScale(grises,1.05,7)

    for (x,y,w,h) in rostros:
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),2)
    #Guardar imagen
    cv2.imwrite("fotoDeteccion.jpg",imagen)

    await update.message.reply_photo(photo=open("fotoDeteccion.jpg","rb"))
    camara.release()

    #if captura:
     #   cv2.imwrite("foto.jpg",imagen)
      #  await update.message.reply_photo(photo=open("foto.jpg","rb"))
    #else:
     #   await update.message.reply_text("Error no se pudo obtener la foto")
    
    #camara.release()

app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(CommandHandler("foto",foto))

print("Bot iniciado...")

app.run_polling()