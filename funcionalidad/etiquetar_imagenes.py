import os
from PIL import Image, ImageTk
from datetime import datetime
import PySimpleGUI as sg
import mimetypes
import csv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import registrar_log as log


def imagen_tostring(datos):
    """Devuelve un string con la descripción de la imagen."""

    str = (" | {} | {} MB | {} | \nDescripción: {}".format(datos[4], datos[5], datos[3], datos[1]))

    return str

def add_files_in_folder(parent, dirname):

    """Crea el árbol de archivos."""
    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    treedata = sg.TreeData()
    
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname, f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
            add_files_in_folder(fullname, fullname)
        else:
            treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)
    return treedata

def crear_csv(ruta_csv):
    """Crea el archivo CSV de imagenes etiquetadas en caso de que este no exista"""

    columnas = ['ruta_imagen', 'descripcion', 'tags', 'resolucion', 'mimetype', 'tamaño', 'ultima_actualizacion', 'ultimo_perfil']
    with open(ruta_csv, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columnas)

def guardar_data(ruta, data, usuario_actual):
    """Guarda los datos de la imagen en el archivo csv"""
    try:    
        nombre = os.path.basename(data[0])
        with open(ruta, mode='r+', encoding="utf-8") as file:
            reader = csv.reader(file)
            contenido_csv = list(reader)
        encontre = False
        #Busco la fila en el csv
        for pos, datos_fila in enumerate(contenido_csv):
            if any(nombre in campo for campo in datos_fila):
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
        try:
            with open(ruta, 'w',newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(contenido_csv)
        except(PermissionError):
            sg.popup_error("No se cuentan con los permisos para acceder al archivo 'imagenes_etiquetadas.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.")
            sys.exit()
    except(PermissionError):
        sg.popup_error("No se cuentan con los permisos para acceder al archivo 'imagenes_etiquetadas.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.")
        sys.exit()
    except (FileNotFoundError):
        sg.popup_error("No se ha encontrado el archivo 'imagenes_etiquetadas', se cerrará el programa.")
        sys.exit()

def actualizar_tags(csv_archivo, ruta):
    """Retorna los tags"""
    try:
        with open(csv_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            contenido_csv = list(reader)
        tags = []
        #Busco la fila en el csv
        for datos_fila in contenido_csv:
            #si encuentro la fila          
            try: 
                ruta_corregida = os.path.basename(ruta)
                ruta_corregida_enarbol = os.path.basename(datos_fila[0])
                if (ruta_corregida == ruta_corregida_enarbol):
                    # me guardo los datos de la imagen y dejo de recorrer el csv
                    tags = datos_fila[2].split(', ')                    
                    break
            #si no encuentro la fila, quedan los valores por defecto
            except: 
                pass
        return tags
    except(PermissionError):
        sg.popup_error("No se cuentan con los permisos para acceder al archivo 'imagenes_etiquetadas.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.")
        sys.exit()
    except(FileNotFoundError):
        sg.popup_error("No se ha encontrado el archivo 'imagenes_etiquetadas', se cerrará el programa.")
        sys.exit()


    
def actualizar_desc(csv_archivo, ruta):
    """Chequeo si la imagen ya fué editada para poder mostras sus tags y descripción correctamente""" 
    try:
        with open(csv_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            contenido_csv = list(reader)
            descripcion = "Sin desripción"
            
            #Busco la fila en el csv
            for datos_fila in contenido_csv:
                #si encuentro la fila          
                ruta_corregida = os.path.basename(ruta)
                ruta_corregida_enarbol = os.path.basename(datos_fila[0])
                try: 
                    if (ruta_corregida == ruta_corregida_enarbol):
                        # me guardo los datos de la imagen y dejo de recorrer el csv
                        descripcion = datos_fila[1] 
                        break
                #si no encuentro la fila, quedan los valores por defecto
                except: 
                    pass
        return descripcion
    except(PermissionError):
        sg.popup_error("No se cuentan con los permisos para acceder al archivo 'imagenes_etiquetadas.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.")
        sys.exit()
    except (FileNotFoundError):
        sg.popup_error("No se ha encontrado el archivo 'imagenes_etiquetadas', se cerrará el programa.")
        sys.exit()


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
            tags_crudas = values['TagList']
            tags = ', '.join(tags_crudas)
        else:
            #actualizo la descripción
            descripcion = values['Texto'] if values['Texto'] != '' else actualizar_desc(csv_archivo, ruta_imagen) 
            #lista de tags(lo saco de imagen seleccionada)
            tags_crudas = values['TagList']
            tags = ', '.join(tags_crudas)
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
