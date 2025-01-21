############### Barra de desplazamiento y selección ###################

import cv2  # Importa la biblioteca OpenCV para procesamiento de imágenes

# Carga una imagen desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

# Crea una copia de la imagen original para poder modificarla sin perder la original
img_original = img.copy()

# Define el color (rojo en este caso), grosor de la línea, fuente y escala del texto
color = (0, 0, 255)  # Color rojo en formato BGR
grosor = 2  # Grosor del texto
fuente = cv2.FONT_ITALIC  # Tipo de fuente para el texto
escala = 0.5  # Escala del texto
alto_imagen, ancho_imagen, canales = img.shape  # Obtiene las dimensiones de la imagen

def actualizar_imagen(escala):
    """
    Actualiza la imagen mostrando el texto con el tamaño de la escala proporcionada.
    """
    img = img_original.copy()  # Copia la imagen original
    posicion_x, posicion_y = centrarImagen(escala)  # Calcula la posición centrada del texto
    # Añade el texto a la imagen en la posición calculada
    cv2.putText(img, "Ejemplo de barra", (posicion_x, posicion_y), fuente, escala, color, grosor)
    cv2.imshow('Ejemplo', img)  # Muestra la imagen actualizada en una ventana

def centrarImagen(escala):
    """
    Calcula la posición centrada del texto en la imagen.
    """
    # Obtiene el tamaño del texto que se va a dibujar
    (ancho_texto, alto_texto), _ = cv2.getTextSize("Ejemplo de barra", fuente, escala, grosor)
    # Calcula la posición x para centrar el texto
    posicion_x = int((ancho_imagen - ancho_texto) / 2)
    # Calcula la posición y para centrar el texto
    posicion_y = int((alto_imagen + alto_texto) / 2)
    return posicion_x, posicion_y  # Devuelve las coordenadas centradas

# Calcula la posición centrada inicial del texto
posicion_x, posicion_y = centrarImagen(escala)

# Dibuja el texto en la imagen original en la posición centrada
cv2.putText(img, "Ejemplo de barra", (posicion_x, posicion_y), fuente, escala, color, grosor)
cv2.imshow('Ejemplo', img)  # Muestra la imagen con el texto

# Crea una barra de desplazamiento (trackbar) para ajustar la escala del texto
cv2.createTrackbar('Escala', 'Ejemplo', 0, 20, actualizar_imagen)

cv2.waitKey(0)  # Espera a que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas