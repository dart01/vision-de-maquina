##### Detección de color en alguna sección específica
import cv2  # Importar la biblioteca OpenCV para procesamiento de imágenes

# Leer la imagen desde la ruta especificada
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

# Hacer una copia de la imagen original para restaurarla más tarde
img_original = img.copy()

# Mostrar la imagen original en una ventana llamada 'ejemplo'
cv2.imshow('ejemplo', img)

# Definir la función de callback para manejar eventos del mouse
def color(evento, x, y, flags, parametro):
    global img  # Hacer referencia a la variable global img
    if evento == cv2.EVENT_LBUTTONDOWN:  # Si se presiona el botón izquierdo del mouse
        # Obtener el color en la posición (x, y) de la imagen
        color = img[y, x].tolist()
        # Dibujar un círculo en la posición (x, y) con el color obtenido
        cv2.circle(img, (x, y), 12, color, -1)

        # Mostrar el valor RGB en la imagen
        texto = f"RGB: {color}"  # Formatear el texto con el valor RGB
        cv2.putText(img, texto, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    elif evento == cv2.EVENT_LBUTTONUP:  # Si se suelta el botón izquierdo del mouse
        # Restaurar la imagen original
        img = img_original.copy()      
    
    # Mostrar la imagen actualizada en la ventana
    cv2.imshow('ejemplo', img) 

# Configurar la función de callback para la ventana 'ejemplo'
cv2.setMouseCallback('ejemplo', color)        

# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
