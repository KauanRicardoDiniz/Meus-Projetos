nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if nota1 < 0 and nota2 < 0 and nota1 > 10 and nota2 > 10:
    print("NOTA INVÁLIDA")
elif media >= 7:
    print("APROVADO")
elif media >= 4:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")