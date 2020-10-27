import PySimpleGUI as sg

# View do padrão MVC


class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window(
            "Consulta de clientes", self.__container, font=("Helvetica", 14))
        sg.theme('Topanga')

    def tela_consulta(self):
        linha1 = [
            sg.Text('Digite o código ou o nome do cliente e clique na ação desejada: ')]
        linha2 = [sg.Text('Nome: '), sg.InputText('', key="nome")]
        linha3 = [sg.Text('Código: '), sg.InputText('', key="codigo")]
        linha4 = [sg.Button('Cadastrar'), sg.Button(
            'Consultar'), sg.Button('Consultar todos'), sg.Button('Importar/Exportar')]
        linha5 = [sg.Text('', key="resultado", size=(50, 1))]

        self.__container = [linha1, linha2, linha3, linha4, linha5]
        self.__window = sg.Window(
            "Consulta de clientes", self.__container, font=("Helvetica", 14))

    def mostra_resultado(self, resultado):
        split = resultado.split('\n')
        height = len(split)
        self.__window.Element('resultado').Update(resultado)
        self.__window.Element('resultado').set_size((50, height - 1))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
