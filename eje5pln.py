#HABLAR - HABLANDO - HABLE - HABLAMOS 
#RAMIFICACION DE PALABRAS
from nltk.stem import PorterStemmer

ramificaciones=PorterStemmer()
palabras=["hablar","hablando","hable","hablamos"]
for palabra in palabras:
    print(ramificaciones.stem(palabra))