""""
frutas = ["maçã", "banana", "uva", "pera"]

for i, lines in enumerate(frutas, start=1):
    print(i,"-",lines)
"""
""""
word = "Python"

for i, letter in enumerate(word, start=0):
    print(i,":",letter)
"""
"""
with open("teste GPT/lista.txt", "r", encoding="UTF-8") as file:
    for i, lines in enumerate(file, start=1):
        print(lines.rstrip())
        if i == 3:
            break
"""
""""
with open("teste GPT/lista.txt", "r", encoding="UTF-8") as file:
    for i, lines in enumerate(file, start=1):
        if i % 2 == 0:
            print(i,"-",lines.rstrip())
"""
animais = ["gato", "cachorro", "coelho"]

for i, bichos in enumerate(animais, start=1):
    print(len(animais) - i + 1, "-", bichos)
        