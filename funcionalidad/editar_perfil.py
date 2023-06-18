import os

def mostrar_perfil(perfil_actual,window):
    """ MUestro los valores del perfil"""

    genero_opciones=['Masculino','Femenino','Otro']
    genero_valor=''

    if perfil_actual['Genero'] == 'Masculino' or perfil_actual['Genero'] == 'Femenino':
        genero_indice=genero_opciones.index(perfil_actual['Genero'])
    else:
        genero_valor = perfil_actual['Genero']
        genero_indice=genero_opciones.index('Otro')

    window['Nombre'].update(perfil_actual['Nombre'])
    window['Edad'].update(perfil_actual['Edad'])
    window['Genero'].update(genero_opciones, set_to_index=genero_indice)
    window['Especificar genero'].update(genero_valor)
    window['-BROWSE-'].update(perfil_actual['Avatar'])
    
    
    return(window)
    
    
def modificar_perfil(perfil_actual,cambios_perfil):
    """ Le asigno al perfil actual los nuevo valores actualizados"""
 
    if os.path.basename(cambios_perfil['-BROWSE-'])!= 'avatar.png':
        perfil_actual['Avatar'] = os.path.basename(cambios_perfil['-BROWSE-'])
    else:
        perfil_actual['Avatar'] = os.path.basename(perfil_actual['Avatar'])

    if cambios_perfil['Genero'][0] != perfil_actual['Genero']:
        if cambios_perfil['Genero'][0] == 'Masculino' or cambios_perfil['Genero'][0] == 'Femenino':
            perfil_actual['Genero']=cambios_perfil['Genero'][0]
        else:
            perfil_actual['Genero'] = cambios_perfil['Especificar genero']

    perfil_actual['Nombre'] = cambios_perfil['Nombre']
    perfil_actual['Edad'] = cambios_perfil['Edad']
    
    return perfil_actual

def llenar_genero(values,avatar_actual):
    """Asigno valores que llevan por si no son modificados"""
    if os.path.basename(values['-BROWSE-']) == '':
        values['-BROWSE-'] = avatar_actual
    if values['Genero'][0] != 'Otro':
        values['Especificar genero'] = '-'
