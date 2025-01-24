from PIL import Image
import os

# Ruta de la carpeta que contiene las imágenes
folder_path = './taller2/n'
# Dimensiones deseadas
new_size = (800, 600)  # Cambia esto a las dimensiones que desees

# Iterar sobre cada archivo en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Filtrar por tipos de imagen
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            # Redimensionar la imagen
            img = img.resize(new_size)
            # Guardar la imagen redimensionada
            img.save(img_path)

print("Todas las imágenes han sido redimensionadas.")
