#filtro otsu
import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',0)

umbral, umbralizado = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('img filtrada', umbralizado)
print(f"El umbral calculado por Otsu es: {umbral}")
cv2.imshow('imagen original', img)


cv2.waitKey(0)
cv2.destroyAllWindows()