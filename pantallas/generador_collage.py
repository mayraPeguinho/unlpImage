import PySimpleGUI as sg
from PIL import Image, ImageTk
import sys
import os
import csv
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import archivo_imagenes_etiquetadas_csv as ruta_archivo
from funcionalidad.verificar_input import falta_completar_campos
from rutas import ruta_diseños_collages
from funcionalidad import crear_collage

def obtener_imagenes():
    imagenes = {}

    with open(ruta_archivo, 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        next(reader)  
        for row in reader:
            descripcion = row[1]
            nombre_imagen = row[0]
            imagenes[descripcion] = nombre_imagen

    return imagenes


def layout(cant_imagenes,descripciones):

    

    column1 = [
        [sg.Text("Seleccionar imagenes")],
    ]
    column1.extend([[sg.Combo(descripciones, key=f"-IMAGEN-{i+1}-",enable_events=True)] for i in range(cant_imagenes)])

    column1.append([sg.Text("Título")])
    column1.append([sg.Input(key="-TÍTULO-",size=(35))])
    column1.append([sg.Button("Actualizar", key="-ACTUALIZAR-")])

    column2 = [
         [sg.Image(key="-IMAGEN-", size=(400, 400))],
         [sg.Column(
         [[sg.Button("Guardar", key="-GUARDAR-")]],
                     expand_x=True,
                     element_justification="right"
                   )
         ],
    ]

    return [
        [   [sg.Text("Generar Collage", font=("Helvetica", 20), justification="left"),
             sg.Column( [[sg.Button("Volver", key="-VOLVER-")]],
                          expand_x=True,
                          element_justification="right"
                      )
           ],
        
            sg.Column(column1,vertical_alignment="center"),
            sg.Column(column2,vertical_alignment="center"),
        ]
    ]


def generar_collage(diseño,cant_imagenes):
     
     #obtengo las imagenes etiquetadas
     imagenes_diccionario = obtener_imagenes()
     #en los combos se debe mostrar la descripcion de la imagen
     descripciones = list(imagenes_diccionario.keys())

     window = sg.Window("Generador de Collages", layout(cant_imagenes,descripciones),margins=(60,30),element_justification="center",resizable=True)
     window.finalize()
     
     # creo una imagen base para el collage
     size=400,400
     imagen_base = PIL.Image.new('RGB', size)
     image = ImageTk.PhotoImage(imagen_base)
     window["-IMAGEN-"].update(data=image)

     collage=imagen_base


     while True:
         evento, valores = window.read()
         if evento == "-VOLVER-":
             window.close()
             break
         elif evento == sg.WIN_CLOSED:
             sys.exit()
         
         elif evento== "-ACTUALIZAR-":
              pass  
         elif evento == "-GUARDAR-":
             if not falta_completar_campos(valores):
                 #Guardo el collage
                 #crear_collage.guardar_collage(valores["-TÍTULO-"],collage)
                 sg.popup("El collage se generó con éxito")
                 break
             else:
                  sg.popup("Falta completar los campos necesarios")   
         else:                
             match diseño:            
                 case "collage_1.png":
                     if evento=="-IMAGEN-1-":                          
                         collage = crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage = crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         
                 case "collage_2.png":
                     print('case 2')
                     if evento=="-IMAGEN-1-":                           
                         collage= crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                     
                     elif evento=="-IMAGEN-3-":
                         collage = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                         
                 case "collage_3.png":
                     if evento=="-IMAGEN-1-":                           
                         collage= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                     
                     elif evento=="-IMAGEN-3-":
                         collage = crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                     
                     elif evento=="-IMAGEN-4-":
                         collage= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-4-"]),4, collage)
                         

                 case "collage_4.png":
                     if evento==f"-IMAGEN-1-":                           
                         collage= crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage = crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         
                     
             #muestro el collage altualizado
             imagen_actualizada = ImageTk.PhotoImage(collage)
             window["-IMAGEN-"].update(data=imagen_actualizada)
        
     window.close()


if __name__ =="__main__":
     #diseño seleccionado
     diseño = 'collage_1.png'
     #cantidad de imagenes que tendrá el collage
     cant_imagenes = 2
     generar_collage(diseño, cant_imagenes)

    