import cv2
import numpy as np

# Tamaño del tablero y celdas
TAMANO_TABLERO = 600
TAMANO_CELDA = TAMANO_TABLERO // 3

# Crear una imagen en blanco
img = np.ones((TAMANO_TABLERO, TAMANO_TABLERO, 3), np.uint8) * 255

# Inicializar el tablero
tablero = [[None for _ in range(3)] for _ in range(3)]

# Variable para alternar entre "X" y "O"
turno = "X"

# Función para dibujar una "X"
def dibujar_x(x, y):
    cv2.line(img, (x, y), (x + TAMANO_CELDA, y + TAMANO_CELDA), (0, 0, 255), 3)
    cv2.line(img, (x + TAMANO_CELDA, y), (x, y + TAMANO_CELDA), (0, 0, 255), 3)

# Función para dibujar un "O"
def dibujar_o(x, y):
    centro = (x + TAMANO_CELDA // 2, y + TAMANO_CELDA // 2)
    radio = TAMANO_CELDA // 2 - 10
    cv2.circle(img, centro, radio, (255, 0, 0), 3)

# Función para dibujar las líneas del tablero
def dibujar_tablero():
    for i in range(1, 3):
        # Líneas verticales
        cv2.line(img, (i * TAMANO_CELDA, 0), (i * TAMANO_CELDA, TAMANO_TABLERO), (0, 0, 0), 2)
        # Líneas horizontales
        cv2.line(img, (0, i * TAMANO_CELDA), (TAMANO_TABLERO, i * TAMANO_CELDA), (0, 0, 0), 2)

# Función para verificar si hay un ganador
def verificar_ganador():
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] is not None:
            return fila[0], "fila", tablero.index(fila)
    
    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] is not None:
            return tablero[0][columna], "columna", columna
    
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not None:
        return tablero[0][0], "diagonal", 0
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not None:
        return tablero[0][2], "diagonal", 1
    
    return None, None, None
def tachar_linea(ganador, tipo, indice):
    if tipo == "fila":
        y = indice * TAMANO_CELDA + TAMANO_CELDA // 2
        cv2.line(img, (10, y), (TAMANO_TABLERO - 10, y), (0, 255, 0), 5)
    elif tipo == "columna":
        x = indice * TAMANO_CELDA + TAMANO_CELDA // 2
        cv2.line(img, (x, 10), (x, TAMANO_TABLERO - 10), (0, 255, 0), 5)
    elif tipo == "diagonal":
        if indice == 0:
            cv2.line(img, (10, 10), (TAMANO_TABLERO - 10, TAMANO_TABLERO - 10), (0, 255, 0), 5)
        else:
            cv2.line(img, (TAMANO_TABLERO - 10, 10), (10, TAMANO_TABLERO - 10), (0, 255, 0), 5)

# Función para manejar los clics del mouse
def pintar(evento, x, y, flags, parametros):
    global turno

    if evento == cv2.EVENT_LBUTTONDOWN:
        # Determinar la celda en la que se hizo clic
        fila = y // TAMANO_CELDA
        columna = x // TAMANO_CELDA

        # Verificar si la celda está vacía
        if tablero[fila][columna] is None:
            # Dibujar "X" o "O" según el turno
            if turno == "X":
                dibujar_x(columna * TAMANO_CELDA, fila * TAMANO_CELDA)
                tablero[fila][columna] = "X"
                turno = "O"
            else:
                dibujar_o(columna * TAMANO_CELDA, fila * TAMANO_CELDA)
                tablero[fila][columna] = "O"
                turno = "X"

            # Verificar si hay un ganador
            ganador, tipo, indice = verificar_ganador()
            if ganador is not None:
                print(f"¡El ganador es {ganador}!")
                tachar_linea(ganador, tipo, indice)

            # Actualizar la imagen
            cv2.imshow('Triqui', img)

# Dibujar el tablero inicial
dibujar_tablero()

# Mostrar la imagen inicial
cv2.imshow('Triqui', img)

# Asignar la función de manejo de clics
cv2.setMouseCallback('Triqui', pintar)

# Esperar a que se cierre la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()