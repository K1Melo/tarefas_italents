# Cria uma lista vazia para armazenar os valores únicos
valores_unicos = []

# Faz a leitura dos valores digitados pelo usuário
while True:
    valor = input("Digite um valor numérico (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja encerrar o programa
    if valor.lower() == 'sair':
        break
    
    # Converte o valor para o tipo numérico
    valor = int(valor)
    
    # Verifica se o valor já foi digitado anteriormente
    if valor not in valores_unicos:
        valores_unicos.append(valor)

# Ordena os valores únicos em ordem crescente
valores_unicos.sort()

# Exibe os valores únicos em ordem crescente
print("Valores únicos em ordem crescente:", valores_unicos)