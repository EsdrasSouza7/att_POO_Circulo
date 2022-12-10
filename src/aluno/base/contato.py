from src.cliente.contato_base import ContatoBase


class Contato(ContatoBase):

    def __init__(self, id: str, email: str):
        super().__init__(id, email)

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email

    def setId(self, id: str):
        self.id = id
        return True

    def setEmail(self, email: str):
        self.email = email
        return True

    def getFavorito(self):
        return self.favorito


