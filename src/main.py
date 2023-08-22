from modules.Lista import Lista
from modules.Contato import Contato


lista = Lista()
contato = Contato("Victor", "Telefone Victor")
lista.adicionar_contato(contato=contato)

lista.pesquisar_contato("v")
