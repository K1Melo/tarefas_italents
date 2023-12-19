# Cria a matriz com informações dos clientes
clientes = [
    ["Fulano", 20],
    ["Fulana", 17],
    ["Ciclano", 25],
    ["Beltrano", 16],
    ["Maria", 18]
]

# Inicializa as variáveis de contagem
maiores_idade = 0
menores_idade = 0

# Verifica a idade de cada cliente
for cliente in clientes:
    nome = cliente[0]
    idade = cliente[1]
    
    if idade >= 18:
        print(f"{nome} é maior de idade")
        maiores_idade += 1
    else:
        print(f"{nome} é menor de idade")
        menores_idade += 1

# Exibe a quantidade de clientes maiores e menores de idade
print(f"Quantidade de clientes maiores de idade: {maiores_idade}")
print(f"Quantidade de clientes menores de idade: {menores_idade}")
