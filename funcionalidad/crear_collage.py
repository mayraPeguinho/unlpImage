import PySimpleGUI as sg
import os, sys
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw
import csv

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad import registrar_log as log
from rutas import archivo_imagenes_etiquetadas_csv as ruta_archivo
from funcionalidad import configuracion as conf



def obtener_imagenes():
      """Lee un archivo csv que contiene información sobre imágenes y devuelve un diccionario con las descripciones
      como claves y los nombres de las imágenes como valores. """
      try:
           imagenes = {}
           repetidas = {}
           with open(ruta_archivo, 'r') as archivo_csv:
                reader = csv.reader(archivo_csv)
                next(reader)  
                for row in reader:
                     descripcion = row[1]
                     ruta_repo = conf.obtener_directorio('repositorio_imagenes')
                     nombre_archivo = os.path.basename(row[0])
                     nombre_imagen = os.path.join(ruta_repo, nombre_archivo)

                     #para que no la sobreescriba la descripción, si ya existe
                     if descripcion in imagenes:
                          # Si la descripción ya existe en el diccionario de repetidas, incrementa el contador correspondiente
                          if descripcion in repetidas:
                               repetidas[descripcion] += 1
                          else:
                               repetidas[descripcion] = 2
                          #Agrega un sufijo del contador a la descripción
                          descripcion = f"{descripcion}_{repetidas[descripcion]}"
                     imagenes[descripcion] = nombre_imagen
      except(FileNotFoundError):
           sg.popup_error("""No se ha encontrado el archivo 'imagenes_etiquetadas.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
           sys.exit()
      except PermissionError:
           sg.popup_error("No se cuentan con los permisos para acceder al archivo 'imagenes_etiquetadas.csv',por lo que la aplicacion no puede continuar, se cerrará el programa.")
           sys.exit()


      return imagenes

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
      """ Crea el collage del diseño 4 utilizando una imagen en una posición especifica.
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

def insertar_titulo(titulo, collage):
    '''Recibe un título y lo inserta en el collage recibido.
    Retorna una copia del collage modificado.'''
    copia = collage.copy()
    draw = PIL.ImageDraw.Draw(copia)
    draw.text((10, 380), titulo, fill="white")

    return copia

def existe_nombre(nombre):
      '''Retorna True si el nombre ya existe en el directorio de collages, False en caso contrario'''
      directorio_collages=conf.obtener_directorio('directorio_collages')
      nombres = os.listdir(directorio_collages)   
      return any(map(lambda x: x == nombre, nombres))

def es_nombre_valido(nombre):
      '''Verifica si el texto dado es válido para ser utilizado como nombre de archivo.'''
      invalidos = '[<>\}/|;*#$%!¡?¿ ]'
      return not any(caracter in invalidos for caracter in nombre)




def guardar_collage(nombre,collage,imagenes_usadas,usuario,titulo, cant_imagenes):
      '''Guarda el collage en el repositorio de collages
      y registra el evento en el archivo de logs.'''

      directorio_collages= conf.obtener_directorio('directorio_collages')
      collage_path = os.path.join(directorio_collages, f"{nombre}.png")
      collage.save(collage_path)
      
      #asi obtengo solo las últimas imagenes seleccionadas.
      if len(imagenes_usadas) > cant_imagenes:
            imagenes_usadas = imagenes_usadas[-cant_imagenes:]
      log.registrar_interaccion(usuario,"Generación de collage",imagenes_usadas,titulo)
