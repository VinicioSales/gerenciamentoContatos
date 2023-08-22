import sys
import pytest
from io import StringIO
from src.modules.Lista import Lista
from src.modules.Contato import Contato
from src.errors.ListaFazia import ListaFazia
from src.errors.UsuarioJaCadastrado import UsuarioJaCadastrado
from src.errors.ContatoNaoEncontrado import ContatoNaoEncontrado


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

def test_pesquisar_contato():
    lista3 = Lista()
    contato1 = Contato(nome="Vinício", telefone="Telefone Vinício")
    contato2 = Contato(nome="Victor", telefone="Telefone Victor")
    lista3.adicionar_contato(contato=contato1)
    lista3.adicionar_contato(contato=contato2)

    pegar_output = StringIO()
    sys.stdout = pegar_output

    lista3.pesquisar_contato(nome="v")

    sys.stdout = sys.__stdout__

    output = pegar_output.getvalue()

    assert f"Nome: {contato1.nome} Telefone: {contato1.telefone}" in output
    assert f"Nome: {contato2.nome} Telefone: {contato2.telefone}" in output

def test_pesquisar_contato_lista_vazia():
    lista2 = Lista()
    
    with pytest.raises(ListaFazia) as exc_info:
        lista2.pesquisar_contato(nome="v")
    
    assert isinstance(exc_info.value, ListaFazia)

def test_pesquisar_contato_contato_nao_encontrado():
    lista3 = Lista()
    contato1 = Contato(nome="Vinício", telefone="Telefone Vinício")
    lista3.adicionar_contato(contato=contato1)

    with pytest.raises(ContatoNaoEncontrado) as exc_info:
        lista3.pesquisar_contato(nome="asddf")

    assert isinstance(exc_info.value, ContatoNaoEncontrado)
