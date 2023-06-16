import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pantallas import seleccion_de_collage
from pantallas import etiquetar_imagenes
from pantallas import configuracion
from pantallas import editar_perfil
from pantallas import inicio
from pantallas import seleccion_template as st      
import rutas as r

def generar_ventana_de_ayuda():
    '''Esta funcion define la ventana de ayuda
       donde se explica la funcionalidad de la aplicacion al usuario. '''
    layout = [[sg.Text("UNLPImage es una aplicación de escritorio, que permite realizar memes")],
              [sg.Text("o collages con imagenes almacenadas en el dispositivo.")],
              [sg.Text(" "*25), sg.Button("¿Cómo armar un collage?",key="-COLLAGE-")],
              [sg.Text(" "*25), sg.Button(" ¿Cómo crear un meme? ",key="-MEME-")],
             ]
    layout_meme=None
    def ayuda_collage():
        '''Genera la ventana de ayuda_collage con la respectiva informacion que le servirá
        al usuario de la aplicación para hacer uso de la funcionalidad de generar collage'''
        layout_collage=[[sg.Text("-Desde el menú debe seleccionar el boton “Generar Collage”, a continuación se")],
                        [sg.Text("mostrará una pantalla con los diseños posibles. Seleccione uno haciendo click.")],
                        [sg.Text(" ")],
                        [sg.Text("-Se mostrará la pantalla de creación, donde se podrán seleccionar cada una de")],
                        [sg.Text("las imágenes a utilizar y el título que se desee.")],
                        [sg.Text(" ")],
                        [sg.Text("-Deberá hacer click  en “Actualizar” para insertar el título en el collage.")],
                        [sg.Text("Haga click en Guardar y se solicitará el nombre con el cuak desee guardar el,")],
                        [sg.Text("si se guardó correctamente se mostrará un mensaje de éxito.")]
                       ]
        collage=sg.Window("Ayuda",layout_collage)
        while True:
            evento, valores = collage.read()
            if evento == sg.WIN_CLOSED:
                collage.close()
                break

    ventana_de_ayuda=sg.Window("Ayuda",layout)
    while True:
        evento, valores = ventana_de_ayuda.read()
        if evento == sg.WIN_CLOSED:
            ventana_de_ayuda.close()
            break
        if evento == "-COLLAGE-":
            ventana_de_ayuda.hide()
            ayuda_collage()
            ventana_de_ayuda.un_hide()
        if evento == "-MEME-":
            pass

def ventana_menu(perfil_actual):
    '''Esta funcion define la ventana de menu con sus respectivos botones. '''
    columna1=[[sg.Button(image_filename=os.path.join(r.ruta_imagenes_perfil,perfil_actual["Avatar"]),
                         image_size=(80,80),
                         image_subsample=3,
                         key="-VENTANA EDITAR PERFIL-")],
              [sg.Text(perfil_actual["Usuario"],key="-USUARIO-")]
             ]
    columna2=[[sg.Button("Configuracion",key="-VENTANA CONFIGURACION-")]]
    
    columna3=[[sg.Button('?',tooltip="Ayuda",key="-VENTANA AYUDA-")]]

    layout = [[sg.Column(columna1),sg.Column(columna2),sg.Column(columna3)],
              [sg.Button("Etiquetar Imagenes",key="-VENTANA ETIQUETAR-")],
              [sg.Button("Generar meme",key="-VENTANA MEME-")],
              [sg.Button("Generar collage",key="-VENTANA COLLAGE-")],
              [sg.Button("Salir",key="-SALIR-")]
             ]
    
    return sg.Window("UNLPImage",layout,margins=(150, 150),metadata={"perfil_actual":perfil_actual})

def eventos_menu_principal(menu):
    '''Maneja los eventos de la ventana menu prinicipal'''
    while True:
        evento, valores = menu.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-SALIR-":
                menu.close()
                inicio.eventos_inicio()
                break
            case "-VENTANA AYUDA-":
                generar_ventana_de_ayuda()
            case "-VENTANA MEME-":
                menu.hide()
                st.pantalla_seleccionartemplate(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA COLLAGE-":
                menu.hide()
                #pasarle la info del perfil actual
                seleccion_de_collage.eventos_seleccion_collage(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA ETIQUETAR-":
                menu.hide()
                etiquetar_imagenes.pantalla_etiquetar(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA CONFIGURACION-":
                menu.hide()
                configuracion.pantalla_configuracion(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA EDITAR PERFIL-":
                menu.hide()
                menu.metadata["perfil_actual"]=editar_perfil.ventana_editar_perfil(menu.metadata["perfil_actual"])
                menu["-VENTANA EDITAR PERFIL-"].update(
                    image_filename=os.path.join(r.ruta_imagenes_perfil,menu.metadata["perfil_actual"]["Avatar"]),
                    image_size=(80,80),
                    image_subsample=3
                    )
                menu.un_hide()

if __name__ =="__main__":
    ventana_menu()
                 