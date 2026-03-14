import nltk
from nltk.tokenize import word_tokenize
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler,filters, ContextTypes

tokenTelegram=""

#Base del Conocimiento
baseConocimiento = {
    # --- Saludos y Generalidades ---
    "hola": "¡Hola! Bienvenido al centro de atención de la Universidad UCATEC. ¿En qué puedo ayudarte hoy?",
    "mision": "Nuestra misión es formar emprendedores éticos, innovadores y socialmente responsables.",
    "ubicación": "Nos encontramos en la Calle Iturricha N° 847, zona de Sarco, Cochabamba, Bolivia.",
    "contacto": "Puedes comunicarte con nosotros al teléfono (4) 4420010 o vía WhatsApp al 72200222.",

    # --- Oferta de Postgrado (Diplomados) ---
    "diplomados": "UCATEC ofrece diplomados especializados como: Inteligencia Artificial, Marketing Digital, Educación Superior y Gestión del Talento Humano.",
    "diplomado inteligencia artificial": "El Diplomado en IA se enfoca en Machine Learning, redes neuronales y automatización de procesos para empresas.",
    "diplomado marketing digital": "Enfocado en Growth Hacking, gestión de RRSS, SEO/SEM y estrategias de venta online.",
    "diplomado educacion superior": "Dirigido a profesionales que desean ejercer la docencia universitaria con enfoque en el modelo por competencias.",
    "diplomado gestion talento": "Especialización en liderazgo, cultura organizacional y nuevas tendencias en reclutamiento 4.0.",

    # --- Carreras de Pregrado (Facultades) ---
    "carreras": "Contamos con carreras en áreas de Ingeniería, Ciencias Empresariales, Sociales y Salud. ¿Alguna área te interesa en particular?",
    "ingenieria": "Ofrecemos Ingeniería de Sistemas, Ingeniería Comercial e Ingeniería Industrial.",
    "ciencias empresariales": "Contamos con Administración de Empresas, Contaduría Pública y Comercio Internacional.",
    "comunicacion": "La carrera de Comunicación Social de UCATEC destaca por su enfoque en producción multimedia y periodismo digital.",

    # --- Beneficios y Modalidad ---
    "modalidad": "Contamos con modalidades presenciales, semipresenciales y virtuales, adaptadas a tu ritmo de trabajo.",
    "emprendimiento": "Somos la primera universidad emprendedora; contamos con un Centro de Emprendimiento (C-EMPRENDE) para apoyar tus proyectos.",
    "requisitos inscripcion": "Necesitas tu Título de Bachiller (original), certificado de nacimiento, fotocopia de C.I. y 4 fotos 3x3 fondo azul.",

    # --- Cierre ---
    "gracias": "Fue un placer ayudarte. ¡Esperamos verte pronto en el campus de UCATEC!",
    "adios": "¡Hasta luego! Recuerda que el éxito depende de tu espíritu emprendedor."
}

def similitudes(texto1,texto2):
    palabras1=set(word_tokenize(texto1.lower()))
    palabras2=set(word_tokenize(texto2.lower()))

    interseccion=palabras1.intersection(palabras2)
    return len(interseccion)

async def responder(update:Update,context:ContextTypes.DEFAULT_TYPE):
    mensaje=update.message.text.lower()
    mejor_respuesta="No entendi la pregunta"
    puntaje=0
    for pregunta in baseConocimiento:
        puntajePregunta=similitudes(mensaje,pregunta)
        if puntajePregunta>puntaje:
            puntaje=puntajePregunta
            mejor_respuesta=baseConocimiento[pregunta]
    await update.message.reply_text(mejor_respuesta)

#Creacion del bot
app=ApplicationBuilder().token(tokenTelegram).build()
app.add_handler(MessageHandler(filters.TEXT,responder))

print("Bot inicializado...")
app.run_polling()