""""
Conta letras maiúsculas e minúsculas

Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

Lista números pares e ímpares de uma lista

Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""
"""""
def contar_letras(string):
    # Inicializando contadores
    maiusculas = 0
    minusculas = 0

    # Percorrendo cada caractere na string
    for char in string:
        if char.isupper():  # Verifica se é letra maiúscula
            maiusculas += 1
        elif char.islower():  # Verifica se é letra minúscula
            minusculas += 1

    # Retorna ou imprime os resultados
    print(f"Letras maiúsculas: {maiusculas}")
    print(f"Letras minúsculas: {minusculas}")

# Exemplo de uso
contar_letras("Olá Mundo!")
"""

def contar_pares_impares(*num):
    par = []
    impar = []
    
    for n in num:  
        if n % 2 == 0:  
            par.append(n)  
        else:
            impar.append(n)  
    
    print("Números pares:", par)
    print("Números ímpares:", impar)


contar_pares_impares(1, 2, 3, 4, 5, 6, 7, 8)

    