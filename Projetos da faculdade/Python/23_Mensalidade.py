mensalidade = 400
irmaos = int(input("Quantos irmãos/irmãs estão matriculados? "))

if irmaos == 0:
    print("Não tem desconto. A mensalidade é R${:.2f}".format(mensalidade))
elif irmaos < 2:
    print("O desconto é de 5%. A mensalidade è R${:.2f}".format(mensalidade * 0.95))
elif irmaos < 3:
    print("O desconto é de 10%. A mensalidade é R${:.2f}".format(mensalidade * 0.90))
else:
    print("O desconto é de 15%. A mensalidade é R${:.2f}".format(mensalidade * 0.85))