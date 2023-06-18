import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad import actualizar_datos as act
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
                        [sg.Text("Haga click en Guardar, entonces se solicitará el nombre con el cual desee guardar el")],
                        [sg.Text("collage, si se guardó correctamente se mostrará un mensaje de éxito.")]
                       ]
        collage=sg.Window("Ayuda",layout_collage)
        while True:
            evento, valores = collage.read()
            if evento == sg.WIN_CLOSED:
                collage.close()
                break

    def ayuda_meme():
        '''Genera la ventana de ayuda_meme con la respectiva informacion que le servirá
        al usuario de la aplicación para hacer uso de la funcionalidad de generar meme'''
        layout_meme=[[sg.Text("-Desde el menú debe seleccionar el boton “Generar Meme”, a continuación se mostrará")],
                     [sg.Text("una pantalla con las imagenes del repositorio configurado.")],
                     [sg.Text(" ")],
                     [sg.Text("-Alli debe seleccionar el template (plantilla) que quiera utilizar. Al hacer click en")],
                     [sg.Text("una imagen, el sistema indicará si se trata de un template o no. Una vez encontrada la")],
                     [sg.Text("plantilla que se quiere utilizar, debe hacer click en “Generar” y se abrirá otra pantalla")],
                     [sg.Text(" ")],
                     [sg.Text("-En esta pantalla, debe seleccionar la fuente deseada para el texto. Y debe completar")],
                     [sg.Text("cada cuadro de texto con el contenido deseado.")],
                     [sg.Text(" ")],
                     [sg.Text("-Luego debe hacer click en “Actualizar” para chequear que el texto se vea de la forma")],
                     [sg.Text("deseada. En caso contrario puede modificar nuevamente las casillas de texto.")],
                     [sg.Text(" ")],
                     [sg.Text("-Haga click en Guardar, se solicitará el nombre con el cual desee guardar el meme. Y por")],
                     [sg.Text("ultimo debe hacer click en “Generar”, si se guardó correctamente el sistema indicará que")],
                     [sg.Text("se creo un nuevo meme con éxito.")]
                     ]
        meme=sg.Window("Ayuda",layout_meme)
        while True:
            evento, valores = meme.read()
            if evento == sg.WIN_CLOSED:
                meme.close()
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
            ventana_de_ayuda.hide()
            ayuda_meme()
            ventana_de_ayuda.un_hide()

def ventana_menu(perfil_actual):
    '''Esta funcion retorna la ventana de menu con sus respectivos botones. '''
    imagen_bytes=act.mostrar_imagen(os.path.join(r.ruta_imagenes_perfil,perfil_actual["Avatar"]))
    columna1=[[sg.Button(image_data=imagen_bytes,
                         key="-VENTANA EDITAR PERFIL-")],
              [sg.Text(perfil_actual["Usuario"],key="-USUARIO-")]
             ]
    columna2=[[sg.Button("Configuracion",key="-VENTANA CONFIGURACION-")]]
    
    columna3=[[sg.Button('?',tooltip="Ayuda",key="-VENTANA AYUDA-")]]

    layout = [[sg.Column(columna1),sg.Column(columna2),sg.Column(columna3)],
              [sg.Text(" "*10),sg.Button("Etiquetar Imagenes",size=(15,1),key="-VENTANA ETIQUETAR-")],
              [sg.Text(" "*10),sg.Button("   Generar meme   ",size=(15,1),key="-VENTANA MEME-")],
              [sg.Text(" "*10),sg.Button("  Generar collage ",size=(15,1),key="-VENTANA COLLAGE-")],
              [sg.Text(" "*10),sg.Button("       Salir      ",size=(15,1),key="-SALIR-")]
             ]
    
    return sg.Window("Menú",layout,margins=(150, 150),metadata={"perfil_actual":perfil_actual})

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
                imagen_bytes=act.mostrar_imagen(os.path.join(r.ruta_imagenes_perfil,menu.metadata["perfil_actual"]["Avatar"]))
                menu["-VENTANA EDITAR PERFIL-"].update(image_data=imagen_bytes)
                menu.un_hide()

if __name__ =="__main__":
    ventana_menu()
                 