import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

def actualizar_datos(meme,values,fuente):
    """Se actualiza lo escrito en el meme"""

    copia = meme.copy()
    draw = PIL.ImageDraw.Draw(copia)
    if (values['TEXTO_1'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_1'], font=fuente)
    
    if (values['TEXTO_2'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_2'], font=fuente)
    
    if (values['TEXTO_3'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_3'], font=fuente)

    if (values['TEXTO_4'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_4'], font=fuente)

    if (values['TEXTO_5'] != ''):
        draw.text([top_left_x, top_left_y], values['TEXTO_5'], font=fuente)

    return copia

def recorrer_archivo(archivo):
    """Cuento en el archivo json la cantidad de text_boxes que tiene"""

    cuadros_de_texto = [item['text_boxes'] for item in data if (item['image'] == imagen_seleccionada)]
    cantidad_cuadros = cuadros_de_texto.__len__()

    return cantidad_cuadros