import sys
import os
import PySimpleGUI as sg
import PIL

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import etiquetar_imagenes as ei
from funcionalidad import configuracion as cg
from rutas import archivo_imagenes_etiquetadas_csv as ruta_csv

def pantalla_etiquetar(usuario):
    '''Genera la panatalla de etiquetar, tanto su layout como su manejador de eventos,
    recibiendo como parametro el usuario actual para poder identificar quien realiza
    cambios cuando se etiquetan imagenes
    '''
    starting_path = cg.obtener_directorio('repositorio_imagenes')
    
    #En caso de que el archivo csv de etiquetado de imágenes no exista, lo creo
    if not os.path.isfile(ruta_csv):
        try:
            ei.crear_csv(ruta_csv)
        except PermissionError:
           sg.popup_error("¡No tienes permisos para acceder al archivo de configuración! La aplicación se cerrará.") 
           window.close()
           sys.exit()  
    #Creo el árbol de archivos
    treedata = ei.add_files_in_folder('', starting_path)
    tags = []
    columna_izquierda = [[sg.Text('Repositorio de imagenes')],
            [sg.Tree(data=treedata,
                    headings=['Tamaño', ],
                    auto_size_columns=True,
                    select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                    num_rows=20,
                    col0_width=40,
                    key='-TREE-',
                    show_expanded=False,
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    )],
            [sg.Text('Tag:')],
            [sg.InputText(key='Tag'), sg.Button('Agregar')],
            [sg.Text('Texto descriptivo:')],
            [sg.InputText(key='Texto'), sg.Button('Modificar')],
            [sg.Button('Guardar'), sg.Button('Volver')]]

    columna_derecha = [[sg.Text('La imagen que elegiste:')],
                [sg.Text(size=(40,1), key='-TOUT-')],
                [sg.Image(key='-IMAGE-', size= (15, 20))],
                [sg.Text('Tags:')],
                [sg.Listbox(values= tags, size=(20, 6), key='TagList'), sg.Button('Eliminar')],
                [sg.Text('Descripción: ', key='-DESCRIPCION-')]]
                

    layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]


    #agregar en window el manejo de usuarios entre ventanas. 
    window = sg.Window('Etiquetar Imagenes', layout, resizable=False, finalize=True)


    while True:     # Loop de eventos
        event, values = window.read()    
        if event == 'Volver':
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            sys.exit()           
        else:
            if event == '-TREE-':     
                #Chequear que se pueda abrir y tratar la imagen
                try:
                    imagen_data = ei.traer_data(usuario, values,ruta_csv, "r")
                    ruta_imagen = imagen_data[0]
                    #Muestro la imagen
                    datavisual_imagen = ei.mostrar_imagen(ruta_imagen)
                    tags = imagen_data[2]
                    window["-IMAGE-"].update(data=datavisual_imagen)
                    window["-DESCRIPCION-"].update(ei.imagen_tostring(imagen_data))  
                    window['TagList'].update(values=tags)
                    window['Texto'].update(imagen_data[1])
                except PIL.UnidentifiedImageError:
                    sg.popup_error("¡No es una imagen!")
                except IsADirectoryError:
                    pass
                except PermissionError:
                    sg.popup_error("¡No tienes permisos para acceder a esa carpeta o archivo!")
            if event == 'Agregar':
                tag = values['Tag']
                if tag not in tags:
                    tags.append(tag)
                window['TagList'].update(values=tags)
                values['TagList'] = tags
            if event == 'Eliminar':
                try: 
                    tags_seleccionadas = values['TagList'][0] 
                    tags = [tag for tag in tags if tag not in tags_seleccionadas]
                    window['TagList'].update(values=tags)
                    values['TagList'] = tags  
                except IndexError: 
                    sg.PopupError("No hay tag a eliminar")
            if event == 'Modificar':
                try:
                    imagen_data = ei.traer_data(usuario, values, ruta_csv, "d")
                    window["-DESCRIPCION-"].update(ei.imagen_tostring(imagen_data))  
                    sg.popup("La descripción surtirá efecto al hacer click en guardar")
                except:
                    sg.popup_error("¡Debes seleccionar una imágen válida!")
            if event == 'Guardar':
                try:
                    window['TagList'].update(values=tags)
                    values['TagList'] = tags
                    imagen_data = ei.traer_data(usuario, values, ruta_csv, "w")
                    ei.guardar_data(ruta_csv, imagen_data, usuario)
                    window["-DESCRIPCION-"].update(ei.imagen_tostring(imagen_data))
                    sg.popup("¡Imagen etiquetada con éxito!")             
                except PermissionError:
                    sg.popup_error("¡No tienes permisos para acceder esta imágen o carpeta! Debes seleccionar una imágen válida.") 
                except:
                    sg.popup_error("¡Debes seleccionar una imágen válida!")    

    window.close()

if __name__ =="__main__":
    pantalla_etiquetar("null")
