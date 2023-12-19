# Cria três listas vazias para armazenar os números digitados pelo usuário
numeros = []
pares = []
impares = []

# Faz a leitura dos números digitados pelo usuário
while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    
    # Verifica se o usuário deseja encerrar o programa
    if numero.lower() == 'sair':
        break
    
    # Converte o número para o tipo inteiro
    numero = int(numero)
    
    # Adiciona o número à lista de números
    numeros.append(numero)
    
    # Verifica se o número é par ou ímpar e adiciona à lista correspondente
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibe o conteúdo das três listas
print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)