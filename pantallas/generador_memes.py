import PySimpleGUI as sg

def generar_meme():
    layout = [
             [sg.Text('Seleccionar imagen:')],
             [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar imagen")],
             [sg.Text('Introducir el texto:')],
             [sg.InputText()],
             [sg.OK(button_text="Generar"), sg.Cancel(button_text="Volver")]
            
           ]
    window = sg.Window('Generador de memes').Layout(layout)

    while True:
         evento, valores = window.Read()
    
         if evento == 'Generar':
             pass   
         elif evento == 'Volver' or evento== sg.WIN_CLOSED:
             break
        
    window.Close()

if __name__ =="__main__":
    generar_meme()
  