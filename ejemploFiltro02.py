import cv2
from matplotlib import pyplot as plt

#treshold
    # 1. binario
    # 2. binario invertido
    # 3. truncado
    # 4. truncado
    # 5. to_zero
    # 6. to_zero_inv
    
def actualizarImagen(umbral):
    _, umbralizado = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY)
    cv2.imshow('imagen filtrada', umbralizado) 

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',0)
cv2.imshow('imagen original', img) 

# Obtener el tamaño de la imagen
altura, ancho = img.shape

# Mostrar el tamaño
print(f"Altura: {altura}, Ancho: {ancho}")


cv2.createTrackbar('umbral', 'imagen original', 0 , 255, actualizarImagen)
actualizarImagen(0)
cv2.waitKey(0)
cv2.destroyAllWindows()