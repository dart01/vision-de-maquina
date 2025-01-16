import cv2
import numpy

img = numpy.ones((600,600,3), numpy.uint8)
img[:] = (255,255,255)

color= (0,0,255)
grosor=3

cv2.imshow('ejemplo', img)

def pintar(evento, x, y, flags, parametros):
    global x_prev, y_prev
    if evento== cv2.EVENT_FLAG_LBUTTON:
        x_prev, y_prev = x, y
    elif evento == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
        cv2.line(img, (x_prev, y_prev), (x,y), color, grosor)
        x_prev, y_prev = x, y

        cv2.imshow('ejemplo', img)    

cv2.setMouseCallback('ejemplo', pintar)

cv2.waitKey(0)
cv2.destroyAllWindows()