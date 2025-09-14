names = []
with open("dados/namex.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names): #ordem alfabética da lista
    print(f"Olá, {name}")