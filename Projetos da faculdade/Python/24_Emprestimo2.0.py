salario = float(input("Digite seu salario: "))
emprestimo = float(input("Quanto de emprestimo você deseja? R$"))
meses = int(input("Em quantos meses vocé quer pagar? "))
prestacao = emprestimo / meses

if emprestimo >= salario * 10 or prestacao > salario * 1.30 or meses < 6 or meses > 48:
    print("EMPRESTIMO REPROVADO!")
else:
    print("EMPRESTIMO APROVADO! A prestacao fica R${:.2f} de {} vezes.".format(prestacao, meses))