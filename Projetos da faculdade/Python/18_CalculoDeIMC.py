altura = float(input("Qual a sua altura? "))
peso = float(input("Quanto você pesa? "))
imc = peso / altura ** 2
if imc < 17:
    print("Está muito abaixo do peso.")
elif imc >= 17 and imc < 18.5:
    print("Está abaixo do peso.")
elif imc >= 18.5 and imc < 25 :
    print("Peso normal.")
elif imc >= 25 and imc < 30:
    print("Está acima do peso.")
elif imc >= 30 and imc < 35:
    print("Está com obesidade.")
elif imc >= 35 and imc < 40:
    print("Está com obesidade severa.")
elif imc >= 40:
    print("Está com obesidade morbida.")