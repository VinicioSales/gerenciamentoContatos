class ListaFazia(Exception):

    def __init__(self):
        mensagem = "A lista está vazia!"
        super().__init__(mensagem)
        self.mensagem = mensagem
