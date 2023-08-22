from src.modules.Contato import Contato

contato1 = Contato(nome="Amanda", telefone="Telefone Amanda")

def test_instaciar_contato():
    contato = Contato(nome="Amanda", telefone="Telefone Amanda")

    assert contato.nome == "Amanda"
    assert contato.telefone == "Telefone Amanda"

def test_get_nome():
    nome = contato1.get_nome()

    assert nome == "Amanda"

def test_get_telefone():
    telefone = contato1.get_telefone()

    assert telefone == "Telefone Amanda"

