import cv2
import numpy as np

img = cv2.imread('C:/Users/diego/Desktop/taller1/laberinto.png', 1)  # Imagen del isométrico
# img = np.ones((600,600,3), np.uint8)  # Si prefieres usar una imagen en blanco

def click_event(event, x, y, flags, params):
    global points, last_point
    if event == cv2.EVENT_LBUTTONDOWN:
        if last_point is None:
            # Si no hay un punto anterior, simplemente guarda el punto actual
            last_point = (x, y)
        else:
            # Dibuja una línea desde el último punto al punto actual
            cv2.line(img, last_point, (x, y), (0, 0, 255), 2)
            # Actualiza el último punto al punto actual
            last_point = (x, y)
        
        cv2.imshow('Image', img)

points = []
last_point = None  # Variable para almacenar el último punto

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()