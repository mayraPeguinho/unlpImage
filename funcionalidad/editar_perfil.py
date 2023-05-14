import os

def mostrar_perfil(perfil_actual,window):
    """ Guardo los valores del perfil"""
        
    window['Nombre'].update(perfil_actual['Nombre']),
    window['Edad'].update(perfil_actual['Edad']),
    window['Genero'].update(perfil_actual['Genero']),
    window['Especificar genero'].update(perfil_actual['Especificar genero']),
    window['-BROWSE-'].update(perfil_actual['Avatar']),

    return(window)
    
    


def modificar_perfil(cambios_perfil):
    """ Le asigno al perfil actual los nuevo valores actualizados"""
    
    cambios_perfil = {
        'Nombre': cambios_perfil['Nombre'],
        'Edad': cambios_perfil['Edad'],
        'Genero': cambios_perfil['Genero'],
        'Especificar genero': cambios_perfil['Especificar genero'],
        'Avatar': os.path.basename(cambios_perfil['-BROWSE-']),
    }
    return cambios_perfil
