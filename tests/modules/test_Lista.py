import pytest
from src.modules.Lista import Lista
from src.modules.Contato import Contato
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


