#Paso 1. Importar la libreria
import cv2

#Paso 2. Cargar el modelo (Clasificador de rostros)
modelo=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

#Paso 3. Cargar una imagen
imagen=cv2.imread("personas4.jpeg")

#Paso 4. Convertir a escalas de grises (256)
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#Paso 5. Deteccion de rostros
rostros=modelo.detectMultiScale(grises,1.05,7)

#Escalas de tamaños
#1.05 mas preciso pero muy lento
#1.1 buena precision
#1.3 mas rapido
#1.5 puede perder rostros 

#Valor para cantidad de detecciones repetitivas
#3 detecta mas rostros pero mas errores
#5 es el mas equilibrado
#7 es mas estricto
#10 puede perder rostros

#Paso 6. Dibujar los rectangulos a las detecciones
for (x,y,w,h) in rostros:
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),2)

#Paso 7. Mostrar el resultado de la deteccion
cv2.imshow("DETECCION DE ROSTROS",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
