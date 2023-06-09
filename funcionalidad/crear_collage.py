import os
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

from rutas import ruta_directorio_collages


def crear_collage_diseño_1(imagen, pos, collage):
    
      """ Crea el collage del diseño 1 utilizando una imagen en una posición específica.
      recibe  la ruta de la imagen a utilizar,la posición de la imagen en el collage (1 o 2) y
      la imagen base sobre la que esta construyendo el collage.
      Retorna el collage actualizado con la nueva imagen. """

      image = PIL.Image.open(imagen)
      if pos == 1:
           image = PIL.ImageOps.fit(image, (400, 200))
           collage.paste(image, (0, 0))
      else:
           image = PIL.ImageOps.fit(image, (400, 200))
           collage.paste(image, (0, 200))

      return collage



def crear_collage_diseño_2(imagen,pos,collage):
      
      """ Crea el collage del diseño 2 utilizando una imagen en una posición específica.
      recibe  la ruta de la imagen a utilizar,la posición de la imagen en el collage (1,2 o 3) y
      la imagen base sobre la que esta construyendo el collage.
      Retorna el collage actualizado con la nueva imagen. """
      
      image = PIL.Image.open(imagen)
      if pos == 1:
           image  = PIL.ImageOps.fit(image ,(400,200))
           collage.paste(image , (0, 0))
      elif pos == 2:
           image  = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (0,200))
      elif pos == 3:
           image  = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (200,200))
    
      return collage


def crear_collage_diseño_3(imagen,pos,collage):
      
      """ Crea el collage del diseño 3 utilizando una imagen en una posición específica.
      recibe  la ruta de la imagen a utilizar,la posición de la imagen en el collage (1,2,3 o 4) y
      la imagen base sobre la que esta construyendo el collage.
      Retorna el collage actualizado con la nueva imagen. """

      image = PIL.Image.open(imagen)
      if pos == 1:
           image  = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (0, 0))
      elif pos == 2:
           image  = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (200,0))
      elif pos == 3:
           image = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (0,200))
      elif pos== 4:
           image  = PIL.ImageOps.fit(image ,(200,200))
           collage.paste(image , (200,200))
    
      return collage
     


def crear_collage_diseño_4(imagen,pos,collage):
      
      """ Crea el collage del diseño 4 utilizando una imagen en una posición específica.
      recibe  la ruta de la imagen a utilizar,la posición de la imagen en el collage (1 o 2) y
      la imagen base sobre la que esta construyendo el collage.
      Retorna el collage actualizado con la nueva imagen. """
      
      image = PIL.Image.open(imagen)
      if pos == 1:
           image = PIL.ImageOps.fit(image,(200,400))
           collage.paste(image, (0, 0))
      else:
          image = PIL.ImageOps.fit(image,(200,400))
          collage.paste(image, (200,0))
     
     
      return collage



def guardar_collage(titulo,collage):
     
     collage_path = os.path.join(ruta_directorio_collages, f"{titulo}.png")
     collage.save(collage_path)