"""
Contagem Regressiva

Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

Tabuada

Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""
""""
for cont in range(10,-1,-1): #dentro do range primeiro item: começa com. segundo item: termina com. terceiro: Decrementa ou incrementa
    print(cont)
    if cont == 0:
        winsound.Beep(2500, 500)
"""


""""
print("======= Tabuada ==========")
while True:  # Loop infinito até o usuário decidir sair
    saida = input("Insira 's' para sair, ou qualquer outra tecla para continuar: ")
    if saida == 's':  
        break  # Sai do loop
    
    ini = int(input("Insira o primeiro valor: "))
    fin = int(input("Insira o segundo valor: "))
    total = ini * fin
    print(f"O resultado da multiplicação é: {total}")
"""
""""
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1
"""
"""
x = 10
while x >= 0:
    print(x)
    x = x - 1
winsound.Beep(2500, 500)
"""