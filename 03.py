def analisa_faturamento(faturamento_diario):

  media_mensal = sum(faturamento_diario) / len(faturamento_diario)

  menor_valor = min(faturamento_diario)
  maior_valor = max(faturamento_diario)

  dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

  return menor_valor, maior_valor, dias_acima_media

faturamento = [1000, 1500, 800, 2000, 1200]
menor, maior, dias_acima = analisa_faturamento(faturamento)

print(f"Menor valor de faturamento: R$ {menor}")
print(f"Maior valor de faturamento: R$ {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")