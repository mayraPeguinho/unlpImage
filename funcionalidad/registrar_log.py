import csv
import os
import datetime
import PySimpleGUI as sg

ruta = os.path.realpath(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "logs","logs.csv")


def registrar_interaccion(nick, operacion):
    
     '''Esta función agrega un registro al archivo logs.csv'''
     timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
     log = [timestamp, nick, operacion]
     try:
         with open(ruta_archivo, 'a', newline='', encoding='UTF-8') as archivo_csv:
             writer_csv = csv.writer(archivo_csv)
             writer_csv.writerow(log)
     except FileNotFoundError:
         print("Archivo no encontrado")

