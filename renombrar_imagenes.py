import os

# Ruta de la carpeta que contiene las imágenes
folder_path = './taller2/p'

# Obtener la lista de archivos en la carpeta
files = os.listdir(folder_path)

# Renombrar las imágenes
for index, filename in enumerate(files):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Filtrar por tipos de imagen
        new_name = f'objeto{index + 1}.jpg'  # Cambiar la extensión según sea necesario
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

print("Las imágenes han sido renombradas.")
