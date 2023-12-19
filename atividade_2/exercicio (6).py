nota = float(input("Digite a nota do aluno: "))

if nota < 0.0 or nota > 10.0:
    print("Erro: Nota inválida. A nota deve estar entre 0.0 e 10.0.")
elif nota < 6.0:
    print("Nota F")
elif nota <= 7.0:
    print("Nota D")
elif nota <= 8.0:
    print("Nota C")
elif nota <= 9.0:
    print("Nota B")
else:
    print("Nota A")