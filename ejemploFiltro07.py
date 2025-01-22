# Filtro morfológico
# 1. Erosión: Reduce el tamaño de los objetos en la imagen, eliminando pequeñas imperfecciones y ruidos.
# 2. Dilatación: Aumenta el tamaño de los objetos en la imagen, llenando pequeños agujeros o espacios.

import cv2  # Importa la biblioteca OpenCV para procesamiento de imágenes
import numpy as np  # Importa NumPy para operaciones numéricas

# Definir un kernel de 3x3 lleno de unos, que se usará para las operaciones morfológicas
kernel = np.ones((3,3), np.uint8)  # Corregido de np.unit8 a np.uint8

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/MorfologicoRuido.jpg', 0)

# Aplicar la operación de erosión a la imagen
erosion = cv2.erode(img, kernel)

# Aplicar la operación de dilatación a la imagen
dilatada = cv2.dilate(img, kernel)  

# Mostrar la imagen original en una ventana
cv2.imshow('imagen original', img)

# Mostrar la imagen erosionada en una ventana
cv2.imshow('img erosionada', erosion) 

# Mostrar la imagen dilatada en una ventana
cv2.imshow('imagen dilatada', dilatada)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
