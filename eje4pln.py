#dESCARGAR EL DATA DE NLTK
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

texto="El Presidente Paz propone bloque de seis naciones para potenciar el desarrollo sudamericano el 20 de abril "
#Tokenizacion por palabras
tokenizar=word_tokenize(texto)
#tokenizacion por oraciones
oraciones=sent_tokenize(texto)
#Eliminaion de palabras vacias
palabrasVacias=set(stopwords.words('spanish'))
restultadoPalabrasVacias=[palabra for palabra in tokenizar if palabra not in palabrasVacias]
print(tokenizar)
print(oraciones)
print(restultadoPalabrasVacias)


