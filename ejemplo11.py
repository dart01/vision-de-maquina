## Recorte de imagen
##### Detección de color en alguna sección específica

import cv2  # Importar la biblioteca OpenCV para procesamiento de imágenes

# Definición de variables para el color del rectángulo, grosor y ancho mínimo
color = (0, 0, 255)  # Color rojo en formato BGR
grosor = 2  # Grosor del rectángulo
ancho_min = 125  # Ancho mínimo para considerar el recorte

# Leer la imagen desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)
img_original = img.copy()  # Hacer una copia de la imagen original para usarla más tarde

# Mostrar la imagen original en una ventana llamada 'ejemplo'
cv2.imshow('ejemplo', img)

# Definición de la función que manejará los eventos del mouse
def region(evento, x, y, flags, parametros):
    global x1, y1, img  # Declarar variables globales para las coordenadas y la imagen
    if evento == cv2.EVENT_LBUTTONDOWN:  # Si se presiona el botón izquierdo del mouse
        x1, y1 = x, y  # Guardar las coordenadas iniciales del clic
    elif evento == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # Si se mueve el mouse mientras se mantiene presionado el botón izquierdo
        img = img_original.copy()  # Restaurar la imagen original
        # Dibujar un rectángulo desde las coordenadas iniciales hasta la posición actual del mouse
        cv2.rectangle(img, (x1, y1), (x, y), color, grosor)
    elif evento == cv2.EVENT_LBUTTONUP:  # Si se suelta el botón izquierdo del mouse
        # Verificar que el rectángulo tenga un tamaño válido
        if x > x1 and y > y1 and x - x1 > ancho_min:
            # Recortar la imagen usando las coordenadas del rectángulo
            img_recortada = img_original[y1:y, x1:x]
            # Mostrar la imagen recortada en una nueva ventana
            cv2.imshow('recorte imagen', img_recortada)

# Configurar la función de callback para manejar eventos del mouse en la ventana 'ejemplo'
cv2.setMouseCallback('ejemplo', region)

# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
