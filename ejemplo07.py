############### Barra dedesplazamiento y selección ###################

import cv2

img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg',1)

img_original = img.copy()

color = (0, 0, 255)
grosor = 2 
fuente = cv2.FONT_ITALIC
escala = 0.5 
alto_imagen, ancho_imagen, canales = img.shape

def actualizar_imagen(escala):
    img = img_original.copy()
    posicion_x, posicion_y = centrarImagen(escala)
    cv2.putText(img, "Ejemplo de barra", (posicion_x, posicion_y), fuente, escala, color, grosor)
    cv2.imshow('Ejemplo', img)
    
def centrarImagen(escala):
    (ancho_texto, alto_texto), _ = cv2.getTextSize("Ejemplo de barra", fuente, escala, grosor)
    posicion_x = int((ancho_imagen - ancho_texto) / 2)
    posicion_y = int((alto_imagen  + alto_texto) / 2)
    return posicion_x, posicion_y

posicion_x, posicion_y = centrarImagen(escala)

cv2.putText(img, "Ejemeplo de barra", (posicion_x,posicion_y), fuente, escala, color, grosor)
cv2. imshow('Ejemplo', img)

cv2.createTrackbar('Escala', 'Ejemplo', 0, 20, actualizar_imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()