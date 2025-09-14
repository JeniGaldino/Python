import random

def sorteio():
    lista = [1,2,3,4,5,6,7,8,9,10]
    num = int(input("Digite o número:\n"))
    ran = random.choice(lista)
    if num == ran:
        print(f"Você acertou!")
    else:
        print(f"Você errou! Número sorteado: {ran}")

def menu():
    while True:
        print("====Tente adivinhar o número====")
        print("1. Escolha um número")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            sorteio()   
        elif opcao == "2":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
menu()