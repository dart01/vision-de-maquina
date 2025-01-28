import cv2  # Importa la biblioteca OpenCV, que se utiliza para el procesamiento de imágenes y visión por computadora.

# Cargar el clasificador en cascada para vehículos
#car_cascade = cv2.CascadeClassifier('C:/Users/diego/Desktop/IA/taller2/cars.xml')
car_cascade = cv2.CascadeClassifier('C:/Users/diego/Desktop/IA/taller2/cascade.xml')
# Se crea un objeto CascadeClassifier que carga un modelo preentrenado para detectar vehículos. 
# El archivo 'cars.xml' contiene los datos del clasificador.

# Verificar si el clasificador se cargó correctamente
if car_cascade.empty():
    print("Error: No se pudo cargar el clasificador.")
    exit()
# Se verifica si el clasificador se ha cargado correctamente. 
# Si no se ha cargado, se imprime un mensaje de error y se termina la ejecución del programa.

image_path = 'C:/Users/diego/Desktop/IA/taller2/imagen3.jpg'  # Cambia esto según la imagen que desees usar
# Se define la ruta de la imagen que se va a procesar. 
# Puedes cambiar 'imagen2.jpg' por cualquier otra imagen que desees usar.

# Leer la imagen
image = cv2.imread(image_path)
# Se utiliza cv2.imread para leer la imagen desde la ruta especificada y se almacena en la variable 'image'.

if image is None:
    print("Error: No se pudo cargar la imagen.")
    exit()
# Se verifica si la imagen se ha cargado correctamente. 
# Si 'image' es None, significa que no se pudo cargar la imagen, se imprime un mensaje de error y se termina la ejecución.


# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Se convierte la imagen a escala de grises utilizando cv2.cvtColor. 
# Esto es necesario porque el clasificador en cascada funciona mejor con imágenes en escala de grises.

# Detectar vehículos
vehicles = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# Se utiliza el método detectMultiScale para detectar vehículos en la imagen en escala de grises. 
# 'scaleFactor' especifica cuánto se reduce la imagen en cada escala, y 'minNeighbors' define cuántos vecinos debe tener un rectángulo para retenerlo.

# Contar vehículos detectados
vehicle_count = len(vehicles)
# Se cuenta el número de vehículos detectados al obtener la longitud de la lista 'vehicles'.

# Dibujar rectángulos alrededor de los vehículos detectados
for (x, y, w, h) in vehicles:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Se itera sobre cada vehículo detectado y se dibuja un rectángulo alrededor de él en la imagen original. 
# (x, y) son las coordenadas de la esquina superior izquierda del rectángulo, y (w, h) son el ancho y la altura del rectángulo. 
# El color del rectángulo es azul (255, 0, 0) y el grosor es 2 píxeles.

# Mostrar la imagen con los vehículos detectados
cv2.imshow('Vehículos detectados', image)
# Se muestra la imagen con los vehículos detectados en una ventana titulada 'Vehículos detectados'.

# Imprimir la cantidad de vehículos detectados
print(f'Cantidad de vehículos detectados: {vehicle_count}')
# Se imprime en la consola la cantidad de vehículos que han sido detectados.

cv2.waitKey(0)  # Espera a que se presione una tecla para cerrar la ventana de la imagen.
cv2.destroyAllWindows() 

