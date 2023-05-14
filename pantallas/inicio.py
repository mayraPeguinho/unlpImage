import PySimpleGUI as sg
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import nuevo_perfil
from pantallas import menu_principal

def mostrar_perfiles(datos):
    '''Esta funcion carga los diferentes perfiles creados previamente
       en diferentes botones que seran mostrados luego en la ventana de inicio.'''
    ruta_imagenes_perfil=os.path.join(os.getcwd(),'imagenes','imagenes_perfil')
    perfiles=[]
    for numero,elemento in enumerate(datos): 
        perfiles.append(sg.Column([[sg.Button(image_source=os.path.join(ruta_imagenes_perfil,elemento["Avatar"]),
                                              image_size=(80,80),
                                              image_subsample=3,
                                              key=numero)],
                                   [sg.Text(elemento["Usuario"],justification="center")]
                                  ])
                        )

    #perfiles=list(map(lambda numero,elemento: sg.Column([[sg.Button(image_source=os.path.join(ruta_repositorio_imagenes,elemento["Avatar"]),image_size=(80,80),image_subsample=3,key=numero)],[sg.Text(elemento["Usuario"])]]), enumerate(datos())))
    return perfiles

def layout_inicio(datos,no_desplegar=True):
    '''Esta funcion crea el layout de la ventana de inicio
       dependiendo de cuantos perfiles cargados previamente haya.'''
    perfiles=mostrar_perfiles(datos)
    if(perfiles==[]):
         layout=[[sg.Button("+",key="-AGREGAR PERFIL-")]]
    elif(perfiles.__len__()<=4):
        perfiles.append(sg.Button("+",key="-AGREGAR PERFIL-"))
        layout=[[perfiles]]
    elif (4<perfiles.__len__()) and no_desplegar:
        layout = [[perfiles[0],perfiles[1],perfiles[2],perfiles[3],sg.Button("+",key="-AGREGAR PERFIL-")]]
        layout.append([sg.Button("Ver más",key="-VER MAS-")])
    elif (4<perfiles.__len__()) and not(no_desplegar):
        perfiles.append(sg.Button("+",key="-AGREGAR PERFIL-"))
        layout = [[perfiles]]
        layout.append([sg.Button("Ver menos",key="-VER MENOS-")])
    return layout

def mostrar_mas_perfiles(datos):
    '''Esta funcion crea la ventana en donde se muestran los perfiles restantes'''
    layout=layout_inicio(datos,False)
    return sg.Window("UNLPImage",layout,margins=(200, 150))

def generar_ventana_de_inicio(datos):
    '''Esta funcion muestra hasta un maximo de cuatro perfiles,
    que pasada esa cantidad estara hablitado el boton "Ver mas"
    para ver los restantes perfiles creados'''
    layout=layout_inicio(datos,True)
    return sg.Window("UNLPImage",layout,margins=(200, 150))

def manejar_eventos_mas_perfiles(keys,datos):
    '''Maneja los eventos de la ventana que muestra todos los perfiles'''
    mas_perfiles=mostrar_mas_perfiles(datos)
    while True:
        evento, valores = mas_perfiles.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-VER MENOS-":
                mas_perfiles.close()
                break
            case "-AGREGAR PERFIL-":
                mas_perfiles.hide()
                nuevo_perfil.ventana_nuevo_perfil()
        if evento in keys:
            menu=menu_principal.ventana_menu(datos[evento])
            mas_perfiles.hide()
            menu_principal.eventos_menu_principal(menu)
            mas_perfiles.un_hide()

if __name__ =="__main__":
     generar_ventana_de_inicio([])