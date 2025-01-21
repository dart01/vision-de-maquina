# Importar la biblioteca OpenCV para procesamiento de imágenes
import cv2

# Inicializar el tamaño del bloque y la constante para el umbral adaptativo
bloque = 3  # Tamaño del bloque para el cálculo del umbral
constante = 0  # Constante que se resta del valor medio de la vecindad

# Función para actualizar el tamaño del bloque
def actualizarBloque(blq):
    global bloque  # Declarar que se usará la variable global 'bloque'
    bloque = blq  # Asignar el nuevo valor del bloque
    # Asegurarse de que el bloque sea al menos 3 y que sea impar
    if bloque < 3: 
        bloque = 3
    elif bloque % 2 == 0: 
        bloque += 1  # Aumentar el bloque para que sea impar
    # Aplicar el umbral adaptativo a la imagen
    imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
    # Mostrar la imagen umbralizada
    cv2.imshow('imagen filtrada', imgUmbralizada)

# Función para actualizar la constante
def actualizarConstante(cte):
    global constante  # Declarar que se usará la variable global 'constante'
    constante = cte  # Asignar el nuevo valor de la constante
    # Aplicar el umbral adaptativo a la imagen
    imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)
    # Mostrar la imagen umbralizada
    cv2.imshow('imagen filtrada', imgUmbralizada)

# Leer la imagen en escala de grises desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/tabla_numeros.jpg', 0)
# Aplicar el umbral adaptativo a la imagen inicial
imgUmbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bloque, constante)

# Mostrar la imagen original
cv2.imshow('imagen original', img)
# Mostrar la imagen umbralizada
cv2.imshow('imagen filtrada', imgUmbralizada)

# Crear una barra de seguimiento para ajustar el tamaño del bloque
cv2.createTrackbar('Bloque', 'imagen original', 0, 100, actualizarBloque)
# Crear una barra de seguimiento para ajustar la constante
cv2.createTrackbar('constante', 'imagen original', 0, 255, actualizarConstante)

# Esperar a que se presione una tecla
cv2.waitKey(0)
# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
