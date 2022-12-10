from src.aluno.base.circulo import Circulo
from src.aluno.base.contato import Contato
from src.cliente.circulo_base import CirculoBase
from src.cliente.circulo_not_found_exception import CirculoNotFoundException
from src.cliente.contato_base import ContatoBase
from src.cliente.contato_not_found_exception import ContatoNotFoundException
from src.cliente.icirculo_operations_manager import ICirculoOperationsManager
from src.cliente.icirculos_manager import ICirculosManager
from src.cliente.icontatos_manager import IContatosManager


class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):

    def __init__(self):
        self.contatos = []
        self.cirulos = []

    def buscaPorIdContato(self, id: str):
        for contatos in self.contatos:
            if contatos.getId() == id:
                return contatos
        return None

    def createContact(self, id: str, email: str) -> bool:
        contatos = self.buscaPorIdContato(id)
        if contatos is not None:
            return False
        else:
            temp = Contato(id, email)
            self.contatos.append(temp)
            return True

    def getAllContacts(self) -> list:
        retorno = []
        temp = {}
        for contato in self.contatos:
            temp[contato.getId()] = contato
        nomes = sorted(temp)
        for ordenado in nomes:
            retorno.append(temp.get(ordenado))
        return retorno

    def updateContact(self, contato: ContatoBase) -> bool:
        pessoa = self.buscaPorIdContato(contato.getId())
        if pessoa is not None:
            self.contatos.remove(pessoa)
            self.contatos.append(contato)
            return True
        else:
            return False

    def removeContact(self, id: str) -> bool:
        contatos = self.buscaPorIdContato(id)
        if contatos is not None:
            self.contatos.remove(contatos)
            for circulos in self.cirulos:
                for contat in circulos.contatosNoCirculo:
                    if contatos == contat:
                        circulos.contatosNoCirculo.remove(contatos)
                        circulos.limite = circulos.limite + 1
            return True
        return False


    def getContact(self, id: str) -> ContatoBase:
        contatos = self.buscaPorIdContato(id)
        if contatos is not None:
            return contatos
        return None

    def getNumberOfContacts(self) -> int:
        return len(self.contatos)

    def favoriteContact(self, idContato: str) -> bool:
        contatos = self.buscaPorIdContato(idContato)
        if contatos is not None:
            contatos.favorito = True
            return True
        return False

    def unfavoriteContact(self, idContato: str) -> bool:
        contato = self.buscaPorIdContato(idContato)
        if contato is not None:
            contato.favorito = False
            return True
        return False

    def isFavorited(self, id: str) -> bool:
        contato = self.buscaPorIdContato(id)
        if contato is not None:
            return contato.getFavorito()
        return False

    def getFavorited(self) -> list:
        favorito = []
        for contato in self.contatos:
            if contato.getFavorito():
                favorito.append(contato)
        return favorito

    def buscaPorIdCirculo(self, id: str):
        for circulo in self.cirulos:
            if circulo.getId() == id:
                return circulo
        return None

    def createCircle(self, id: str, limite: int) -> bool:
        circulo = self.buscaPorIdCirculo(id)
        if limite > 0:
            if circulo is not None:
                return False
            else:
                temp = Circulo(id, limite)
                self.cirulos.append(temp)
                return True
        return False

    def updateCircle(self, circulo: CirculoBase) -> bool:
        circulos = self.buscaPorIdCirculo(circulo.getId())
        if circulo.getLimite() >= 1:
            if circulos is not None:
                self.cirulos.remove(circulos)
                self.cirulos.append(circulo)
                return True
            else:
                return False
        return False

    def getCircle(self, idCirculo: str) -> CirculoBase:
        circulo = self.buscaPorIdCirculo(idCirculo)
        if circulo is not None:
            return circulo
        return None

    def getAllCircles(self) -> list:
        retorno = []
        temp = {}
        for circulo in self.cirulos:
            temp[circulo.getId()] = circulo
        nomes = sorted(temp)
        for ordenado in nomes:
            retorno.append(temp.get(ordenado))
        return retorno

    def removeCircle(self, idCirculo: str) -> bool:
        circulo = self.buscaPorIdCirculo(idCirculo)
        if circulo is not None:
            self.cirulos.remove(circulo)
            return True
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.cirulos)

    def tie(self, idContato: str, idCirculo: str) -> bool:
        circulo = self.buscaPorIdCirculo(idCirculo)
        if circulo is None:
            raise CirculoNotFoundException(idCirculo)
        if circulo.getLimite() > 0:
            contato = self.buscaPorIdContato(idContato)
            if contato is None:
                raise ContatoNotFoundException(idContato)
            for cir in circulo.contatosNoCirculo:
                if contato == cir:
                    return False
            if circulo is not None and contato is not None:
                circulo.contatosNoCirculo.append(contato)
                circulo.limite = circulo.limite - 1
                return True
            return False
        return False

    def untie(self, idContato: str, idCirculo: str) -> bool:
        circulo = self.buscaPorIdCirculo(idCirculo)
        if circulo is None:
            raise CirculoNotFoundException(idCirculo)
        contato = self.buscaPorIdContato(idContato)
        if contato is None:
            raise ContatoNotFoundException(idContato)
        if circulo is not None and contato is not None:
            circulo.contatosNoCirculo.remove(contato)
            circulo.limite = circulo.limite + 1
            return True
        return False

    def getContacts(self, id: str) -> list:
        circulo = self.buscaPorIdCirculo(id)
        if circulo is None:
            raise CirculoNotFoundException(id)
        if circulo is not None:
            retorno = []
            temp = {}
            for lista in circulo.contatosNoCirculo:
                temp[lista.getId()] = lista
            nomes = sorted(temp)
            for ordenado in nomes:
                retorno.append(temp.get(ordenado))
            return retorno
        return None

    def getCircles(self, id: str) -> list:
        pertence = []
        contato = self.buscaPorIdContato(id)
        if contato is None:
            raise ContatoNotFoundException(id)
        else:
            for circulo in self.cirulos:
                for contatosC in circulo.contatosNoCirculo:
                    if contatosC == contato:
                        pertence.append(circulo)
                        break
            retorno = []
            temp = {}
            for lista in pertence:
                temp[lista.getId()] = lista
            nomes = sorted(temp)
            for ordenado in nomes:
                retorno.append(temp.get(ordenado))
            return retorno

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        pertenceC1 = []
        pertenceC2 = []
        igual = []
        contato1 = self.buscaPorIdContato(idContato1)
        contato2 = self.buscaPorIdContato(idContato2)
        if contato1 is None:
            raise ContatoNotFoundException(idContato1)
        if contato2 is None:
            raise ContatoNotFoundException(idContato2)
        for circulo in self.cirulos:
            for contatosC in circulo.contatosNoCirculo:
                if contatosC== contato1:
                    pertenceC1.append(circulo)
                    break
        for circulo in self.cirulos:
            for contatosC in circulo.contatosNoCirculo:
                if contatosC == contato2:
                    pertenceC2.append(circulo)
                    break
        for C1 in pertenceC1:
            for C2 in pertenceC2:
                if C1 == C2:
                    igual.append(C1)
        return igual
