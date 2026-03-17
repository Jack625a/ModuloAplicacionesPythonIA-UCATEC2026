import cv2

print("Verificacion de camaras")

#for i in range(10):
 #   camara=cv2.VideoCapture(i)
  #  if camara.isOpened():
   #     print("Camara encontrada con id: ",i)
    #    camara.release()

camara=cv2.VideoCapture(0)
while True:
    captura,image=camara.read()
    if not captura:
        print("No se activo niguna camara")
        break
    cv2.imshow("Camara 1",image)
    if cv2.waitKey(1)&0xFF==ord("q"):
        break
camara.release()
cv2.destroyAllWindows()

  