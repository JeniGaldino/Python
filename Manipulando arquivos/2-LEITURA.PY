"""
with open ("namex.txt", "r") as file:
    for line in file:
        print(f"Olá {line}")
"""
with open("dados/namex.txt", "a", encoding="UTF-8") as file2: #ENCONDING PARA CARCTERES ESPECIAIS
    name = input("Digite um nome\n")
    file2.write(name)
with open("dados/namex.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(f"Olá {line.rstrip()}") #rstrip remove espaço
        
