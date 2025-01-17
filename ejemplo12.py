
import cv2

# Leer la imagen
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

alto, ancho, _ =img.shape
escala =0.5
ancho_escalado, alto_escalado = int(ancho*escala), int(alto*escala)

imagen_escalada =cv2.resize(img, (ancho_escalado, alto_escalado))

cv2.imshow('imagen original', img)
cv2.imshow('imagen escalda', imagen_escalada)

cv2.waitKey(0)
cv2.destroyAllWindows()