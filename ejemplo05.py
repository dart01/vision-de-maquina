import cv2
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',1)


color = (0,255,255)
grosor = 1

cara_x1, cara_x2 = 300, 500
cara_y1, cara_y2 = 20, 200

cv2.rectangle(img, (cara_x1, cara_y1), (cara_x2, cara_y2), color, grosor)

cv2.imshow("ejemplo05", img)

cv2.waitKey(0)
cv2.destroyAllWindows()