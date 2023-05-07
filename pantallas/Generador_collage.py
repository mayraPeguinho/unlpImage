import PySimpleGUI as sg

def generar_collage():
     '''Esta funcion define una ventana 
       para generar collages a partir de imágenes y plantillas seleccionadas por el usuario. '''
     layout = [
    [
        sg.Text("Generar Collage", font=("Helvetica", 20), justification="left"),
        sg.Column(
            [[sg.Button("Volver ➡", key="-VOLVER-")]],
            expand_x=True,
            element_justification="right"
        ),
     ],
     [sg.Text("Seleccionar imágenes")],
     [sg.Input(), sg.FileBrowse(button_text="Seleccionar")],
     [sg.Text("Seleccionar plantilla")],
     [sg.Combo(["Plantilla 1", "Plantilla 2", "Plantilla 3", "Plantilla 4"], key="Listar Plantillas")],
     [sg.Column([[sg.Button("Generar Collage", "-GENERAR COLLAGE-")]], expand_x=True, element_justification="right")],
     ]

     window = sg.Window('Generador de collage', layout, margins=(60, 80), finalize=True, resizable=True)

     while True:
         evento, valores = window.read()
         if evento == sg.WIN_CLOSED or evento == "-VOLVER-":
             break
         elif evento == "-GENERAR COLLAGE-":
              # función que genera
              print("Collage generado correctamente")

     window.close()


if __name__ =="__main__":
     generar_collage()


    