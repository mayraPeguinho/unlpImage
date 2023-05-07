import PySimpleGUI as sg

def generar_meme():
    '''Esta funcion define una ventana 
       para generar memes a partir de una imágen y un seleccionados por el usuario. '''
    layout = [
             [ sg.Text("Generar Meme", font=("Helvetica", 20), justification="left"),
             sg.Column([[sg.Button("Volver ➡", key="-VOLVER-")]],expand_x=True,element_justification="right"),],
             [sg.Text('Seleccionar imagen:')],
             [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar imagen")],
             [sg.Text('Introducir el texto:')],
             [sg.InputText()],
             [sg.Column([[sg.Button("Generar", "-GENERAR-")]], expand_x=True, element_justification="right")],
            
           ]
    window = sg.Window('Generador de memes',layout, margins=(60, 80), finalize=True, resizable=True)

    while True:
         evento, valores = window.Read()
    
         if evento == "-GENERAR-":
             pass   
         elif evento == "-VOLVER-" or evento== sg.WIN_CLOSED:
             break
        
    window.Close()

if __name__ =="__main__":
    generar_meme()
  