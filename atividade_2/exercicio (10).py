import random

numero_aleatorio = random.randint(0, 10)

numero_usuario = int(input("Digite um número inteiro entre 0 e 10: "))

print("Número escolhido pelo computador:", numero_aleatorio)

if numero_usuario == numero_aleatorio:
    print("Parabéns! Você acertou!")
else:
    print("Você errou. O número correto era", numero_aleatorio)