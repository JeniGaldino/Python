name = input("Digite o seu nome\n")

file = open("namex.txt", "a")
file.write(f"{name}\n")
file.close()


#ouuu

with open("names.txt", "a") as file:
    file.write(f"{name}\n")