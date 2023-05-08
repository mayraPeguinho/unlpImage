import PySimpleGUI as sg
import json
import os
import sys
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import rutas

def mostrar_perfiles(datos):
    '''Esta funcion carga los diferentes perfiles creados previamente
       en diferentes botones que seran mostrados luego en la ventana de inicio.'''
    ruta_repositorio_imagenes=rutas.imagenes_perfil
    perfiles=[]
    i=0
    for elemento in datos:
        perfiles.append(sg.Button(image_source=os.path.join(ruta_repositorio_imagenes,elemento["-BROWSE-"]),image_size=(80,80),image_subsample=3,key=i))
        i=i+1
    return perfiles


def layout_inicio(datos,no_desplegar=True):
    '''Esta funcion crea el layout de la ventana de inicio
       dependiendo de cuantos perfiles cargados previamente haya.'''
    perfiles=mostrar_perfiles(datos)
    if(perfiles==[]):
         layout=[[sg.Button(button_text= "+")]]
    if(perfiles.__len__()<=4):
        botones=[]
        for elemento in perfiles:
            botones.append(elemento)
        botones.append(sg.Button(button_text= "+"))
        layout=[[botones]]
    if (4<perfiles.__len__()) and no_desplegar:
        layout = [[perfiles[0],perfiles[1],perfiles[2],perfiles[3],sg.Button(button_text= "+")]]
        layout.append([sg.Button(button_text= "Ver más")])
    if (4<perfiles.__len__()) and not(no_desplegar):
        layout = [[perfiles,sg.Button(button_text= "+")]]
        layout.append([sg.Button(button_text= "Ver menos")])
    return layout

def mostrar_mas_perfiles(datos):
    '''Esta funcion crea la ventana en donde se muestran los perfiles restantes'''
    layout=layout_inicio(datos,False)
    return sg.Window("UNLPImage",layout,margins=(200, 150),metadata={"perfil_actual":None})

def generar_ventana_de_inicio(datos):
    '''Esta funcion muestra hasta un maximo de cuatro perfiles,
    que pasada esa cantidad estara hablitado el boton "Ver mas"
    para ver los restantes perfiles creados'''
    layout=layout_inicio(datos,True)
    return sg.Window("UNLPImage",layout,margins=(200, 150),metadata={"perfil_actual":None})

if __name__ =="__main__":
     generar_ventana_de_inicio({})