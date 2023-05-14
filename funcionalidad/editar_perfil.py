import os

def mostrar_perfil(perfil_actual):
    """ Guardo los valores del perfil"""

    perfil = {
        "Nombre": perfil_actual["-NOMBRE-"],
        "Edad": perfil_actual["-EDAD-"],
        "Genero": perfil_actual["-GENERO-"],
        "Especificar genero": perfil_actual["-ESPECIFICAR_GENERO-"],
        "Avatar": perfil_actual["-BROWSE-"],
    }
    return perfil

def modificar_perfil(perfil_actual, cambios_perfil):
    cambios_perfil = {
        perfil_actual['-NOMBRE-']: cambios_perfil['-NOMBRE-'],
        perfil_actual['-EDAD-']: cambios_perfil['-EDAD-'],
        perfil_actual['-GENERO-']: cambios_perfil['-GENERO-'],
        perfil_actual['-ESPECIFICAR_GENERO-']: cambios_perfil['-ESPECIFICAR_GENERO-'],
        perfil_actual['-BROWSE-']: os.path.basename(cambios_perfil['-BROWSE-']),
    }
    return cambios_perfil
