def calcula_percentual_faturamento(dados_faturamento):

  faturamento_total = sum(dados_faturamento.values())

  percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in dados_faturamento.items()}

  return percentuais

dados = {
  'SP': 67836.43,
  'RJ': 36678.66,
  'MG': 29229.88,
  'ES': 27165.48,
  'Outros': 19849.53
}

resultados = calcula_percentual_faturamento(dados)
for estado, percentual in resultados.items():
  print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")