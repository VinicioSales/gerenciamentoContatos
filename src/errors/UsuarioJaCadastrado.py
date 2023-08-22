class UsuarioJaCadastrado(Exception):

    def __init__(self, nome):
        mensagem = f"Usuario já cadastrado com nome {nome}"
        super().__init__(mensagem)
        self.mensagem = mensagem
