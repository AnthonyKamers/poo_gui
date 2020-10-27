from ClienteExportImportView import ClienteExportImportView
import PySimpleGUI as sg


class ClienteExportImportController:
    def __init__(self):
        self.__tela = ClienteExportImportView(self)

    def inicia(self):
        container = self.__tela.tela_importa_exporta()

        # loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__tela.le_eventos()
