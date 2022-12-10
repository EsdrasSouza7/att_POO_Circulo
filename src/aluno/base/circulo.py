from src.cliente.circulo_base import CirculoBase


class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super().__init__(id, limite)
        self.contatosNoCirculo = []

    def getNumberOfContacts(self):
        return len(self.contatosNoCirculo)

    def setLimite(self, limite: int):
        pass

    def getId(self):
        return self.id

    def getLimite(self):
        return self.limite