frase = input("Digite uma frase: ").strip().upper()
palavra = frase.replace(" ", "")
inverso = "".join(reversed(palavra))
print(f"O inverso de {palavra} é {inverso}")
if palavra == inverso:
    print("A palavra digitada é um palindromo.")
else:
    print("A palavra digitada não é um palindromo.")