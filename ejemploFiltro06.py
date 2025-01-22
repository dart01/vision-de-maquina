#filtro pasa alto ---> resaltar detalles de imagen 'filtro de gradiente'
import cv2

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/FiltroPasaBajo.jpg', 0)

imgFiltroPasaBajo = cv2.blur(img,(10,10))
# Aplicar el filtro pasa alto
imgFiltroPasaAlto = cv2.subtract(img, imgFiltroPasaBajo)



cv2.imshow('imagen original', img)
cv2.imshow('imagen con filtro pasa alto',imgFiltroPasaAlto )

cv2.waitKey(0)
cv2.destroyAllWindows()



#filtro sobler-laplaciano-charr