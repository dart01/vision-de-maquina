import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
img = 'ConjuntoImagenes/Ejemplo01.jpg'  # Cambia esto si necesitas otra imagen
imagen = cv2.imread(img)


# Convertir a escala de grises
gray_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen en gris',gray_image)
# Calcular el histograma
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Mostrar el histograma
plt.figure(figsize=(10, 5))
plt.title('Histograma de la Imagen')
plt.xlabel('Intensidad de Pixel')
plt.ylabel('Número de Pixeles')
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()
