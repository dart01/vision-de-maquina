##recorte de imagen
##### deteccion de color en alguna seccion especifica
import cv2

color=(0,0,255)
grosor= 2
ancho_min=125

# Leer la imagen
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)
img_original= img.copy()

cv2.imshow('ejemplo', img)

def region (evento, x, y, flags, parametros):
    global x1, y1, img
    if evento == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x , y
    elif evento == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        img = img_original.copy()
        cv2.rectangle(img, (x1, y1), (x, y), color, grosor)
    elif evento == cv2.EVENT_LBUTTONUP:
        if x > x1 and y > y1 and x - x1 > ancho_min:
            img_recortada = img_original[y1:y, x1:x]
            cv2.imshow('recorte imagen', img_recortada)


cv2.setMouseCallback('ejemplo', region)
# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()            