emprestimo = float(input("Quanto de emprestimo você deseja ? "))
salario = float(input("Qual o seu salario ? R$"))
meses = int(input("Em quantos meses você quer pagar o emprestimo ? "))
prestação = emprestimo / meses
if salario * 1.30 < prestação:
    print("Emprestimo não aprovado.")
else:
    print("Emprestimo aprovado! Cada prestação fica R${:.2f} de {} vezes.".format(prestação, meses))