#Escreva um programa que receba uma string e conte quantas vogais há nessa string. Utilize o laço de repetição while.
frase = input("Digite qualquer coisa que não seja número: ").lower()
count = 0
i = 0
while i < len(frase):
    if frase[i] in "aeiou":
        count += 1
    i += 1
print(f"Sua frase tem {count} vogais.")