import os

def mostrar_perfil(perfil_actual,window):
    """ Guardo los valores del perfil"""
        
    window['Nombre'].update(perfil_actual['Nombre']),
    window['Edad'].update(perfil_actual['Edad']),
    window['Genero'].update(perfil_actual['Genero']),
    window['Especificar genero'].update(perfil_actual['Especificar genero']),
    window['-BROWSE-'].update(perfil_actual['Avatar']),

    return(window)
    
    
def modificar_perfil(perfil_actual,cambios_perfil):
    """ Le asigno al perfil actual los nuevo valores actualizados"""

    perfil_actual['Nombre'] = cambios_perfil['Nombre']
    perfil_actual['Edad'] = cambios_perfil['Edad']
    perfil_actual['Genero'] = cambios_perfil['Genero']
    perfil_actual['Especificar genero'] = cambios_perfil['Especificar genero']
    perfil_actual['Avatar'] = os.path.basename(cambios_perfil['-BROWSE-'])
    
    return perfil_actual
