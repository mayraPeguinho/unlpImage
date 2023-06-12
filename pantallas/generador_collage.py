import PySimpleGUI as sg
import sys
import os
import csv
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import ruta_directorio_collages
from funcionalidad.verificar_input import falta_completar_campos
from funcionalidad import crear_collage


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


def generar_collage(usuario,cant_imagenes,diseño):
     
     """
     Genera la interfaz gráfica para crear un collage y permitiendo al usuario seleccionar las imágenes.
     Recibe la cantidad de imágenes que tendrá el collage, el numero del diseño a usar y el usuario.
     """

     # Obtengo las imágenes etiquetadas
     imagenes_diccionario = crear_collage.obtener_imagenes()

     # En los combos se debe mostrar la descripción de la imagen
     descripciones = list(imagenes_diccionario.keys())

     #obtengo el nombre de la imagen a partir de la ruta para luego guardarla en el log.
     nombres_imagenes = [os.path.basename(ruta_imagen) for ruta_imagen in list(imagenes_diccionario.values())]
    
     window = sg.Window("Generador de Collages", layout(cant_imagenes,descripciones),margins=(60,30),element_justification="center",resizable=True)
     window.finalize()
     
     # creo una imagen base para el collage
     size=400,400
     collage = PIL.Image.new('RGB', size,color='white')
     image = PIL.ImageTk.PhotoImage(collage)
     window["-IMAGEN-"].update(data=image)
     
  # Ruta de guardado del collage en formato PNG





     collage_actual = collage.copy()
     titulo_insertado = False

     while True:
         evento, valores = window.read()     
         if evento == "-VOLVER-":
             window.close()
             break
         elif evento == sg.WIN_CLOSED:
             sys.exit()

         elif evento == "-ACTUALIZAR-":    
             collage_actual= crear_collage.insertar_titulo(valores["-TÍTULO-"],collage)
             if valores["-TÍTULO-"] != '':
                 titulo_insertado=True
             else:
                 sg.popup("Debe ingresar un título")
         elif evento == "-GUARDAR-":
             if not falta_completar_campos(valores):
                 if titulo_insertado:
                     #obtengo la lista de nombres de los collages creados
                     nombres = os.listdir(ruta_directorio_collages)            
                     nombre = sg.popup_get_text("Ingrese un nombre para el collage")
                     if nombre is not None and crear_collage.es_nombre_valido(nombre) and nombre != '':
                         if not crear_collage.verificar_nombre(nombres, f"{nombre}.png"):
                             crear_collage.guardar_collage(nombre, collage_actual,nombres_imagenes,usuario,valores["-TÍTULO-"])
                             sg.popup("El collage se generó con éxito")
                             break
                         else:
                             sg.popup("Ya existe un archivo con ese nombre. Por favor, ingrese otro nombre")
                     else:
                         sg.popup("Debe ingresar un nombre válido para el collage. Caracteres no permitidos : <>:/\|;*#$%!¡?¿")
                 else:
                     sg.popup("Actualice el collage")
             else:
                  sg.popup("Falta completar los campos necesarios")   
        
         else:                
             match diseño:            
                 case 1:
                     if evento=="-IMAGEN-1-":                          
                         collage_actual = crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage_actual= crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         
                 case 2:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage_actual = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                     
                     elif evento=="-IMAGEN-3-":
                         collage_actual = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                         
                 case 3:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                        collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                     
                     elif evento=="-IMAGEN-3-":
                         collage_actual = crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                     
                     elif evento=="-IMAGEN-4-":
                         collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-4-"]),4, collage)
                         

                 case 4:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                             
                     elif evento=="-IMAGEN-2-":
                         collage_actual = crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         
                     
         #muestro el collage altualizado
         imagen_actualizada = PIL.ImageTk.PhotoImage(collage_actual)
         window["-IMAGEN-"].update(data=imagen_actualizada)
        
     window.close()


    