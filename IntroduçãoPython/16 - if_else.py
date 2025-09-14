gamequantity = []  
quantidade = int(input("Quantos jogos você deseja cadastrar? "))  

for i in range(quantidade):
    print(f"\nCadastro do jogo {i + 1}:")
    name = input("Digite o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
    classification = float(input("Informe a nota de classificação do jogo: "))
    
    jogo = {
        "nome": name,
        "ano": yearLaunch,
        "classificação": classification
    }
    
    gamequantity.append(jogo)  
    
    # Avaliação do jogo com base na classificação
    if classification >= 8:
        print(f"O jogo {name} é bom. Recomendo jogá-lo.")
    elif 5 <= classification <= 7:
        print(f"O jogo {name} é razoável. Pode ser que goste ou odeie.")
    else:
        print(f"O jogo {name} ainda não atingiu uma boa nota, por isso não recomendo.")
    
