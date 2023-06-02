import sys
import os
import PySimpleGUI as Sg

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pantallas import inicio

Sg.theme("DarkBlue14")
inicio.eventos_inicio()