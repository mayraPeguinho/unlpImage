import PySimpleGUI as sg
import json
import os
import sys
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import rutas
from pantallas import menu_principal

ruta_archivo = rutas.archivo_perfiles_json
ruta_repositorio_imagenes=rutas.imagenes_perfil

try:
    with open(ruta_archivo,"r") as archivo:
        data = json.load(archivo)
except FileNotFoundError:
    x=1
except PermissionError:
    x=2

def mostrar_perfiles(datos):
    perfiles=[]
    keys=[]
    i=-1
    for elemento in datos:
        i=i+1
        keys.append(i)
        perfiles.append(sg.Button(image_source=os.path.join(ruta_repositorio_imagenes,elemento["-BROWSE-"]),image_size=(64,64),key=i))
    return perfiles


def layout_inicio(datos,no_desplegar=True):
    perfiles=mostrar_perfiles(datos)
    if(perfiles==[]):
         layout=[[sg.Button(button_text= "+")]]
    if(perfiles.__len__()<4):
        layout=[perfiles,[sg.Button(button_text= "+")]]
    if (4<perfiles.__len__()) and no_desplegar:
        layout = [[perfiles[0],perfiles[1],perfiles[2],perfiles[3],sg.Button(button_text= "+")]]
        layout.append([sg.Button(button_text= "Ver más",key="Mostrar")])
    if (4<perfiles.__len__()) and not(no_desplegar):
        layout = [[perfiles,sg.Button(button_text= "+")]]
        layout.append([sg.Button(button_text= "Ver menos",key="Mostrar")])
    return layout

def generar_ventana_de_inicio(datos,desplegar=True):
    layout=layout_inicio(datos,desplegar)
    return sg.Window("UNLPImage",layout,margins=(200, 150),metadata={"perfil_actual":None})

inicio=generar_ventana_de_inicio(data)
keys=[0,1,2,3,4,5,6,7]

while True:
    evento, valores = inicio.read()
    match evento:
        case sg.WIN_CLOSED:
            break
        case "+":
            #Va la pestaña de nuevo perfil
            x=1
        case "Mostrar":
            inicio["Mostrar"].update("Ver menos")
            print("Hola")
    if evento in keys:
        inicio.metadata["perfil_actual"]=data[evento]
        inicio.hide()
        if __name__ =="__main__":
            menu_principal.ventana_menu()
        inicio.un_hide()

      
inicio.close()