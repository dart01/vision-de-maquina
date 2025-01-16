import cv2
import numpy as np

img = cv2.imread('C:/Users/diego/Desktop/taller1/isometrico.png',1) #imagen del isometrico 
#img = np.ones((600,600,3), np.uint8)

def click_event(event, x, y, flags, params):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 2:
            cv2.line(img, points[0], points[1], (0, 0, 255), 2)#dibujando lineas rojas
            points = []  # Reset for the next line

    cv2.imshow('Image', img)

points = []

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()