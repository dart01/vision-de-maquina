#filtro simple
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',0)

hist = cv2.calcHist(img, [0], None, [256], [0, 256])

print(hist)

cv2.imshow('imagen', img)
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
