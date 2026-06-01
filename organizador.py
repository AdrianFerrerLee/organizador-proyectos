import os
import shutil

# Carpeta que quieres organizar (cambia esta ruta por la tuya)
carpeta = "/Users/adrianferrer/Downloads"

# Definimos qué extensiones van a cada carpeta
destinos = {
    "briefs":        [".pdf"],
    "presupuestos":  [".xlsx", ".xls", ".xlsm"],
    "video":         [".mov", ".mp4"],
    "creatividades": [".ai", ".psd", ".png", ".jpg"],
}

# Recorremos todos los archivos de la carpeta
for archivo in os.listdir(carpeta):
    
    # Obtenemos la extensión del archivo (.pdf, .xlsx, etc.)
    nombre, extension = os.path.splitext(archivo)
    extension = extension.lower()
    
    # Buscamos a qué carpeta pertenece
    for carpeta_destino, extensiones in destinos.items():
        if extension in extensiones:
            
            # Creamos la carpeta destino si no existe
            ruta_destino = os.path.join(carpeta, carpeta_destino)
            os.makedirs(ruta_destino, exist_ok=True)
            
            # Movemos el archivo
            ruta_origen = os.path.join(carpeta, archivo)
            shutil.move(ruta_origen, ruta_destino)
            print(f"✅ {archivo} → {carpeta_destino}/")

print("¡Listo! Archivos organizados.")