class Viagem:
    catalogo = []  

    def __init__(self, destino):
        self.destino = destino
        Viagem.catalogo.append(self)

    @classmethod
    def mostrar_opcoes(cls):
        print("Destinos disponíveis:")
        for i, viagem in enumerate(cls.catalogo, start=1):
            print(f"{i} - {viagem.destino}")


# Criando as viagens no catálogo
Viagem("Rio de Janeiro")
Viagem("Buenos Aires")
Viagem("Rio Branco")
Viagem("Brasília")
Viagem("Romênia")
Viagem("Berlim")
Viagem("Jamaica")
Viagem("Itália")

# Pedir nome
nome = input("Digite seu nome: ")
while nome == "":
    nome = input("Nome inválido. Digite novamente: ")

# Mostrar opções
Viagem.mostrar_opcoes()

# Escolher destino
escolha = int(input("Digite o número do destino desejado: "))
while escolha < 1 or escolha > len(Viagem.catalogo):
    escolha = int(input("Opção inválida. Digite novamente: "))

# Mensagem final
destino_escolhido = Viagem.catalogo[escolha - 1]
print(nome + ", sua viagem para " + destino_escolhido.destino + " foi cadastrada com sucesso!")