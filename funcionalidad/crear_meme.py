import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw
import PIL.ImageFont
import os
from funcionalidad import registrar_log as log
from rutas import ruta_directorio_fuentes
from funcionalidad import configuracion
import PySimpleGUI as sg
import sys

fuente_default = os.path.join(ruta_directorio_fuentes, 'Lato-BoldItalic.ttf')

def obterer_coordenadas(meme_json, pos):
    '''Esta función obtiene las coordenadas de los textos que se mostraran
    en el meme, estas estan cargados en el archivo json de templates'''
    top_left_x = meme_json[0]['text_boxes'][pos]['top_left_x']
    top_left_y = meme_json[0]['text_boxes'][pos]['top_left_y']
    bottom_right_x = meme_json[0]['text_boxes'][pos]['bottom_right_x']
    bottom_right_y = meme_json[0]['text_boxes'][pos]['bottom_right_y']

    return top_left_x, top_left_y, bottom_right_x, bottom_right_y

def entra(contenedor,contenido):
    """Calcula si el texto entra en la caja"""
    return contenido[0] <= contenedor[0] and contenido[0] <= contenedor[0]

def tam_box(x1,y1,x2,y2):
    """Calcula el tamaño de la box"""
    return (x2 - x1, y2 - y1)

def calcular_tam_fuente(draw, texto, path_fuente, box):
    """Va achicando el tamaño de la fuente hasta encontrar el ideal para el meme"""
    tam_contenedor = tam_box(*box)
    for tam in range(200, 20, -5):
        fuente = PIL.ImageFont.truetype(path_fuente, tam)
        box_texto = draw.textbbox((0, 0), texto, font = fuente)
        tam_box_texto = tam_box(*box_texto)
        if entra(tam_contenedor,tam_box_texto):
            return fuente
        
    return fuente

def actualizar_datos(meme_imagen,meme_json,values):
    """Se actualiza lo escrito en el meme"""

    copia = meme_imagen.copy()
    draw = PIL.ImageDraw.Draw(copia)
    color = (0,0,0)
    if (values['-FUENTE-'] == ''):
        values['-FUENTE-'] = fuente_default
    
    if (values['-TEXTO_1-'] != ''):
        coordenadas = obterer_coordenadas(meme_json,0)

        top_left_x, top_left_y, bottom_right_x, bottom_right_y = coordenadas
        try:    
            fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_1-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
            draw.text([top_left_x, top_left_y], values['-TEXTO_1-'], font=fuente_ajustada, fill= color)
        except(PermissionError):
            sg.popup("No se cuentan con los permisos para acceder al directorio fuentes, por lo que la aplicacion no puede continuar, se cerrará el programa.")
            sys.exit()
        except(OSError):
            sg.popup('La fuente debe ser seleecionada desde la carpeta fuentes')

        
    if (values.get('-TEXTO_2-', '') != ''):
        coordenadas = obterer_coordenadas(meme_json,1)

        top_left_x, top_left_y, bottom_right_x, bottom_right_y = coordenadas
        try:
            fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_2-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
            draw.text([top_left_x, top_left_y], values['-TEXTO_2-'], font=fuente_ajustada, fill= color)
        except(PermissionError):
            sg.popup("No se cuentan con los permisos para acceder al directorio fuentes, por lo que la aplicacion no puede continuar, se cerrará el programa.")
            sys.exit()
        except(OSError):
            sg.popup('La fuente debe ser seleecionada desde la carpeta fuentes')
      
    if (values.get('-TEXTO_3-', '') != ''):
        coordenadas = obterer_coordenadas(meme_json,2)

        top_left_x, top_left_y, bottom_right_x, bottom_right_y = coordenadas
        try:
            fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_3-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
            draw.text([top_left_x, top_left_y], values['-TEXTO_3-'], font=fuente_ajustada, fill= color)
        except(PermissionError):
            sg.popup("No se cuentan con los permisos para acceder al directorio fuentes, por lo que la aplicacion no puede continuar, se cerrará el programa.")
            sys.exit()
        except(OSError):
            sg.popup('La fuente debe ser seleecionada desde la carpeta fuentes')
       
    if (values.get('-TEXTO_4-', '') != ''):
        coordenadas = obterer_coordenadas(meme_json,3)

        top_left_x, top_left_y, bottom_right_x, bottom_right_y = coordenadas
        try:
            fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_4-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
            draw.text([top_left_x, top_left_y], values['-TEXTO_4-'], font=fuente_ajustada, fill= color)
        except PermissionError:
            sg.popup_error("""No se cuentan con los permisos para acceder al directorio 'fuentes', por lo que la aplicacion no puede continuar, se cerrará el programa.""") 
        except(OSError):
            sg.popup('La fuente debe ser seleecionada desde la carpeta fuentes')
    
    
    if (values.get('-TEXTO_5-', '') != ''):
        coordenadas = obterer_coordenadas(meme_json,4)

        top_left_x, top_left_y, bottom_right_x, bottom_right_y = coordenadas

        try:
            fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_5-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
            draw.text([top_left_x, top_left_y], values['-TEXTO_5-'], font=fuente_ajustada, fill= color)
        except(PermissionError):
            sg.popup("No se cuentan con los permisos para acceder al directorio fuentes, por lo que la aplicacion no puede continuar, se cerrará el programa.")
            sys.exit()
        except(OSError):
            sg.popup('La fuente debe ser seleecionada desde la carpeta fuentes')
        
    
    return copia

def asigno_fuente(values):
    """Si no se le asigna otro valor se le deja el por defecto"""

    if (values['-FUENTE-'] == ''):
        values['-FUENTE-'] = fuente_default


def formato(nombre):
    """Chequea que el nombre del arhivo guardado tenga la extencion correcta"""
    
    return nombre.endswith('.jpg') or nombre.endswith('.png')
        
def guardar_meme(usuario,nombre,nombre_imagen,values,meme_actual):
    """Guardo el meme y actualizo los logs"""

    directorio_memes= configuracion.obtener_directorio('directorio_memes')
    meme_path = os.path.join(directorio_memes, nombre)

    meme_actual.save(meme_path)

    #Paso los valores del diccionario a una lista para poder agregarlos a los logs
    textos = list(values.values())
    log.registrar_interaccion(usuario,'Generacion meme', nombre_imagen, textos[1:])


