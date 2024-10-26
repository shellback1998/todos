import FreeSimpleGUI as sg
from zip_extractor import extract_archive


sg.theme('Black')

label1 = sg.Text('Select archive:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output',text_color='green')

col1 = sg.Column([[label1],[label2]])
col2 = sg.Column([[input1],[input2]])
col3 = sg.Column([[choose_button1],[choose_button2]])

window = sg.Window('Archive Extractor',layout=[[col1,col2,col3],[extract_button]])



# window = sg.Window('Archive Extractor',
#                     layout=[[label1,input1, choose_button1],
#                             [label2, input2,choose_button2],
#                             [extract_button, output_label]])

while True:

    event, values = window.read()
    match event:
        case "Extract":
            print(event, values)
            archivepath = values['archive']
            dest_path = values['folder']
            extract_archive(archivepath, dest_path)
            window['output'].update(value='Extracted')
        case sg.WINDOW_CLOSED:
            break

window.close()