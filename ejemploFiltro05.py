#filtro pasa bajo ---> suavizar o difuminar 
import cv2

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)

imgSuavizada= cv2.blur(img, (10,10))

cv2.imshow('imagen original', img)
cv2.imshow('imagen suavizada', imgSuavizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
