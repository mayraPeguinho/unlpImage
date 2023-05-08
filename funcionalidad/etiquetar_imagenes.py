import os
from PIL import Image, ImageTk
from datetime import datetime
import mimetypes
import csv


def imagen_tostring(datos):
    """Devuelve un string con la descripción de la imagen."""

    str = (" | {} | {} MB | {} | \nTags: {} \nDescripción: {}".format(datos[4], datos[5], datos[3], datos[2], datos[1]))

    return str




def guardar_data(ruta, data):
    """Guarda los datos de la imagen en el archivo csv"""
    ruta
    with open(ruta, mode='r+') as file:
            # Creo objeto lector
            reader = csv.reader(file)
            contenido_csv = list(reader)

            encontre = False
            #Busco la fila en el csv
            for pos, datos_fila in enumerate(contenido_csv):
                if data[0] in datos_fila:
                    # me guardo la posicion en el archivo
                    posicion = pos
                    datos_previos_modificar = datos_fila
                    encontre = True
                    break
            if encontre:
                datos_imagen = datos_previos_modificar[:]
                datos_imagen[1] = data[1]
                datos_imagen[2] = data[2]
                datos_imagen[6] = data[6]
                datos_imagen[7] = "null" #De momento es null porque falta implementar funcionalidad
                                        #de agregar ultimo perfil que actualizó
                #Modifico el csv con los datos modificados de imagen existente
                contenido_csv[posicion] = datos_imagen
            else:
                # Si no se encontró una fila con la ruta dada, agreo una nueva fila (nueva imagen editada)
                fila_nueva = (data[0], data[1], data[2],data[3], data[4], data[5], data[6], "null")
                #Modifico el csv con los datos agregados de una imagen nueva
                contenido_csv.append(fila_nueva)

            with open(ruta, 'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(contenido_csv)
    


def traer_data(values):
    """Retorna y actualiza los valores de la imagen que deben mostrarse y/o editarse."""
    # traigo la ruta de la imagen
    ruta_imagen = values['-TREE-'][0]
    # la abro
    imagen = Image.open(ruta_imagen)
    #Extraigo la resolución antes de cambiarla
    resolucion = imagen.size
    descripcion = values['Texto']
    #lista de tags(lo saco de imagen_seleccionada)
    tags = values['Tag']
    #tipo (mimetype)
    mimetype = mimetypes.guess_type(ruta_imagen)[0]
    #tamaño (metadata)
    tamaño = os.path.getsize(ruta_imagen)
    #Fecha de ultima actualización (enviar al log)
    timestamp = datetime.timestamp(datetime.now())
    ultima_actualizacion = datetime.fromtimestamp(timestamp)  
    #----------------------------------------------------------------
    #ultimo perfil que actualizó ---(/!\ ver con Fran como implementar esta funcionalidad)---
    #----------------------------------------------------------------
    datos = (ruta_imagen, descripcion, tags,(str(resolucion[0]) + 'x' + str(resolucion[1])), 
                    mimetype, (round(tamaño / (1024*1024), 2)), ultima_actualizacion, "null")
    return datos

def mostrar_imagen(ruta):
    imagen = Image.open(ruta)
    #Modifico el tamaño para mostrarla en la pantalla
    imagen = imagen.resize((350, 300))
    # convertir la imagen a un formato que pueda mostrar PySimpleGUI
    data = ImageTk.PhotoImage(imagen)
    return data