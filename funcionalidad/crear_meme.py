import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw
import PIL.ImageFont
import os
from funcionalidad import registrar_log as log
from rutas import ruta_directorio_memes
from rutas import ruta_directorio_fuentes

fuente_default = os.path.join(ruta_directorio_fuentes, 'Lato-BoldItalic.ttf')

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
        top_left_x = meme_json[0]['text_boxes'][0]['top_left_x']
        top_left_y = meme_json[0]['text_boxes'][0]['top_left_y']
        bottom_right_x = meme_json[0]['text_boxes'][0]['bottom_right_x']
        bottom_right_y = meme_json[0]['text_boxes'][0]['bottom_right_y']
        
        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_1-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
        draw.text([top_left_x, top_left_y], values['-TEXTO_1-'], font=fuente_ajustada, fill= color)
        
  
    if (values.get('-TEXTO_2-', '') != ''):
        top_left_x = meme_json[0]['text_boxes'][1]['top_left_x']
        top_left_y = meme_json[0]['text_boxes'][1]['top_left_y']
        bottom_right_x = meme_json[0]['text_boxes'][1]['bottom_right_x']
        bottom_right_y = meme_json[0]['text_boxes'][1]['bottom_right_y']

        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_2-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
        draw.text([top_left_x, top_left_y], values['-TEXTO_2-'], font=fuente_ajustada, fill= color)


    if (values.get('-TEXTO_3-', '') != ''):
        top_left_x = meme_json[0]['text_boxes'][2]['top_left_x']
        top_left_y = meme_json[0]['text_boxes'][2]['top_left_y']
        bottom_right_x = meme_json[0]['text_boxes'][2]['bottom_right_x']
        bottom_right_y = meme_json[0]['text_boxes'][2]['bottom_right_y']

        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_3-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
        draw.text([top_left_x, top_left_y], values['-TEXTO_3-'], font=fuente_ajustada, fill= color)
    
    if (values.get('-TEXTO_4-', '') != ''):
        top_left_x = meme_json[0]['text_boxes'][3]['top_left_x']
        top_left_y = meme_json[0]['text_boxes'][3]['top_left_y']
        bottom_right_x = meme_json[0]['text_boxes'][3]['bottom_right_x']
        bottom_right_y = meme_json[0]['text_boxes'][3]['bottom_right_y']

        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_4-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
        draw.text([top_left_x, top_left_y], values['-TEXTO_4-'], font=fuente_ajustada, fill= color)
    
    if (values.get('-TEXTO_5-', '') != ''):
        top_left_x = meme_json[0]['text_boxes'][4]['top_left_x']
        top_left_y = meme_json[0]['text_boxes'][4]['top_left_y']
        bottom_right_x = meme_json[0]['text_boxes'][4]['bottom_right_x']
        bottom_right_y = meme_json[0]['text_boxes'][4]['bottom_right_y']

        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_5-'],values['-FUENTE-'],(top_left_x,top_left_y,bottom_right_x,bottom_right_y))
        draw.text([top_left_x, top_left_y], values['-TEXTO_5-'], font=fuente_ajustada, fill= color)
    
    return copia

def calculo_cajas(meme_json,imagen_seleccionada):
    """Cuento en el archivo json la cantidad de text_boxes que tiene"""

    #meme_json = [item for item in meme_json if item['image'] == os.path.basename(imagen_seleccionada)]

    cant_cajas = (meme_json[0]['text_boxes'].__len__())

    return cant_cajas

def asigno_fuente(values):
    """Si no se le asigna otro valor se le deja el por defecto"""

    if (values['-FUENTE-'] == ''):
        values['-FUENTE-'] = fuente_default
    print(values)
def guardar_meme(usuario,nombre,nombre_imagen,values,meme_actual):
    """Guardo el meme y actualizo los logs"""

    meme_path = os.path.join(ruta_directorio_memes, f"{nombre}.png")

    meme_actual.save(meme_path)

    #Paso los valores del diccionario a una lista para poder agregarlos a los logs
    textos = list(values.values())
    log.registrar_interaccion(usuario,'Generacion meme', nombre_imagen, textos[1:])
