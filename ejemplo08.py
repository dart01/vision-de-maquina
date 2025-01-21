import cv2  # Importa la biblioteca OpenCV para el procesamiento de imágenes
import numpy  # Importa la biblioteca NumPy para manejar arreglos numéricos

# Crea una imagen de 600x600 píxeles, inicializada con valores de 1 (blanco)
img = numpy.ones((600, 600, 3), numpy.uint8)
img[:] = (255, 255, 255)  # Establece todos los píxeles a blanco

# Configuración de parámetros para el texto que se dibujará en la imagen
color = (0, 0, 255)  # Color rojo en formato BGR
grosor = 3  # Grosor de la línea del texto
fuente = cv2.FONT_ITALIC  # Tipo de fuente (itálica)
escala = 1  # Escala del texto

# Carga una imagen desde la ruta especificada y la muestra en una ventana
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)
cv2.imshow('eventos mouse', img)  # Muestra la imagen en una ventana llamada 'eventos mouse'

# Definición de la función que maneja los eventos del mouse
def eventos_raton(evento, x, y, flags, parametros):
    # Verifica si se ha hecho clic izquierdo
    if evento == cv2.EVENT_FLAG_LBUTTON:
        # Dibuja el texto "click izquierdo" en las coordenadas (x, y)
        cv2.putText(img, "click izquiero", (x, y), fuente, escala, color, grosor) 
    # Verifica si se ha hecho clic derecho
    elif evento == cv2.EVENT_RBUTTONDOWN:
        # Dibuja el texto "click derecho" en las coordenadas (x, y)
        cv2.putText(img, "click derecho", (x, y), fuente, escala, color, grosor)   

    # Muestra la imagen actualizada con el texto agregado
    cv2.imshow('eventos mouse', img)

# Establece un callback que vincula la ventana 'eventos mouse' con la función eventos_raton
cv2.setMouseCallback('eventos mouse', eventos_raton)

# Espera indefinidamente hasta que se presione una tecla
cv2.waitKey(0)
# Cierra todas las ventanas abiertas por OpenCV
cv2.destroyAllWindows()