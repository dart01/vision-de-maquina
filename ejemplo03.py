############ LINEAS ###############

import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',1)

# Creación de metadato - Línea
cv2.arrowedLine(img,(200,100), (300,150),(0,0,255),2)

cv2.imshow('Ejemplo03', img)

cv2.waitKey(0)
cv2.destroyAllWindows()