class ContatoNaoEncontrado(Exception):

    def __init__(self, nome: str):
        mensagem = f"Contato não encontrado com o nome: {nome}"
        super().__init__(mensagem)
        self.mensagem = mensagem
