import json
import os

avatar_imagen = 'avatar.png'
ruta_avatares = os.path.join(os.getcwd(), "imagenes", "imagenes_perfil", avatar_imagen)

ruta_archivo = os.path.join(os.getcwd(), "datos", "perfil_nuevo.json")

def crear_perfil(values):
    """ Creo el perfil para pasarlo por las diferentes ventanas"""

    perfil = {
        "Usuario": values["-USUARIO-"],
        "Nombre": values["-NOMBRE-"],
        "Edad": values["-EDAD-"],
        "Genero": values["-GENERO-"],
        "Especificar genero": values["-ESPECIFICAR_GENERO-"],
        "Browse": values["-BROWSE-"],
    }
    return perfil

def crear_json(usuario):
    """Le paso el usuario y lo agregar al archivo JSON"""

    datos_agregar = []
    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_agregar = json.load(archivo)
    except (FileNotFoundError, PermissionError, json.JSONDecodeError):
        pass
    datos_agregar.append(usuario)
    return datos_agregar

def existe_nombre(alias):
    """Chequea si ya existe el alias en el archivo JSON."""

    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)
        for nombre_usuario in datos_perfil:
            if nombre_usuario["Usuario"] == alias:
                return True
    except (FileNotFoundError, PermissionError, json.JSONDecodeError):
        return False
    

def verificar_edad(edad):
    """Chequea que la edad ingresada sea un numero entero entre 0-99"""
    try:
        return 99 > int(edad) > 0
    except (TypeError, ValueError):
        return False
    
def llenar_solo(values):
    """Auto completa valores por defecto """
    if values['-BROWSE-'] == '':
        values['-BROWSE-'] = avatar_imagen
    if values['-GENERO-'] == ['Masculino'] or values['-GENERO-'] == ['Femenino']:
        values['-ESPECIFICAR_GENERO-'] = '-'
