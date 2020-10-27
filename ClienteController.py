from ClienteView import ClienteView
import PySimpleGUI as sg
from Cliente import Cliente
from ClienteDAO import ClienteDAO


class ClienteController:
    def __init__(self, arquivo='clientes.pkl'):
        self.__telaCliente = ClienteView(self)
        self.__clientes = ClienteDAO(arquivo)  # pickle de clientes (padrão)

    def inicia(self):
        container = self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                try:
                    nome = str(values['nome'])
                    codigo = int(values['codigo'])

                    nomeJaCadastrado = self.busca_nome(nome)
                    codigoJaCadastrado = self.busca_codigo(codigo)

                    if (not nomeJaCadastrado and not codigoJaCadastrado):
                        self.adiciona_cliente(codigo, nome)
                        resultado = 'Cliente cadastrado'
                    else:
                        resultado = 'Cliente já cadastrado!'
                except ValueError as e:
                    resultado = 'Código deve ser um inteiro'

            elif event == 'Consultar':
                try:
                    nome = str(values['nome'])
                    if (values['codigo'] == ''):
                        codigo = ''
                    else:
                        codigo = int(values['codigo'])

                    cliente = self.busca_nome(
                        nome) or self.busca_codigo(codigo)

                    if not cliente:
                        resultado = 'Cliente não encontrado!'
                    else:
                        resultado = str(cliente)
                except ValueError as e:
                    resultado = 'Código deve ser um inteiro'

            elif event == 'Consultar todos':
                resultado = self.get_all_clientes()

            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()

    def busca_codigo(self, codigo):
        if codigo == '':
            return False
        return self.__clientes.get(codigo)

    def adiciona_cliente(self, codigo, nome):
        cliente = Cliente(codigo, nome)
        self.__clientes.add(cliente)

    def busca_nome(self, nome):
        if nome == '':
            return False

        for cliente in self.__clientes.get_all():
            if cliente.nome == nome:
                return cliente
        return False

    def get_all_clientes(self):
        x = ''
        for cliente in self.__clientes.get_all():
            x += str(cliente) + '\n'

        return x
