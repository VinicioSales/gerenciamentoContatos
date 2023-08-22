class Contato:
    
    def __init__(self, nome: str, telefone: str):
        """Instancia um contato com nome e telefone."""
        self.nome = nome
        self.telefone = telefone
    
    def get_nome(self):
        """Retorna o nome do contato."""
        return self.nome
    
    def get_telefone(self):
        """Retorna o telefone do contato."""
        return self.telefone
    
    def __eq__(self, other):
        """Define igualdade de contatos com base em nome e telefone."""
        if isinstance(other, Contato):
            return self.nome == other.nome and self.telefone == other.telefone
        return False
