import cv2
import matplotlib.pyplot as plt

def mostrar_histograma(image_path, color='gray'):
    """
    Carga una imagen y muestra su histograma.
    
    :param imag Ruta de la imagen a cargar.
    :param color Color del histograma ('gray' para escala de grises, 'color' para color).
    """
    # Cargar la imagen
    image = cv2.imread(image_path)
    

    # Convertir a escala de grises si se selecciona 'gray'
    if color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Calcular el histograma en escala de grises
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
        
        # Mostrar el histograma
        plt.figure(figsize=(10, 5))
        plt.title('Histograma de la Imagen en Escala de Grises')
        plt.xlabel('Intensidad de Pixel')
        plt.ylabel('Número de Pixeles')
        plt.plot(histogram, color='black')
        plt.xlim([0, 256])
        plt.grid()
        plt.show()
    
    # Si se selecciona 'color', calcular el histograma para cada canal
    elif color == 'color':
        colors = ('b', 'g', 'r')
        plt.figure(figsize=(10, 5))
        plt.title('Histograma de la Imagen en Color')
        plt.xlabel('Intensidad de Pixel')
        plt.ylabel('Número de Pixeles')
        
        for i, col in enumerate(colors):
            histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histogram, color=col)
        
        plt.xlim([0, 256])
        plt.grid()
        plt.show()
    else:
        print("Error: Color no válido. Usa 'gray' o 'color'.")

# Ejemplo de uso
mostrar_histograma('ConjuntoImagenes/Ejemplo01.jpg', color='gray')  # Cambia 'gray' a 'color' para el histograma en color
