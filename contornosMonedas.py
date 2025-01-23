##################### CONTADOR MONEDAS 02 ########################
import cv2  # Importa la biblioteca OpenCV para procesamiento de imágenes

# Definición de parámetros para el texto que se mostrará en la imagen
fuente = cv2.FONT_HERSHEY_COMPLEX  # Tipo de fuente para el texto
color = (0, 255, 255)  # Color del texto en formato BGR (amarillo)
grosor = 2  # Grosor del texto
escala = 1  # Escala del texto
# Posiciones donde se mostrará el texto en la imagen
posicion_texto_1 = (20, 30)
posicion_texto_2 = (20, 60)
posicion_texto_5 = (20, 90)

umbral = 120  # Valor de umbral para la binarización de la imagen

# Se declaran las variables que contienen el área mínima para cada moneda
area_min_1 = 4000  # Área mínima para monedas de 1 centavo
area_min_2 = 6000  # Área mínima para monedas de 2 centavos
area_min_5 = 8000  # Área mínima para monedas de 5 centavos

# Inicialización de contadores para cada tipo de moneda
num_monedas_1 = num_monedas_2 = num_monedas_5 = 0

# Carga la imagen de las monedas
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/monedas.jpg')
# Convierte la imagen a escala de grises
img_byn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Aplica un umbral para binarizar la imagen
_, img_umbral = cv2.threshold(img_byn, umbral, 255, cv2.THRESH_BINARY_INV)
# Encuentra los contornos en la imagen umbralizada
contornos, _ = cv2.findContours(img_umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img, contornos, -1, color, grosor)  # (opcional) Dibuja los contornos en la imagen original

# Itera sobre cada contorno encontrado
for contorno in contornos:
    area = abs(cv2.contourArea(contorno, True))  # Calcula el área del contorno
    # Clasifica las monedas según su área
    if area >= area_min_5: 
        num_monedas_5 += 1  # Incrementa el contador de monedas de 5 centavos
    elif area >= area_min_2: 
        num_monedas_2 += 1  # Incrementa el contador de monedas de 2 centavos
    elif area >= area_min_1: 
        num_monedas_1 += 1  # Incrementa el contador de monedas de 1 centavo

# Muestra el número de monedas contadas en la imagen
cv2.putText(img, "Monedas de 1 centimo:  " + str(num_monedas_1), posicion_texto_1, fuente, escala, color, grosor)
cv2.putText(img, "Monedas de 2 centimos: " + str(num_monedas_2), posicion_texto_2, fuente, escala, color, grosor)
cv2.putText(img, "Monedas de 5 centimos: " + str(num_monedas_5), posicion_texto_5, fuente, escala, color, grosor)

# Muestra la imagen con los resultados
cv2.imshow('Contornos', img)

cv2.waitKey(0)  # Espera a que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV

