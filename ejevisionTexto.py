import cv2
from paddleocr import PaddleOCR
from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler,filters,ContextTypes

tokenTelegram=""

analisis=PaddleOCR(use_angle_cls=True, lang='es', enable_mkldnn=False)

async def leer(update:Update,context:ContextTypes.DEFAULT_TYPE):
    imagenDescargar=await update.message.photo[-1].get_file()
    await imagenDescargar.download_to_drive("imagenTelegram.jpg")
    leerImagen=cv2.imread("imagenTelegram.jpg")
    resultado=analisis.ocr(leerImagen)
    print(resultado)
    textoDetectado=""
    if resultado is not None:
        for res in resultado:
            if res is not None:
                for line in res:
              
                    textoDetectado += line[1][0]
    if textoDetectado.strip()=="":
        textoDetectado="NO SE ENCONTRO NINGUN TEXTO EN LA IMAGEN"
    await update.message.reply_text("Texto detectado:\n"+ textoDetectado)
    print(textoDetectado)


app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.PHOTO,leer))

print("BOT FUNCIONANDO...")

app.run_polling()