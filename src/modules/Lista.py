from .Contato import Contato
from src.errors.ListaFazia import ListaFazia
from src.errors.error_handler import error_handler
from src.errors.UsuarioJaCadastrado import UsuarioJaCadastrado

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
            print(f"\nNome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")

