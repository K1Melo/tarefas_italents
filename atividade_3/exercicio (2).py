# Inicializa a variável contador de respostas positivas
respostas_positivas = 0

# Faz as 5 perguntas ao usuário
pergunta1 = input("Você telefonou para a vítima? (s/n): ")
if pergunta1.lower() == 's':
    respostas_positivas += 1

pergunta2 = input("Esteve no local do crime? (s/n): ")
if pergunta2.lower() == 's':
    respostas_positivas += 1

pergunta3 = input("Mora perto da vítima? (s/n): ")
if pergunta3.lower() == 's':
    respostas_positivas += 1

pergunta4 = input("Devia para a vítima? (s/n): ")
if pergunta4.lower() == 's':
    respostas_positivas += 1

pergunta5 = input("Já trabalhou com a vítima? (s/n): ")
if pergunta5.lower() == 's':
    respostas_positivas += 1

# Classifica a possível participação do usuário no crime
if respostas_positivas == 2:
    print("Você é classificado como SUSPEITO.")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("Você é classificado como CÚMPLICE.")
elif respostas_positivas == 5:
    print("Você é classificado como ASSASSINO.")
else:
    print("Você é classificado como INOCENTE.")
