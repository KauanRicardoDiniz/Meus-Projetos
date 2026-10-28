#Desenvolva um programa que peça ao utilizador dois números inteiros, representando a largura e a altura de um retângulo, e um símbolo em formato de string (como um '*').
#Utilizando laços de repetição aninhados (um for para controlar as linhas e outro for no seu interior para as colunas), o programa deverá desenhar a forma no terminal.
largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))
simbolo = input("Digite um simbolo para desenhar: ")
for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print(simbolo, end="")
        else:
            print(" ", end="")
    print()