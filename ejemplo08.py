import cv2
import numpy

img = numpy.ones((600,600,3), numpy.uint8)
img[:] = (255,255,255)

color= (0,0,255)
grosor=3
fuente=cv2.FONT_ITALIC
escala=1

cv2.imshow('eventos mouse', img)

def eventos_raton(evento, x, y, flags, parametros):
    if evento == cv2.EVENT_FLAG_LBUTTON:
        cv2.putText(img, "click izquiero", (x,y), fuente, escala, color, grosor) 
    elif evento == cv2.EVENT_RBUTTONDOWN:
        cv2.putText(img, "click derecho", (x,y), fuente, escala, color, grosor)   

    cv2.imshow('eventos mouse', img)

cv2.setMouseCallback('eventos mouse', eventos_raton)

cv2.waitKey(0)
cv2.destroyAllWindows()