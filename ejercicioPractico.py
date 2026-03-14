import spacy
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,filters, MessageHandler

procesamieto=spacy.load("es_core_news_sm")
tokenTelegram=""

async def responder(update:Update,context:ContextTypes.DEFAULT_TYPE):
    mensaje=update.message.text.lower()
    documento=procesamieto(mensaje)
    palabras=[token.text for token in documento]
    if "hola" in palabras:
        respuesta="Hola bievenido a UCATEC. En que puedo ayudarte?"
    elif "diplomado" in palabras:
        respuesta="Tenemos 5 diplomados en Inteligencia Artifial"
    elif "precio" in palabras:
        respuesta="El diplomado cuesta 100bs"
    else:
        respuesta="No entendi la pregunta"
    
    await update.message.reply_text(respuesta)

app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.TEXT,responder))

print("Bot esta funcionando")
app.run_polling()