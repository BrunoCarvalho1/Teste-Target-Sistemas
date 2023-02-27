def calcular_percentual(faturamentos):

    faturamento_total = sum(faturamentos.values())
    
    percentuais = {estado: faturamento/faturamento_total*100 for estado, faturamento in faturamentos.items()}
    
    return percentuais

faturamentos = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
percentuais = calcular_percentual(faturamentos)
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
