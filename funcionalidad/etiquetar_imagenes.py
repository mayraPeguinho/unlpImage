import os
from PIL import Image, ImageTk
from datetime import datetime
import mimetypes
import csv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import registrar_log as log


def imagen_tostring(datos):
    """Devuelve un string con la descripción de la imagen."""

    str = (" | {} | {} MB | {} | \nDescripción: {}".format(datos[4], datos[5], datos[3], datos[1]))

    return str


def crear_csv(ruta_csv):
    """Crea el archivo CSV de imagenes etiquetadas en caso de que este no exista"""

    columnas = ['ruta_imagen', 'descripcion', 'tags', 'resolucion', 'mimetype', 'tamaño', 'ultima_actualizacion', 'ultimo_perfil']
    with open(ruta_csv, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columnas)

def guardar_data(ruta, data, usuario_actual):
    """Guarda los datos de la imagen en el archivo csv"""
    ruta
    with open(ruta, mode='r+', encoding="utf-8") as file:
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
                datos_imagen[7] = usuario_actual 
                #Modifico el csv con los datos modificados de imagen existente
                contenido_csv[posicion] = datos_imagen
                log.registrar_interaccion(datos_imagen[7], "Imagen editada")
            else:
                # Si no se encontró una fila con la ruta dada, agreo una nueva fila (nueva imagen editada)
                fila_nueva = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], usuario_actual)
                #Modifico el csv con los datos agregados de una imagen nueva
                contenido_csv.append(fila_nueva)
                log.registrar_interaccion(usuario_actual, "Imagen agregada")

            with open(ruta, 'w',newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(contenido_csv)

#la siguiente función, no funciona. No se porqué.     

def actualizar_tags(csv_archivo, ruta):
    """Retorna los tags"""

    with open(csv_archivo, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)
        contenido_csv = list(reader)
        tags = []
        #Busco la fila en el csv
        for datos_fila in contenido_csv:
            #si encuentro la fila          
            try: 
                if (ruta == datos_fila[0]):
                    # me guardo los datos de la imagen y dejo de recorrer el csv
                    tags_crudas = datos_fila[2]
                    tags = [elemento.strip().replace("'", "") for elemento in tags_crudas.strip("[]").split(",")]
                    break
            #si no encuentro la fila, quedan los valores por defecto
            except: 
                pass
    return tags

def eliminar_tag(valores):
    """Eliminar una tag traída por parámetro"""
    tags = [tag for tag in tags if tag not in valores]
    
def actualizar_desc(csv_archivo, ruta):
    """Chequeo si la imagen ya fué editada para poder mostras sus tags y descripción correctamente""" 

    with open(csv_archivo, "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)
        contenido_csv = list(reader)
        descripcion = "Sin desripción"
        #Busco la fila en el csv
        for datos_fila in contenido_csv:
            #si encuentro la fila          
            try: 
                if (ruta == datos_fila[0]):
                    # me guardo los datos de la imagen y dejo de recorrer el csv
                    descripcion = datos_fila[1] 
                    break
            #si no encuentro la fila, quedan los valores por defecto
            except: 
                pass
    return descripcion

def traer_data(usuario, values, csv_archivo,  mode):
    """Retorna y actualiza los valores de la imagen que deben mostrarse y/o editarse."""
    # traigo la ruta de la imagen
    ruta_imagen = values['-TREE-'][0].replace("\\", "/")
    # la abro
    imagen = Image.open(ruta_imagen)
    #Extraigo la resolución antes de cambiarla
    resolucion = imagen.size
    #tipo (mimetype)
    #invoco a una función que actualiza los tags trayendolos del csv
    
    if mode == "r":
        descripcion = actualizar_desc(csv_archivo, ruta_imagen)   
        tags = actualizar_tags(csv_archivo, ruta_imagen)
    else:
        if mode =="d":
            descripcion = values['Texto']
            #Guardar entre comillas, procesarlas. 
            tags = values['TagList']
        else:
            #actualizo la descripción
            descripcion = values['Texto'] if values['Texto'] != '' else actualizar_desc(csv_archivo, ruta_imagen) 
            #lista de tags(lo saco de imagen seleccionada)
            tags = values['TagList']
    #tipo (mimetype)
    mimetype = mimetypes.guess_type(ruta_imagen)[0]
    #tamaño (metadata)
    tamaño = os.path.getsize(ruta_imagen)
    #Fecha de ultima actualización (enviar al log)
    timestamp = datetime.timestamp(datetime.now())
    ultima_actualizacion = datetime.fromtimestamp(timestamp)  
    usuario = usuario
    datos = (ruta_imagen, descripcion, tags,(str(resolucion[0]) + 'x' + str(resolucion[1])), 
                    mimetype, (round(tamaño / (1024*1024), 2)), ultima_actualizacion, usuario)
    return datos

def mostrar_imagen(ruta):
    """Procesa la imagen para poder mostrarla en PySimpleGUI"""
    imagen = Image.open(ruta)
    #Modifico el tamaño para mostrarla en la pantalla
    imagen = imagen.resize((350, 300))
    # convertir la imagen a un formato que pueda mostrar PySimpleGUI
    data = ImageTk.PhotoImage(imagen)
    return data
