# Solicita as informações do usuário
nome = input("Digite o nome do funcionário: ")
ano_nascimento = int(input("Digite o ano de nascimento do funcionário: "))
ctps = int(input("Digite o número da carteira de trabalho (CTPS): "))

# Cria o dicionário para armazenar as informações
funcionario = {
    "Nome": nome,
    "Ano de Nascimento": ano_nascimento,
    "CTPS": ctps
}

# Verifica se a CTPS é diferente de zero
if ctps != 0:
    ano_contratacao = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o salário do funcionário: "))
    
    # Calcula a idade do funcionário
    idade = 2023 - ano_nascimento
    
    # Calcula a idade de aposentadoria
    idade_aposentadoria = idade + 35
    
    # Adiciona as informações de trabalho no dicionário
    funcionario["Ano de Contratação"] = ano_contratacao
    funcionario["Salário"] = salario
    funcionario["Idade"] = idade
    funcionario["Idade de Aposentadoria"] = idade_aposentadoria

# Exibe o conteúdo completo do dicionário
print("Dados do funcionário:")
for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")