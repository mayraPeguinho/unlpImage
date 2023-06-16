import PySimpleGUI as sg
import sys
import os
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad.verificar_input import falta_completar_campos
from funcionalidad import crear_collage


def layout(cant_imagenes,descripciones):
    '''genera y devuelve el diseño de la interfaz gráfica para la generación de collages.
       Retorna Una lista que representa el diseño de la interfaz gráfica, que incluye combos para seleccionar las imágenes,
       un campo de entrada para el título,una sección para visualizarlo y botones para actualizar y guardar el collage.
       Recibe cant_imagenes para especificar cuantos combos crear y una lista de descripciones de las 
       imágenes disponibles para seleccionar de los combos.
    '''

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
     Genera la interfaz gráfica para crear un collage.
     Recibe la cantidad de imágenes que tendrá el collage, el número del diseño a usar y el usuario.
     """

     # Obtengo las imágenes etiquetadas
     imagenes_diccionario = crear_collage.obtener_imagenes()

     # En los combos se debe mostrar la descripción de la imagen
     descripciones = list(imagenes_diccionario.keys())

     imagenes_usadas=[]

     window = sg.Window("Generador de Collages", layout(cant_imagenes,descripciones),margins=(60,30),element_justification="center",resizable=True)
     window.finalize()
     
     # creo una imagen base para el collage
     size=400,400
     collage = PIL.Image.new('RGB', size,color='white')
     image = PIL.ImageTk.PhotoImage(collage)
     window["-IMAGEN-"].update(data=image)
    
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
                     nombre = sg.popup_get_text("Ingrese un nombre para el collage")
                     if nombre is not None and crear_collage.es_nombre_valido(nombre) and nombre != '':
                         if not crear_collage.existe_nombre(f"{nombre}.png"):
                             crear_collage.guardar_collage(nombre, collage_actual,imagenes_usadas,usuario,valores["-TÍTULO-"],cant_imagenes)
                             sg.popup("El collage se generó con éxito")
                             break
                         else:
                             sg.popup("Ya existe un archivo con ese nombre. Por favor, ingrese otro nombre")
                     else:
                         sg.popup("Debe ingresar un nombre válido para el collage. Caracteres no permitidos : [<>\}/|;*#$%!¡?¿]")
                 else:
                     sg.popup("Actualice el collage")
             else:
                  sg.popup("Falta completar los campos necesarios")   
        
         else:                
             match diseño:            
                 case 1:
                     if evento=="-IMAGEN-1-":                          
                         collage_actual = crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-1-"])))
                         
                     elif evento=="-IMAGEN-2-":
                         collage_actual= crear_collage.crear_collage_diseño_1(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-2-"])))
                         titulo_insertado=False
                 case 2:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-1-"])))  

                     elif evento=="-IMAGEN-2-":
                         collage_actual = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-2-"])))
                         titulo_insertado=False

                     elif evento=="-IMAGEN-3-":
                         collage_actual = crear_collage.crear_collage_diseño_2(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-3-"])))
                         
                 case 3:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-1-"])))  

                     elif evento=="-IMAGEN-2-":
                         collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-2-"])))

                     elif evento=="-IMAGEN-3-":
                         collage_actual = crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-3-"]),3, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-3-"])))
                         titulo_insertado=False

                     elif evento=="-IMAGEN-4-":
                         collage_actual= crear_collage.crear_collage_diseño_3(imagenes_diccionario.get(valores["-IMAGEN-4-"]),4, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-4-"])))

                 case 4:
                     if evento=="-IMAGEN-1-":                           
                         collage_actual= crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-1-"]),1,collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-1-"])))
                         titulo_insertado=False
                     elif evento=="-IMAGEN-2-":
                         collage_actual = crear_collage.crear_collage_diseño_4(imagenes_diccionario.get(valores["-IMAGEN-2-"]),2, collage)
                         imagenes_usadas.append(os.path.basename(imagenes_diccionario.get(valores["-IMAGEN-2-"])))
                        
         #muestro el collage altualizado
         imagen_actualizada = PIL.ImageTk.PhotoImage(collage_actual)
         window["-IMAGEN-"].update(data=imagen_actualizada)
        
     window.close()


if __name__ == "__main__":
     generar_collage(usuario,cant_imagenes, diseño)


    