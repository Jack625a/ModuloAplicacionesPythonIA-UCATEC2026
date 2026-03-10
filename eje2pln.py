import spacy

#cargado del modelo en Español
modelo=spacy.load('es_core_news_sm')

texto="El modulo aplicacion python en Inteligencia artificial esta cambiando Bolivia"

analisis=modelo(texto)

for palabra in analisis.ents:
    print(palabra.text,palabra.label_)