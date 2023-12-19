salario_atual = float(input("Digite o salário atual do colaborador: "))

percentual_aumento = 0
if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print("Salário antes do reajuste: R$", salario_atual)
print("Percentual de aumento aplicado:", percentual_aumento, "%")
print("Valor do aumento: R$", valor_aumento)
print("Novo salário após o reajuste: R$", novo_salario)