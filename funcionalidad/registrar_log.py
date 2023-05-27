import csv
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from datetime import datetime
from rutas import archivo_logs_csv as ruta_archivo

def registrar_interaccion(nick, operacion,valores=None,textos=None):
    
     '''Esta función agrega un registro al archivo logs.csv'''
     
     timestamp = datetime.timestamp(datetime.now())
     log = [timestamp, nick, operacion,valores,textos]

     #para verificar si el archivo existe o no.
     archivo_existe = os.path.isfile(ruta_archivo)

     try:
         with open(ruta_archivo, 'a', newline='', encoding='UTF-8') as archivo_csv:
             writer_csv = csv.writer(archivo_csv)
             #si aun no existe, escribe la primer fila, la cual contiene los encabezados
             if not archivo_existe:
                 writer_csv.writerow(["Fecha y Hora", "Nick", "Operación","Valores", "Textos"])   
             writer_csv.writerow(log)
     except (FileNotFoundError,PermissionError):
         pass


