
print('======Antecessor e Sucessor de um número=====')

number = int(input('Insira um número:'))

number -= 1
print('Número Antecessor:',number)
number += 2
print('Número Sucessor:',number)


print('=====Média de 4 Notas======\n')

pt=float(input("Insira a nota de Português: "))
mat=float(input("Insira a nota de Matemática: "))
cie=float(input("Insira a nota de Ciências: "))
his=float(input("Insira a nota de História: "))

media= (pt+mat+cie+his)/4

print('Sua média é: ', media)