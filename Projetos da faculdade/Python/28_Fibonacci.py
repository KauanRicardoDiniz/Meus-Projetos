n = int(input("Quantos termos você quer mostrar? "))
t1, t2 = 0, 1
contador = 0

print(f"{t1} -> {t2}", end="")
while contador < n - 2:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    contador += 1
print(" -> Fim")