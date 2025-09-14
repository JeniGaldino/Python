""""
Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

Adicionar um time

Remover um time

Listar times

Adicionar jogador em um time

Remover jogador de um time

Listar jogadores de um time

A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.

A opção de adicionar um time deve pedir um nome para o time que será cadastrado.

A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.

A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.

A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.

A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.
"""
def adicionar_time(times):
    nome_time = input("Digite o nome do time que deseja adicionar: ")
    if nome_time in times:
        print("Esse time já existe!")
    else:
        times[nome_time] = []
        print(f"Time '{nome_time}' adicionado com sucesso!")

def remover_time(times):
    listar_times(times)
    escolha = int(input("Digite o número do time para remover: ")) - 1
    if escolha < 0 or escolha >= len(times):
        print("Índice inválido!")
    else:
        nome_time = list(times.keys())[escolha]
        del times[nome_time]
        print(f"Time '{nome_time}' removido com sucesso!")

def listar_times(times):
    if not times:
        print("Nenhum time cadastrado.")
    else:
        print("Times cadastrados:")
        for i, (nome, jogadores) in enumerate(times.items(), start=1):
            print(f"{i}. {nome} ({len(jogadores)} jogadores)")

def adicionar_jogador(times):
    listar_times(times)
    escolha = int(input("Digite o número do time para adicionar um jogador: ")) - 1
    if escolha < 0 or escolha >= len(times):
        print("Índice inválido!")
    else:
        nome_time = list(times.keys())[escolha]
        nome_jogador = input("Digite o nome do jogador: ")
        times[nome_time].append(nome_jogador)
        print(f"Jogador '{nome_jogador}' adicionado ao time '{nome_time}'.")

def remover_jogador(times):
    listar_times(times)
    escolha = int(input("Digite o número do time para remover um jogador: ")) - 1
    if escolha < 0 or escolha >= len(times):
        print("Índice inválido!")
    else:
        nome_time = list(times.keys())[escolha]
        if not times[nome_time]:
            print(f"O time '{nome_time}' não tem jogadores para remover.")
        else:
            for i, jogador in enumerate(times[nome_time], start=1):
                print(f"{i}. {jogador}")
            jogador_escolhido = int(input("Digite o número do jogador para remover: ")) - 1
            if jogador_escolhido < 0 or jogador_escolhido >= len(times[nome_time]):
                print("Índice inválido!")
            else:
                jogador_removido = times[nome_time].pop(jogador_escolhido)
                print(f"Jogador '{jogador_removido}' removido do time '{nome_time}'.")

def listar_jogadores(times):
    listar_times(times)
    escolha = int(input("Digite o número do time para listar os jogadores: ")) - 1
    if escolha < 0 or escolha >= len(times):
        print("Índice inválido!")
    else:
        nome_time = list(times.keys())[escolha]
        if not times[nome_time]:
            print(f"O time '{nome_time}' não tem jogadores.")
        else:
            print(f"Jogadores do time '{nome_time}':")
            for jogador in times[nome_time]:
                print(f"- {jogador}")

def menu():
    times = {}
    while True:
        print("\n=== Gerenciamento de Jogadores e Times ===")
        print("1. Adicionar time")
        print("2. Remover time")
        print("3. Listar times")
        print("4. Adicionar jogador em um time")
        print("5. Remover jogador de um time")
        print("6. Listar jogadores de um time")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_time(times)
        elif opcao == "2":
            remover_time(times)
        elif opcao == "3":
            listar_times(times)
        elif opcao == "4":
            adicionar_jogador(times)
        elif opcao == "5":
            remover_jogador(times)
        elif opcao == "6":
            listar_jogadores(times)
        elif opcao == "7":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")