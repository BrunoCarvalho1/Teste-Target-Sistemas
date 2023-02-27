def calcular_faturamento(vetor_faturamento):

    faturamentos_validos = [faturamento for faturamento in vetor_faturamento if faturamento is not None]
    menor_faturamento = faturamentos_validos[0]
    maior_faturamento = faturamentos_validos[0]
    soma_faturamento = faturamentos_validos[0]
    media_faturamento = 0.0
    
    for faturamento in vetor_faturamento[1:]:
        if faturamento is not None:
            if faturamento < menor_faturamento:
                menor_faturamento = faturamento
            if faturamento > maior_faturamento:
                maior_faturamento = faturamento
            soma_faturamento += faturamento
    

    media_faturamento = soma_faturamento / len(faturamentos_validos)
    

    dias_acima_da_media = sum(faturamento > media_faturamento for faturamento in vetor_faturamento if faturamento is not None)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

vetor_faturamento = [1000, 2000, 1500, None, 1800, 1200, None, 1600, 1900, 2200]
menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(vetor_faturamento)
print(f'Menor faturamento: {menor_faturamento}')
print(f'Maior faturamento: {maior_faturamento}')
print(f'Dias acima da média: {dias_acima_da_media}')
