import sys
import pytest
from io import StringIO
from src.modules.Lista import Lista
from src.modules.Contato import Contato
from src.errors.ListaFazia import ListaFazia
from src.errors.UsuarioJaCadastrado import UsuarioJaCadastrado


lista1 = Lista()
contato1 = Contato(nome="Amanda", telefone="Telefone Amanda")

def test_adicionar_contato():
    lista1.adicionar_contato(contato1)

    assert contato1 in lista1.lista

def test_adicionar_contato_ja_cadastrado():
    with pytest.raises(UsuarioJaCadastrado) as exc_info:
        lista1.adicionar_contato(contato1)

    assert isinstance(exc_info.value, UsuarioJaCadastrado)

def test_exibir_contatos():
    contato2 = Contato(nome="Vinício", telefone="Telefone Vinício")
    lista1.adicionar_contato(contato=contato2)

    pegar_output = StringIO()
    sys.stdout = pegar_output

    lista1.exibir_contatos()

    sys.stdout = sys.__stdout__

    output = pegar_output.getvalue()

    assert f"Nome: {contato1.nome}" in output
    assert f"Telefone: {contato1.telefone}" in output
    assert f"Nome: {contato2.nome}" in output
    assert f"Telefone: {contato2.telefone}" in output

def test_exibir_contatos_lista_fazia():
    lista2 = Lista()
    
    with pytest.raises(ListaFazia) as exc_info:
        lista2.exibir_contatos()
    
    assert isinstance(exc_info.value, ListaFazia)


