##### cargar y vizualizar ####

import cv2

# 1. Cargar la imagen --- > imread ('Nombre de esa imagen' --- Ubicación de la imagen en el equipo)
# IMREAD_GRAYSCALE --- Escala de grises _ 0
# IMREAD_COLOR --- Color _ 1
# IMREAD_UNCHANGE --- -1

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',1)


img_byn = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)



# 2. Visualizar la imagen 
cv2.imshow('CuadroEjemplo', img_byn)

# 3. Debemos utilizar instrucciones que generen una interrupción 
cv2.waitKey(0)
cv2.destroyAllWindows()