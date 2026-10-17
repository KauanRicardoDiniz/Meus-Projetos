sal = float(input("Digite seu salário: "))
dep = int(input("Quantos dependentes você tem ? "))

if sal <= 2000:
    print("Seu salário bruto é R$ {:.2f} e você está insento de imposto!".format(sal))
elif sal <= 3500:
    if dep >= 3:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 6%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.06) - sal, sal * 0.94))
    else:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 8%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.08) - sal, sal * 0.92))
elif sal <= 5000:
    if dep >= 3:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 10%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.10) - sal, sal * 0.90))
    else:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 12%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.12) - sal, sal * 0.88))
else:
    if dep >= 3:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 16%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.16) - sal, sal * 0.84))
    else:
        print("Seu salário bruto é R$ {:.2f}, será aplicado 18%, são R$ {:.2f} de imposto, o salario fica R$ {:.2f}".format(sal, (sal * 1.18) - sal, sal * 0.82))