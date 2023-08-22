from .Contato import Contato
from unidecode import unidecode
from errors.ListaFazia import ListaFazia
from errors.UsuarioJaCadastrado import UsuarioJaCadastrado
from errors.ContatoNaoEncontrado import ContatoNaoEncontrado

class Lista:

    def __init__(self):
        self.lista = []
    
    def adicionar_contato(self, contato: Contato):
        """Adiciona um contato a lista"""
        if contato in self.lista:
            raise UsuarioJaCadastrado(nome=contato.nome)
        self.lista.append(contato)

    def exibir_contatos(self):
        """Exibe todos os contatos da lista"""
        if self.lista == []:
            raise ListaFazia()
        for contato in self.lista:
            print(f"Nome: {contato.nome} Telefone: {contato.telefone}")

    def pesquisar_contato(self, nome: str):
        """Mostra os contatos que tem o nome com as iniciais do nome pesquisado"""
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

