# Você é um professor e precisa calcular a média das notas de um projeto para uma turma de 5 alunos. No entanto, alguns alunos faltaram no dia da apresentação e, no seu sistema, a nota para um aluno ausente é registrada como um número negativo (ex: -1). Esses alunos ausentes não devem ser considerados no cálculo da média.
#Escrever um programa em Python que peça a nota de 5 alunos, uma por uma. O programa deve somar apenas as notas válidas (maiores ou iguais a zero) e, ao final, calcular a média correta considerando apenas os alunos que tiveram uma nota válida.
s = 0
count = 0
for c in range(1,6):
    notas = int(input(f"Digte a nota do {c}º aluno: "))
    if notas >= 0:
        s += notas
        count += 1
if count > 0:
    media = s / count
    print(f"Média das notas válidas: {media:.2f}")
else:
    print("Não há notas válidas.")