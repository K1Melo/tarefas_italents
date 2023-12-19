# Cria um dicionário vazio para armazenar os dados dos alunos
alunos = {}

# Solicita ao usuário o nome e a média do aluno
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

# Verifica a situação do aluno
situacao = ""
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Armazena os dados do aluno no dicionário
alunos[nome] = {
    "Média": media,
    "Situação": situacao
}

# Exibe o conteúdo do dicionário na tela
print("Dados dos alunos:")
for nome, dados in alunos.items():
    print(f"Aluno: {nome}")
    print(f"Média: {dados['Média']}")
    print(f"Situação: {dados['Situação']}")
    print()
