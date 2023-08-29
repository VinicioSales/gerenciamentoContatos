from time import sleep
from modules.Lista import Lista
from modules.Contato import Contato

lista = Lista()

print("-- Gerenciamento de Contatos --")
print("\n")

while True:
    print("1. Adicionar Contato")
    print("2. Exibir Contatos")
    print("3. Pesquisar por Nome")
    print("4. Sair")
    print("\n")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Número de telefone: ")
        contato = Contato(nome=nome, telefone=telefone)
        try:
            lista.adicionar_contato(contato=contato)
            print("Contato adicionado com sucesso!")
            print("\n")
        except Exception as erro:
            print(f"Erro: {erro}")
        sleep(2)

    if opcao == "2":
        print("-- Lista de Contatos --")
        try:
            lista.exibir_contatos()
        except Exception as erro:
            print(f"Erro: {erro}")
        print("\n")
        sleep(2)

    if opcao == "3":
        nome = input("Digite o nome a ser pesquisado: ")
        print("-- Resultados da Pesquisa --")
        try:
            lista.pesquisar_contato(nome=nome)
        except Exception as erro:
            print(f"Erro: {erro}")
        print("\n")
        sleep(2)

    if opcao == "4":
        print("Encerrando o programa...")
        print("\n")
        sleep(2)
        break



