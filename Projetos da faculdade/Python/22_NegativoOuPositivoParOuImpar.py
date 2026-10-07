num = int(input("Digite um numero: "))

if num < 0:
    print("NEGATIVO")
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
elif num > 0:
    print("POSITIVO")
    if num % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
else:
    print("NULO")