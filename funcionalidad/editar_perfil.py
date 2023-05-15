import os

def mostrar_perfil(perfil_actual,window):
    """ Guardo los valores del perfil"""
    genero_opciones=['Masculino','Femenino','Otro']  

    window['Nombre'].update(perfil_actual['Nombre'])
    window['Edad'].update(perfil_actual['Edad'])
    window['Genero'].update(genero_opciones)
    window['Especificar genero'].update(perfil_actual['Especificar genero'])
    window['-BROWSE-'].update(perfil_actual['Avatar'])

    return(window)
    
    
def modificar_perfil(perfil_actual,cambios_perfil):
    """ Le asigno al perfil actual los nuevo valores actualizados"""

    if cambios_perfil['-BROWSE-'] != '':
            perfil_actual['Avatar'] = os.path.basename(cambios_perfil['-BROWSE-'])
    elif perfil_actual['Avatar'] == '':
            perfil_actual['Avatar'] = cambios_perfil['-BROWSE-']
            
    if perfil_actual['Genero'] == '':
            perfil_actual['Genero'] = cambios_perfil['Genero']

    perfil_actual['Nombre'] = cambios_perfil['Nombre']
    perfil_actual['Edad'] = cambios_perfil['Edad']
    perfil_actual['Especificar genero'] = cambios_perfil['Especificar genero']
    
    return perfil_actual
