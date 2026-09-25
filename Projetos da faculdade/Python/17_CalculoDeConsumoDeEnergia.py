kwh = float(input("Qual o consumo de KWh? "))
instalação = str(input("Qual o tipo de instalação? R(Residencial), I(Industrias), C(Comercios) ")).upper()
if instalação == "R":
    if kwh <= 500:
        preço = kwh * 0.40
    else:
        preço = kwh * 0.65
elif instalação == "I":
    if kwh <= 5000:
        preço = kwh * 0.55
    else:
        preço = kwh * 0.60
elif instalação == "C":
    if kwh <= 1000:
        preço = kwh * 0.55
    else:
        preço = kwh * 0.60
print("Você deve pagar R${} de consumo".format(preço))