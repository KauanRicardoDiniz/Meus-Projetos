#Crie um programa em Python que exiba a tabuada de multiplicação para os números de 1 a 9. Para cada um desses números, a tabuada deve mostrar a multiplicação dele pelos números de 1 a 9.
for i in range(1, 10):
    print(f"Tabuada do {i}")
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")