# filtro de canny
import cv2  

# Leer la imagen en escala de grises desde la ruta especificada
# La imagen se carga en escala de grises, lo cual es necesario para la detección de bordes.
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)

# threshold = umbrales

# Aplicar el filtro de Canny a la imagen
# La función Canny detecta bordes en la imagen utilizando un enfoque de múltiples etapas.
# Se utilizan dos umbrales: el umbral bajo (50) y el umbral alto (200).
imgCanny = cv2.Canny(img, 50, 200)

# Aplicar un umbral inverso a la imagen resultante de Canny
# La función threshold segmenta la imagen en dos partes, invirtiendo los valores de los píxeles.
# Los píxeles por debajo del umbral se establecen en 255 (blanco) y los que están por encima se establecen en 0 (negro).
_, imgInversa = cv2.threshold(imgCanny, 0, 255, cv2.THRESH_BINARY_INV)

# Mostrar la imagen original y la imagen procesada
cv2.imshow('img original', img)
cv2.imshow('img Canny', imgInversa)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
