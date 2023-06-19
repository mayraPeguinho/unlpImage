import PySimpleGUI as sg
import csv
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from datetime import datetime
from rutas import archivo_logs_csv as ruta_archivo

def registrar_interaccion(nick, operacion,valores=None,textos=None):
    
     '''Esta función agrega una interaccion en el sistema al archivo logs.csv'''
     
     timestamp = datetime.timestamp(datetime.now())
     #verifico que tenga datos
     if valores:
         #verifico que sea una lista
         if(isinstance(valores,list)):
             valores=";".join(valores)
     else:
         valores= ''

     if textos:
         if(isinstance(textos,list)):
             textos=";".join(textos)
     else:
         textos= ''

     log = [timestamp, nick, operacion,valores,textos]

     #para verificar si el archivo existe o no.
     archivo_existe = os.path.exists(ruta_archivo)
    
     try:
         with open(ruta_archivo, 'a', newline='', encoding='UTF-8') as archivo_csv:
             writer_csv = csv.writer(archivo_csv)
             #si aun no existe, escribe la primer fila, la cual contiene los encabezados
             if not archivo_existe:
                 writer_csv.writerow(["Fecha y Hora", "Nick", "Operación","Valores", "Textos"])   
             writer_csv.writerow(log)
     except FileNotFoundError:
         sg.popup_error("""No se encuentra el archivo 'logs.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
         sys.exit()
     except PermissionError:
         sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'logs.csv', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
         sys.exit()
     except Exception as e:
         sg.popup_error(f"Se produjo un error al escribir en el archivo: {e}. La aplicación no puede continuar. Se cerrará el programa.")
         sys.exit()

