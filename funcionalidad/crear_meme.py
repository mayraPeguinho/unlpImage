import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw
import PIL.ImageFont

def tam_boxes():
    pass

def entra(contenedor,contenido):
    """Calcula si el texto entra en la caja"""
    return contenido[0] <= contenedor[0] and contenido[0] <= contenedor[0]

def tam_box(x1,y1,x2,y2):
    """Calcula el tamaño de la box"""
    return (x2 - x1, y2 - y1)

def calcular_tam_fuente(draw, texto, path_fuente, box):
    """Va achicando el tamañio de la fuente hast encontrar el ideal para el meme"""
    tam_contenedor = tam_box(*box)
    for tam in range(200, 20, -5):
        fuente = PIL.ImageFont.truetype(path_fuente, tam)
        box_texto = draw.textbbox([0, 0], texto, font = fuente)
        tam_box_texto = tam_box(*box_texto)
        if entra(tam_contenedor,tam_box_texto):
            return fuente
        
    return fuente

def actualizar_datos(meme,values,fuente):
    """Se actualiza lo escrito en el meme"""

    copia = meme.copy()
    draw = PIL.ImageDraw.Draw(copia)
    if (values['TEXTO_1'] != ''):
        fuente_ajustada = calcular_tam_fuente(draw,values['-TEXTO_1-'],fuente,(top_left_x,top_left_y,bottom_right_x,bottom_rigth_y))
        draw.text([top_left_x, top_left_y], values['TEXTO_1'], font=fuente_ajustada)
        
    if (values['TEXTO_2'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_2'], font=fuente)
    
    if (values['TEXTO_3'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_3'], font=fuente)

    if (values['TEXTO_4'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_4'], font=fuente)

    if (values['TEXTO_5'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_5'], font=fuente)

    return copia

def recorrer_archivo(data,imagen_seleccionada):
    """Cuento en el archivo json la cantidad de text_boxes que tiene"""

    cuadros_de_texto = [item['text_boxes'] for item in data if (item['image'] == imagen_seleccionada)]
    cantidad_cuadros = cuadros_de_texto.__len__()

    return cantidad_cuadros