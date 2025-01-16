import cv2

# Leer la imagen
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

# Definir los parámetros del texto
color = (255, 255, 255)
grosor = 2
fuente = cv2.FONT_ITALIC
escala = 2

# Agregar texto a la imagen
cv2.putText(img, "me gusta la robotica", (100, 100), fuente, escala, color, grosor)

# Mostrar la imagen
cv2.imshow("Ejemplo 06", img)

# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()