import os

def mostrar_perfil(perfil_actual,window):
    """ MUestro los valores del perfil"""
    ###
    genero_opciones=['Masculino','Femenino','Otro']  
    genero_valor = perfil_actual['Genero']
    genero_indice = genero_opciones.index(genero_valor)

    window['Nombre'].update(perfil_actual['Nombre'])
    window['Edad'].update(perfil_actual['Edad'])
    window['Genero'].update(genero_opciones, set_to_index=genero_indice)
    window['Especificar genero'].update(perfil_actual['Especificar genero'])
    window['-BROWSE-'].update(perfil_actual['Avatar'])
    
    
    return(window)
    
    
def modificar_perfil(perfil_actual,cambios_perfil):
    """ Le asigno al perfil actual los nuevo valores actualizados"""
 
    if os.path.basename(cambios_perfil['-BROWSE-'])!= 'avatar.png':
        perfil_actual['Avatar'] = os.path.basename(cambios_perfil['-BROWSE-'])
    else:
        perfil_actual['Avatar'] = os.path.basename(perfil_actual['Avatar'])

    if cambios_perfil['Genero'] != []:
        perfil_actual['Genero'] = cambios_perfil['Genero'][0]
    

    perfil_actual['Nombre'] = cambios_perfil['Nombre']
    perfil_actual['Edad'] = cambios_perfil['Edad']
    perfil_actual['Especificar genero'] = cambios_perfil['Especificar genero']
    
    return perfil_actual
