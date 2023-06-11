import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

def actualizar_datos(meme,fuente,texto):
    """Se actualiza lo escrito en el meme"""

    copia = meme.copy()
    draw = PIL.ImageDraw.Draw(copia)

    draw.text([top_left_x, top_left_y], texto, font=fuente)

    return copia