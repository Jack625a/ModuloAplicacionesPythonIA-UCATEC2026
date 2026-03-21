import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder,MessageHandler,filters,ContextTypes
from PIL import Image

tokenTelegram=""
apiGoogle=""
genai.configure(api_key=apiGoogle)
modelo=genai.GenerativeModel("gemini-3.1-flash-lite-preview")

async def leer(update:Update, context:ContextTypes.DEFAULT_TYPE):
    imagenDescargar=await update.message.photo[-1].get_file()
    await imagenDescargar.download_to_drive("imagenTelegram.jpg")

    image=Image.open("imagenTelegram.jpg")
    prompt="Extrae todo el texto de esta imagen"

    respuesta=modelo.generate_content([prompt,image])
    texto=respuesta.text
    await update.message.reply_text(texto)

app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.PHOTO,leer))

print("BOT FUNCIONANDO...")

app.run_polling()