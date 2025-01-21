#filtro adptativo 
import cv2

bloque = 3
constante = 0

def actualizarBloque (blq):
    global bloque
    bloque = blq 
    if bloque < 3: bloque = 3
    elif bloque % 2 == 0: bloque += 1
    imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
    cv2.imshow('imagen filtrada', imgUmbralizada)


def actualizarConstante (cte):
    global constante
    constante = cte
    imgUmbralizada= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
    cv2.imshow('imagen filtrada', imgUmbralizada)

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/tabla_numeros.jpg',0)
imgUmbralizada= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)


cv2.imshow('imagen original', img)
cv2.imshow('imagen original', imgUmbralizada)
cv2.createTrackbar('Bloque', 'imagen original', 0, 100, actualizarBloque)
cv2.createTrackbar('constante', 'imagen original', 0, 255, actualizarConstante)

cv2.waitKey(0)
cv2.destroyAllWindows()