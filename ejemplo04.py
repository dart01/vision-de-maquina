import cv2
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',1)

alto, ancho, _ = img.shape

color = (0,0,255)
grosor = 1
cuadricula = 10

for x in range (0, ancho +1, cuadricula):
    img = cv2.line(img,(x,0), (x,alto), color, grosor)
for y in range (0, alto + 1, cuadricula):
    img = cv2.line(img, (0,y), (ancho, y), color, grosor)

cv2.imshow('Ejemplo04', img)

cv2.waitKey(0)
cv2.destroyAllWindows()