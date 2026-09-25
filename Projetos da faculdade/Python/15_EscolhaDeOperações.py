n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro: "))
operação = str(input("Qual operação deseja realizar? (+, -, *, /) "))
if operação == "+":
    print("A soma de {} e {} é {}".format(n1, n2, n1 + n2))
elif operação == "-":
    print("A subtração de {} e {} é {}".format(n1, n2, n1 - n2))
elif operação == "*":
    print("A multiplicação de {} e {} é {}".format(n1, n2, n1 * n2))
elif operação == "/":
    print("A divisão de {} e {} é {:.2f}".format(n1, n2, n1 / n2))