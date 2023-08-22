from .Contato import Contato
from unidecode import unidecode
from src.errors.ListaFazia import ListaFazia
from src.errors.error_handler import error_handler
from src.errors.UsuarioJaCadastrado import UsuarioJaCadastrado
from src.errors.ContatoNaoEncontrado import ContatoNaoEncontrado

class Lista:

    def __init__(self):
        self.lista = []
    
    def adicionar_contato(self, contato: Contato):
        if contato in self.lista:
            raise UsuarioJaCadastrado(nome=contato.nome)
        self.lista.append(contato)

    def exibir_contatos(self):
        if self.lista == []:
            raise ListaFazia()
        for contato in self.lista:
            print(f"Nome: {contato.nome} Telefone: {contato.telefone}")

    def pesquisar_contato(self, nome: str):
        if self.lista == []:
            raise ListaFazia()
        contatos_encontrados = []
        for contato in self.lista:
            if unidecode(contato.nome).lower().startswith(unidecode(nome).lower()):
                contatos_encontrados.append(f"Nome: {contato.nome} Telefone: {contato.telefone}")
        if contatos_encontrados == []:
            raise ContatoNaoEncontrado(nome=nome)
        for contato_encontrado in contatos_encontrados:
            print(contato_encontrado)

