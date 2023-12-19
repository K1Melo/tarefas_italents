cotacoes = {
    'USD': 4.5,   # Cotação do dólar americano
    'EUR': 5.2,   # Cotação do euro
    'GBP': 6.0,   # Cotação da libra esterlina
    'CAD': 3.4,   # Cotação do dólar canadense
    'ARS': 0.05,  # Cotação do peso argentino
    'CLP': 0.006  # Cotação do peso chileno
}

valor_reais = float(input("Digite o valor em reais (R$): "))

# Conversão para outras moedas
valor_dolar = valor_reais / cotacoes['USD']
valor_euro = valor_reais / cotacoes['EUR']
valor_libra = valor_reais / cotacoes['GBP']
valor_dolar_canadense = valor_reais / cotacoes['CAD']
valor_peso_argentino = valor_reais / cotacoes['ARS']
valor_peso_chileno = valor_reais / cotacoes['CLP']

# Exibição dos resultados
print(f"Valor em dólar americano (USD): U${valor_dolar:.2f}")
print(f"Valor em euro (EUR): €{valor_euro:.2f}")
print(f"Valor em libra esterlina (GBP): £{valor_libra:.2f}")
print(f"Valor em dólar canadense (CAD): C${valor_dolar_canadense:.2f}")
print(f"Valor em peso argentino (ARS): ARS {valor_peso_argentino:.2f}")
print(f"Valor em peso chileno (CLP): CLP {valor_peso_chileno:.2f}")