import PySimpleGUI as sg

def generar_collage():
    layout = [
             [sg.Text("Seleccionar imágenes:"),sg.Input(), sg.FileBrowse(button_text= "Seleccionar")],
             [sg.Text("Seleccionar plantilla:   "),sg.Combo(["Plantilla 1", "Plantilla 2", "Plantilla 3","Plantilla 4"],key="Listar Plantillas")],
             [sg.Button("Generar collage"), sg.Button("Salir")]
             ]

    window = sg.Window('Generador de collage', layout, margins=(200,150))

    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED or evento == "Salir":
            break
        elif evento == "Generar collage":
            #funcion que genera
            print("Collage generado correctamente")
    window.close()

if __name__ =="__main__":
    generar_collage()


    