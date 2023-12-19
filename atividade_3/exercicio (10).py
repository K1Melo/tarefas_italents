# Cria uma lista para armazenar os dicionários das pessoas
pessoas = []

# Variáveis para calcular a média de idade
soma_idade = 0
total_pessoas = 0

# Lista para armazenar as mulheres cadastradas
mulheres = []

# Lista para armazenar as idades acima da média
idades_acima_media = []

while True:
    # Solicita as informações da pessoa
    nome = input("Digite o nome da pessoa: ")
    sexo = input("Digite o sexo biológico da pessoa (M/F): ")
    idade = int(input("Digite a idade da pessoa: "))

    # Verifica se o sexo digitado é válido
    if sexo.upper() not in ["M", "F"]:
        print("Sexo biológico inválido. Digite M para masculino ou F para feminino.")
        continue

    # Cria o dicionário para armazenar as informações da pessoa
    pessoa = {
        "Nome": nome,
        "Sexo": sexo,
        "Idade": idade
    }

    # Adiciona o dicionário na lista de pessoas
    pessoas.append(pessoa)

    # Atualiza as variáveis para o cálculo da média de idade
    soma_idade += idade
    total_pessoas += 1

    # Verifica se a pessoa é do sexo feminino e adiciona na lista de mulheres
    if sexo.upper() == "F":
        mulheres.append(nome)

    # Pergunta ao usuário se deseja continuar cadastrando pessoas
    resposta = input("Deseja continuar cadastrando pessoas? (sim/não): ")
    if resposta.lower() != "sim":
        break

# Verifica se há pessoas cadastradas
if total_pessoas > 0:
    # Calcula a média de idade
    media_idade = soma_idade / total_pessoas

    # Verifica as idades acima da média
    for pessoa in pessoas:
        if pessoa["Idade"] > media_idade:
            idades_acima_media.append(pessoa["Idade"])

    # Exibe as informações
    print("Total de pessoas cadastradas:", total_pessoas)
    print("Média de idade das pessoas:", media_idade)
    print("Mulheres cadastradas:", mulheres)
    print("Idades acima da média:", idades_acima_media)
else:
    print("Nenhuma pessoa cadastrada.")