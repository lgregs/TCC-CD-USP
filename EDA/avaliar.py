def avaliar_indicadores_financeiros(df):
    """
    Aplica uma avaliação de 0 a 5 para indicadores financeiros, com base em parâmetros econômicos teóricos.
    Retorna um novo DataFrame com colunas *_score para cada indicador avaliado.
    """
    import numpy as np

    # Dicionário com os thresholds por indicador
    score_thresholds = {
        'liquidez_corrente': [0.8, 1.0, 1.5, 2.0, 3.0],
        'liquidez_seca':     [0.5, 0.8, 1.0, 1.5, 2.0],
        'endividamento_total': [0.5, 0.8, 1.0, 1.2, 1.5],
        'divida_patrimonio':   [0.5, 1.0, 1.5, 2.0, 2.5],
        'margem_bruta':        [0.10, 0.20, 0.30, 0.40, 0.50],
        'margem_operacional':  [0.05, 0.10, 0.15, 0.25, 0.35],
        'margem_ebitda':       [0.08, 0.15, 0.25, 0.35, 0.45],
        'margem_liquida':      [0.03, 0.08, 0.15, 0.25, 0.35],
        'roa':                 [0.02, 0.05, 0.10, 0.15, 0.20],
        'roe':                 [0.05, 0.10, 0.15, 0.25, 0.35],
        'fco_divida':          [0.10, 0.25, 0.40, 0.60, 0.80],
        'fcf_divida':          [0.10, 0.25, 0.40, 0.60, 0.80],
        'cobertura_juros':     [1.0, 2.0, 3.0, 5.0, 8.0],
        'ebitda_divida':       [0.5, 1.0, 1.5, 2.0, 2.5],
        'giro_ativos':         [0.5, 1.0, 1.5, 2.0, 3.0],
        'ciclo_estoques':      [120, 90, 60, 30, 15],  # invertido
        'ciclo_recebiveis':    [90, 60, 30, 15, 7],
        'ciclo_pagamentos':    [15, 30, 45, 60, 90]
    }

    def score_interval(value, bins):
        if value <= bins[0]: return 0
        elif value <= bins[1]: return 1
        elif value <= bins[2]: return 2
        elif value <= bins[3]: return 3
        elif value <= bins[4]: return 4
        else: return 5

    df_scored = df.copy()

    for col, bins in score_thresholds.items():
        if col in df_scored.columns:
            if 'ciclo' in col:
                df_scored[col + '_score'] = df_scored[col].apply(lambda v: 5 - score_interval(v, sorted(bins, reverse=True)))
            else:
                df_scored[col + '_score'] = df_scored[col].apply(lambda v: score_interval(v, bins))

    df_scored.replace([np.inf, -np.inf], np.nan, inplace=True)

    return df_scored