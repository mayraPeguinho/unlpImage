import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image


columna_izquierda = [[sg.Text('Nuevo perfil')],
          [sg.Text('Usuario:')],[sg.InputText(key='-USUARIO-')], 
          [sg.Text('Nombre:')],[sg.InputText(key='-NOMBRE-')],
          [sg.Text('Edad:')],[sg.InputText(key='-EDAD-')],
          [sg.Text('Genero:')],
          [sg.Listbox(['Masculino', 'Femenino', 'Otro'],no_scrollbar=False, s=(15,3))],
             [sg.InputText(key='-ESPECIFICAR_GENERO-')],
          [sg.Button('Guardar'), sg.Button('Volver')]]



columna_derecha = [[sg.Image(key='-IMAGE-')],
              [sg.Button('Seleccionar Imagen')]]

layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]

window = sg.Window('Nuevo perfil', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()