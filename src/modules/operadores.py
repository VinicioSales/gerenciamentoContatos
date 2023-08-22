from errors.UsuarioJaCadastrado import UsuarioJaCadastrado
from errors.error_handler import error_handler

def adicionar_usuario(nome: str, telefone: str):
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = arquivo.read()
        if nome in usuarios.keys():
            raise UsuarioJaCadastrado(nome=nome)
    except Exception as exception:
        error_handler(exception=exception)
        

