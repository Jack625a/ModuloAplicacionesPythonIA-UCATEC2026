from textblob import TextBlob

texto=TextBlob("La hamburguesa esta horrible y no me gusto para nada")
print(texto.sentiment)
#Rnangos de polaridad 
#-1 negativos
# 0 neutrales
# 1 positivos

#Rangos de subjetividad
#0 MUY OBJETIVO (BASADO EN HECHOS)
#1 MUY SUBJETIVO (EMOCIONES)