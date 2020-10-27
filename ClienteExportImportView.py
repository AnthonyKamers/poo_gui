import PySimpleGUI as sg


class ExportImportView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window(
            "Importar / Exportar Backup Clientes", self.__container, font=("Helvetica", 14))
        sg.theme('Topanga')

    def tela_importa_exporta(self):
        linha0 = [sg.Text('Arquivo de dados (Importar): '),
                  sg.InputText('', key="path_import"), sg.Button('Importar')]

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
