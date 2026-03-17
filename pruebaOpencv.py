import cv2
modelo=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
if modelo.empty():
    print("Error al cargar el modelo")
else:
    print("Modelo cargado correctamente")
