kwh = float(input("Qual o consumo em kWh? "))
tarifa = input("Qual a bandeira tarifaria ? (V verde, A amarela, R vermelha) ").upper()

if tarifa == "V":
    print("Bandeira verde não tem acréscimo.")
    if kwh <= 100:
        print("Vai pagar R${:.2f} de energia.".format(kwh * 0.60))
    elif kwh <= 200:
        print("Vai pagar R${:.2f} de energia.".format(kwh * 0.75))
    else:
        print("Vai pagar R${:.2f} de energia.".format(kwh * 0.90))
elif tarifa == "A":
    print("Bandeira amarela tem acréscimo de 5%.")
    if kwh <= 100:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.60) * 1.05))
    elif kwh <= 200:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.75) * 1.05))
    else:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.90) * 1.05))
elif tarifa == "R":
    print("Bandeira vermelha tem acréscimo de 10%.")
    if kwh <= 100:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.60) * 1.10))
    elif kwh <= 200:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.75) * 1.10))
    else:
        print("Vai pagar R${:.2f} de energia.".format((kwh * 0.90) * 1.10))
else:
    print("BANDEIRA INVÁLIDA")