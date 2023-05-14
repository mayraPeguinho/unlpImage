import csv
import os
import sys
import datetime
ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
ruta_archivo = os.path.join(ruta, "logs.csv")

def registrar_interaccion(nick, operacion):
    
     '''Esta función agrega un registro al archivo logs.csv'''
     
     timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
     log = [timestamp, nick, operacion]

     #para verificar si el archivo existe o no.
     archivo_existe = os.path.isfile(ruta_archivo)

     try:
         with open(ruta_archivo, 'a', newline='', encoding='UTF-8') as archivo_csv:
             writer_csv = csv.writer(archivo_csv)
             #si aun no existe, escribe la primer fila, la cual contiene los encabezados
             if not archivo_existe:
                 writer_csv.writerow(["Fecha y Hora", "Nick", "Operación"])   
             writer_csv.writerow(log)
     except (FileNotFoundError,PermissionError):
         pass


