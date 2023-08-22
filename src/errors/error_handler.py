from .UsuarioJaCadastrado import UsuarioJaCadastrado

def error_handler(exception: Exception):
    if isinstance(exception, UsuarioJaCadastrado):
        raise("Usuario já Cadastrado")