import json

def analisa_faturamento(arquivo_json):

  with open(arquivo_json, 'r') as f:
    dados = json.load(f)

  faturamento_diario = [valor for valor in dados['valores'] if valor > 0]

  media_mensal = sum(faturamento_diario) / len(faturamento_diario)

  menor_valor = min(faturamento_diario)
  maior_valor = max(faturamento_diario)

  dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

  return menor_valor, maior_valor, dias_acima_media

arquivo = 'faturamento.json'  # Substitua pelo nome do seu arquivo
menor, maior, dias_acima = analisa_faturamento(arquivo)

print(f"Menor valor de faturamento: R$ {menor}")
print(f"Maior valor de faturamento: R$ {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")