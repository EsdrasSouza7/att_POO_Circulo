from src.cliente.exception_base import ExceptionBase


class ContatoNotFoundException  (ExceptionBase):


    def __init__(self, contatoId: str, message="Circulo não encontrado"):
        super().__init__(message)
        self.contatoId = contatoId

    def getContatoNaoEncontrado(self):
        return self.contatoId