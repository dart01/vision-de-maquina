##### Cargar y Visualizar ####

import cv2

# Tamaño de la imagen
# 2. Ancho y alto
# 3. Canal de color
# 4. Que tipo de datos manejan las distancias

# Asegúrate de que la ruta sea correcta
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

# Verificar si la imagen se ha cargado correctamente
if img is None:
    print("Error al cargar la imagen")
else:
    cv2.imshow('Ejemplo 02', img)

    # Extraer las capas de color de la imagen
    img_b, img_g, img_r = cv2.split(img)
    cv2.imshow('B', img_b)
    cv2.imshow('G', img_g)
    cv2.imshow('R', img_r)

    # Otras características
    Alto, Ancho, Canales = img.shape
    tam = img.size
    tipo = img.dtype

    print("Tamaño: " + str(tam) + " bytes")
    print("Ancho: " + str(Ancho) + " pixeles")
    print("Alto: " + str(Alto) + " pixeles")
    print("# Canales: " + str(Canales))
    print("Tipo: " + str(tipo))

    cv2.waitKey(0)
    cv2.destroyAllWindows()