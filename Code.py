import os
import shutil
import ctypes
import winshell

# Función para eliminar archivos y carpetas


def eliminar_archivos(carpeta):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        try:
            if os.path.isfile(ruta_archivo) or os.path.islink(ruta_archivo):
                os.unlink(ruta_archivo)
            elif os.path.isdir(ruta_archivo):
                shutil.rmtree(ruta_archivo)
        except Exception as e:
            print(f'Error al eliminar {ruta_archivo}. Razón: {e}')


# 1. Eliminar archivos temporales
temp_path = os.getenv('TEMP')
eliminar_archivos(temp_path)

# 2. Eliminar archivos de la carpeta de descargas
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
eliminar_archivos(downloads_path)

# 3. Eliminar archivos de la papelera de reciclaje


def vaciar_papelera():
    # Vaciar la papelera de reciclaje
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

    print("La papelera de reciclaje ha sido vaciada.")


if __name__ == "__main__":
    vaciar_papelera()
