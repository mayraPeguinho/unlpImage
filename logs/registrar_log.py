import csv
import os
import datetime
import PySimpleGUI as sg

ruta = os.path.realpath(os.path.realpath("."))
ruta_archivo = os.path.join(ruta, "logs.csv")


def agregar_log_al_registro(nick, operacion):
    
     '''Esta función agrega un registro al archivo logs.csv'''
     timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
     log = [timestamp, nick, operacion]
     try:
         with open(ruta_archivo, 'a', newline='', encoding='UTF-8') as archivo_csv:
             writer_csv = csv.writer(archivo_csv)
             writer_csv.writerow(log)
             archivo_csv.close()
     except FileNotFoundError:
         print("Archivo no encontrado")


def layout():
    return [
        [ 
            sg.Text('Nick:',justification="center"), 
            sg.InputText(key="-NICK-",  size=(50, 1),justification="center"), 
            sg.Button("Volver", key="-VOLVER-", expand_x=True,size=(4, 1), pad=((50,10), (1,1))),
        ],
        [sg.Button("Modificar imagen clasificada", key="-MODIFICAR IMAGEN CLASIFICADA-",),
        sg.Button("Nueva imagen clasificada", key="-NUEVA IMAGEN CLASIFICADA-",),
        sg.Button("Configuración", key="-CONFIGURACION-" )],
        [sg.Output(size=(70, 20), )]
    ]




     
def registrar_interraccion():
     '''Esta funcion registra los diferentes eventos que ocurren'''

     
     window = sg.Window('Registro de interacciones',layout(),finalize=True,resizable=True)
    
     while True:
         evento, valores = window.read()
         if evento== sg.WIN_CLOSED or evento == "-VOLVER-"    :
             break
         elif evento == "-CONFIGURACION-":
             print('Cambio en la configuración del sistema')
             agregar_log_al_registro(valores["-NICK-"], "configuracion")
         elif evento == "-NUEVA IMAGEN CLASIFICADA-":
             print('Nueva imagen clasificada')
             agregar_log_al_registro(valores["-NICK-"], "Nueva imagen")
         elif evento == "-MODIFICAR IMAGEN CLASIFICADA-":
             print("Modificación de imagen previamente clasificada")
             agregar_log_al_registro(valores["-NICK-"], "Modificación de imagen previamente clasificada")
          
     window.close()


if __name__ == "__main__":
     registrar_interraccion()