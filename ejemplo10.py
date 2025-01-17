##### deteccion de color en alguna seccion especifica
import cv2

# Leer la imagen
img = cv2.imread('C:/Users/diego/Desktop/IA/ConjuntoImagenes/Ejemplo01.jpg', 1)

#color = img[30, 160].tolist()
#print(color)

img_original= img.copy()
cv2.imshow('ejemplo', img)
def color(evento, x, y, flags, parametro):
    global img
    if evento == cv2.EVENT_LBUTTONDOWN:
        color = img[y,x].tolist()
        cv2.circle(img,(x,y), 12, color, -1)

        # Mostrar el valor RGB en la imagen
        texto = f"RGB: {color}"
        cv2.putText(img, texto, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        

    elif evento == cv2.EVENT_LBUTTONUP:
        img = img_original.copy()      
    cv2.imshow('ejemplo', img) 

cv2.setMouseCallback('ejemplo', color)        

# Esperar a que se presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas
cv2.destroyAllWindows()