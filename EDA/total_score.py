def calcular_score_total(df):
    """
    Calcula o score total de crédito com base em médias ponderadas dos setores.
    Requer colunas *_score já calculadas.
    """
    pesos_setores = {
        'liquidez': 0.15,
        'alavancagem': 0.15,
        'rentabilidade': 0.20,
        'retornos': 0.15,
        'caixa': 0.20,
        'eficiencia': 0.15
    }

    setores = {
        'liquidez': [
            'liquidez_corrente_score', 'liquidez_seca_score'
        ],
        'alavancagem': [
            'endividamento_total_score', 'divida_patrimonio_score'
        ],
        'rentabilidade': [
            'margem_bruta_score', 'margem_operacional_score',
            'margem_liquida_score', 'margem_ebitda_score'
        ],
        'retornos': [
            'roa_score', 'roe_score'
        ],
        'caixa': [
            'fco_divida_score', 'fcf_divida_score',
            'cobertura_juros_score', 'ebitda_divida_score'
        ],
        'eficiencia': [
            'giro_ativos_score', 'ciclo_estoques_score',
            'ciclo_recebiveis_score', 'ciclo_pagamentos_score'
        ]
    }

    df = df.copy()
    for setor, colunas in setores.items():
        df[f'{setor}_media'] = df[colunas].mean(axis=1)

    df['score_total'] = sum(
        df[f'{setor}_media'] * peso for setor, peso in pesos_setores.items()
    )

    return df
