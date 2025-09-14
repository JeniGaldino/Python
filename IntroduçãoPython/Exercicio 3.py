'''''
dist = float(input("Digite a distância que deseja percorrer em KM\n"))

if dist <= 200 and dist > 0:
    price = dist * 0.50
    print("O preço da passagem é:", price,'\n')
elif dist >= 201:
    price2= dist * 0.35
    print("O preço da passagem é:",price2,'\n')
else:
    print("Valor inválido!")
'''''

salary = float(input("Digite seu salário:"))

if salary > 1250:
    inc = salary * 0.1
    total = salary + inc
    print("Seu salário foi para: ", total, 'O aumento foi de: ', inc)
else:
    inc = salary * 0.15
    total = salary + inc
    print("Seu salário foi para: ", total, 'O aumento foi de: ', inc)