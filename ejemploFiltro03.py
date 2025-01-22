# Filtro Otsu
import cv2  # Importar la biblioteca OpenCV para procesamiento de imágenes

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 0)

# Aplicar el método de umbralización de Otsu
# cv2.threshold toma la imagen, un umbral inicial (0), el valor máximo (255) y el tipo de umbral (THRESH_OTSU)
# Devuelve el umbral calculado y la imagen umbralizada
umbral, umbralizado = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

# Mostrar la imagen umbralizada en una ventana
cv2.imshow('img filtrada', umbralizado)

# Imprimir el umbral calculado por el método de Otsu en la consola
print(f"El umbral calculado por Otsu es: {umbral}")

# Mostrar la imagen original en una ventana
cv2.imshow('imagen original', img)

# Esperar a que se presione una tecla y cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
