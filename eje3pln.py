import spacy

#cargar modelo en español
pln=spacy.load("es_core_news_sm")

#SEPARACION DE PALABRAS

texto="El Presidente Paz propone bloque de seis naciones para potenciar el desarrollo sudamericano el 20 de abril "
documento=pln(texto)

for separacion in documento:
    print(separacion.text,separacion.pos_)