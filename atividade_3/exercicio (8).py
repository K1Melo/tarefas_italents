# Dicionário de estoque
estoque = {
    "arroz": 10,
    "feijão": 20,
    "macarrão": 15,
    "leite": 5,
    "pão": 8
}

# Variável para armazenar o valor total da compra
valor_total = 0

# Variável para contar a quantidade de itens comprados
quantidade_itens = 0

# Loop para realizar as vendas
while True:
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    
    if produto.lower() == "sair":
        break
    
    if produto.lower() not in estoque:
        print("Produto inválido.")
        continue
    
    quantidade = int(input("Digite a quantidade desejada: "))
    
    if quantidade <= 0:
        print("Quantidade inválida.")
        continue
    
    if quantidade > estoque[produto.lower()]:
        print("Quantidade indisponível no estoque.")
        continue
    
    # Atualiza o estoque
    estoque[produto.lower()] -= quantidade
    
    # Atualiza o valor total da compra
    valor_total += quantidade
    
    # Atualiza a quantidade de itens comprados
    quantidade_itens += 1

# Exibe o resumo da compra
print("Resumo da compra:")
print(f"Quantidade de itens comprados: {quantidade_itens}")
print(f"Valor total da compra: R${valor_total:.2f}")
