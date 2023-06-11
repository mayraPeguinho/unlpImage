import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

def actualizar_datos(meme):
    """Se actualiza lo escrito en el meme"""

    copia = meme.copy()
    draw = PIL.ImageDraw.Draw(copia)

    return copia