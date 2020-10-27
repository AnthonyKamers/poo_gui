from DAO import DAO
import pickle


class ClienteDAO(DAO):
    def __init__(self, arquivo):
        super().__init__(arquivo)

    def add(self, cliente):
        super().add(cliente)

    def get(self, codigo):
        return super().get(codigo)

    def remove(self, cliente):
        return super().remove(cliente.codigo)

    def get_all(self):
        return super().get_all()

    def length(self):
        return len(super().get_all())
