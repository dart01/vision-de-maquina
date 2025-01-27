# Guía de Estudio para el Parcial Final del Seminario de Profundización en Visión de Máquina

## 1. Filtros en Visión de Máquina

### 1.1 Filtro Simple
- **Descripción**: Se utiliza para calcular el histograma de una imagen y visualizar la distribución de intensidades.
- **Código**:
```python
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 0)
hist = cv2.calcHist(img, [0], None, [256], [0, 256])
print(hist)
cv2.imshow('imagen', img)
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Análisis de contraste y iluminación de la imagen.

### 1.2 Umbralización
- **Descripción**: Segmenta la imagen en dos partes, utilizando un valor de umbral.
- **Código**:
```python
import cv2

def actualizarImagen(umbral):
    _, umbralizado = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY)
    cv2.imshow('imagen filtrada', umbralizado)

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 0)
cv2.imshow('imagen original', img)
cv2.createTrackbar('umbral', 'imagen original', 0, 255, actualizarImagen)
actualizarImagen(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Detección de objetos y segmentación.

### 1.3 Umbralización de Otsu
- **Descripción**: Calcula automáticamente el umbral óptimo para segmentar la imagen.
- **Código**:
```python
import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 0)
umbral, umbralizado = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('img filtrada', umbralizado)
print(f"El umbral calculado por Otsu es: {umbral}")
cv2.imshow('imagen original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Segmentación efectiva en imágenes con variaciones de iluminación.

### 1.4 Umbralización Adaptativa
- **Descripción**: Calcula el umbral para diferentes regiones de la imagen.
- **Código**:
```python
import cv2

def actualizarBloque(blq):
    global bloque
    bloque = blq
    if bloque < 3:
        bloque = 3
    elif bloque % 2 == 0:
        bloque += 1
    imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
    cv2.imshow('imagen filtrada', imgUmbralizada)

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/tabla_numeros.jpg', 0)
imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
cv2.imshow('imagen original', img)
cv2.imshow('imagen filtrada', imgUmbralizada)
cv2.createTrackbar('Bloque', 'imagen original', 0, 100, actualizarBloque)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Segmentación en condiciones de iluminación variable.

### 1.5 Filtro Pasa Bajo
- **Descripción**: Suaviza o difumina la imagen.
- **Código**:
```python
import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)
imgSuavizada = cv2.blur(img, (10, 10))
cv2.imshow('imagen original', img)
cv2.imshow('imagen suavizada', imgSuavizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Reducción de ruido y detalles finos.

### 1.6 Filtro Pasa Alto
- **Descripción**: Resalta detalles y bordes en la imagen.
- **Código**:
```python
import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)
imgFiltroPasaBajo = cv2.blur(img, (10, 10))
imgFiltroPasaAlto = cv2.subtract(img, imgFiltroPasaBajo)
cv2.imshow('imagen original', img)
cv2.imshow('imagen con filtro pasa alto', imgFiltroPasaAlto)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Detección de características importantes.

### 1.7 Filtros Morfológicos
- **Descripción**: Modifican la forma de los objetos en la imagen.
- **Código**:
```python
import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/MorfologicoRuido.jpg', 0)
erosion = cv2.erode(img, kernel)
dilatada = cv2.dilate(img, kernel)
cv2.imshow('imagen original', img)
cv2.imshow('img erosionada', erosion)
cv2.imshow('imagen dilatada', dilatada)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Eliminación de ruido y segmentación.

### 1.8 Detección de Bordes con Canny
- **Descripción**: Detecta bordes en la imagen.
- **Código**:
```python
import cv2  

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)
imgCanny = cv2.Canny(img, 50, 200)
_, imgInversa = cv2.threshold(imgCanny, 0, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('img original', img)
cv2.imshow('img Canny', imgInversa)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- **Aplicaciones**: Segmentación y detección de contornos.

## Conclusión
Esta guía cubre los aspectos fundamentales de los filtros en visión por computadora, incluyendo su funcionamiento y aplicaciones. Asegúrate de practicar con los códigos y entender cómo cada filtro afecta a las imágenes.
