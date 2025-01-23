############## DIBUJO CONTORNOS #########################
import cv2

umbral = 200 #Determina el valor correcto del Umbral para la detección de colores a través de su histograma
color = (0,255,255) #Se determina el color para la linea de contorno 
grosor = 3 #
  
img = cv2.imread('C:/Users/gdavi/OneDrive/Documentos/Vision/Imagenes/figuras_geometricas3.jpg') #Se carga la imagen originalmente en color para después umbralizarla
#Sobre la imagen a color es donde se realizara el trazado del contorno 

img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convertimos la imagen en una imagen en escala de grises 
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV) #Aplicamos un filtro de Umbral 
cv2.imshow('Imagen binarizada', img_umbral) #Vemos la imagen binarizada

contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #Encontramos los contornos 

cv2.drawContours(img, contornos, -1, color, grosor) #Se dibujan los contornos 
cv2.imshow('Contorno', img) #Se muestra la imagen con sus contornos

cv2.waitKey(0)
cv2.destroyAllWindows()





