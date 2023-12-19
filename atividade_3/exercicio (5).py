import random

# Solicita a quantidade de jogos ao usuário
quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

# Cria uma matriz vazia para armazenar os jogos
jogos = []

# Gera os jogos aleatoriamente
for _ in range(quantidade_jogos):
    jogo = []
    
    # Sorteia 6 números entre 1 e 60
    for _ in range(6):
        numero = random.randint(1, 60)
        jogo.append(numero)
    
    # Adiciona o jogo à matriz
    jogos.append(jogo)

# Exibe os jogos gerados
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")