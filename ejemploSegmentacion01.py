#contornos
import cv2

#modos---> prioridad de orden deteccion bordes 
# 1. external : externos 
# 2. list  :todos pero no se sabe el orden
# 3. cromp : primero externos luego internos

#metodo 
# approx_none: toma todos los puntos posibles
# approx_simple: puntos concavos "aproxima"

color = (0, 255, 255)
grosor = 3

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/ejemplo01.jpg', 1)
imgOriginal= img.copy()
imgByn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def mostrarImagenBinarizada(umbral):
    global imgUmbral
    _, imgUmbral = cv2.threshold(imgByn, umbral, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('imagen binarizada', imgUmbral)

def mostrarContornos():
    contornos, _= cv2.findContours(imgUmbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    img = imgOriginal.copy()
    cv2.drawContours(img, contornos, -1, color, grosor)
    cv2.imshow('imagen contorno', img)

def actualizarImagen(umbral):
    mostrarImagenBinarizada(umbral)
    mostrarContornos()

actualizarImagen(0)

cv2.createTrackbar('umbral', 'imagen contorno', 0, 254, actualizarImagen)

cv2.waitKey(0)
cv2.destroyAllWindows()