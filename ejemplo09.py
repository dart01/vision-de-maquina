import cv2  # Importa la biblioteca OpenCV para el procesamiento de imágenes
import numpy  # Importa la biblioteca NumPy para trabajar con arreglos

# Crea una imagen en blanco de 600x600 píxeles con 3 canales (RGB)
img = numpy.ones((600, 600, 3), numpy.uint8)
img[:] = (255, 255, 255)  # Establece todos los píxeles a blanco (255, 255, 255)

# Define el color de la línea (rojo) y el grosor de la línea
color = (0, 0, 255)  # Color rojo en formato BGR
grosor = 3  # Grosor de la línea en píxeles

# Carga una imagen desde el disco duro
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)
cv2.imshow('ejemplo', img)  # Muestra la imagen en una ventana llamada 'ejemplo'

# Define la función que se llamará cuando ocurran eventos del mouse
def pintar(evento, x, y, flags, parametros):
    global x_prev, y_prev  # Declara variables globales para las coordenadas previas

    # Si se presiona el botón izquierdo del mouse
    if evento == cv2.EVENT_FLAG_LBUTTON:
        x_prev, y_prev = x, y  # Guarda las coordenadas actuales como las previas

    # Si el mouse se mueve y el botón izquierdo está presionado
    elif evento == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
        # Dibuja una línea desde las coordenadas previas hasta las actuales
        cv2.line(img, (x_prev, y_prev), (x, y), color, grosor)
        x_prev, y_prev = x, y  # Actualiza las coordenadas previas a las actuales

        cv2.imshow('ejemplo', img)  # Muestra la imagen actualizada

# Establece la función 'pintar' como el callback para la ventana 'ejemplo'
cv2.setMouseCallback('ejemplo', pintar)

cv2.waitKey(0)  # Espera indefinidamente hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas de OpenCV
