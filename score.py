import pandas as pd
import numpy as np

def score_financial_ratios(df):
    """
    Aplica um sistema de pontuação baseado em thresholds financeiros para
    criar 20 novas colunas de 'score' e um 'total_score' (média).

    Args:
        df (pd.DataFrame): O DataFrame contendo os rácios já calculados.
                           DEVE conter 'ebitda_final' e outros rácios.

    Returns:
        pd.DataFrame: O DataFrame original com as novas colunas de pontuação.
    """
    # Cria uma cópia para evitar o SettingWithCopyWarning
    data = df.copy()

    # --- 0. Calcular Rácios de Rentabilidade ---
    # ** USA 'ebitda_final' (calculada no script principal) **
    
    '''
    required_for_ebitda = ['ebitda_final', 'receita_de_vendas', 'despesas_financeiras', 'dívidas_financeiras']
    for col in required_for_ebitda:
        if col not in data.columns:
            print(f"Aviso: A coluna {col} (necessária para rácios de EBITDA) não foi encontrada.")
            data[col] = np.nan 

    data['ebitda_margin'] = data['ebitda_final'] / data['receita_de_vendas']
    data['ebitda_to_interest'] = data['ebitda_final'] / data['despesas_financeiras']
    data['ebitda_to_debt'] = data['ebitda_final'] / data['dívidas_financeiras']
    '''

    # Substitui 'inf' e '-inf' por 'NaN' antes de preencher os NaNs
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # --- Pré-processamento: Tratar NaNs ---
    # Preenche com 0 ANTES de pontuar.
    ratios_to_score = [
        'ebitda_margin', 'ebitda_to_interest', 'ebitda_to_debt',
        'roe', 'roa', 'net_margin', 'operating_margin',
        'current_ratio', 'quick_ratio', 'debt_to_equity', 'debt_to_assets',
        'interest_coverage', 'retained_to_assets', 
        'asset_turnover', 'inventory_turnover', 'receivable_turnover', 
        'sales_growth', 'asset_growth', 'net_income_growth', 
        'fx_position_ratio'
    ]
    
    existing_ratios_to_score = [col for col in ratios_to_score if col in data.columns]
    data[existing_ratios_to_score] = data[existing_ratios_to_score].fillna(0)

    # --- 1. Pontuação: Lucratividade e Qualidade dos Ganhos ---

    # ebitda_margin: <0 = 0; 0–10% = 3; 10–20% = 7; >20% = 10
    conditions = [
        data['ebitda_margin'] < 0.0,
        data['ebitda_margin'] <= 0.10,
        data['ebitda_margin'] <= 0.20
    ]
    scores = [0, 3, 7]
    data['score_ebitda_margin'] = np.select(conditions, scores, default=10)

    # ebitda_to_interest: <1 = 0; 1–3 = 5; 3–5 = 7; >5 = 10
    conditions = [
        data['ebitda_to_interest'] < 1.0,
        data['ebitda_to_interest'] < 3.0,
        data['ebitda_to_interest'] <= 5.0
    ]
    scores = [0, 5, 7]
    data['score_ebitda_to_interest'] = np.select(conditions, scores, default=10)

    # ebitda_to_debt: <0.05 = 0; 0.05-0.1 = 5; 0.1-0.3 = 8; >0.3 = 10
    conditions = [
        data['ebitda_to_debt'] < 0.05,
        data['ebitda_to_debt'] < 0.1,
        data['ebitda_to_debt'] < 0.3,
        data['ebitda_to_debt'] <= 0.5 
    ]
    scores = [0, 5, 8, 8] # Faixa 0.3-0.5 recebe 8
    data['score_ebitda_to_debt'] = np.select(conditions, scores, default=10) # > 0.5 recebe 10

    # roe: <0 = 0; 0–10% = 5; 10–20% = 7; >20% = 10
    conditions = [
        data['roe'] < 0.0,
        data['roe'] <= 0.10,
        data['roe'] <= 0.20
    ]
    scores = [0, 5, 7]
    data['score_roe'] = np.select(conditions, scores, default=10)

    # roa: <0 = 0; 0–5% = 5; 5–10% = 8; >10% = 10
    conditions = [
        data['roa'] < 0.0,
        data['roa'] <= 0.05,
        data['roa'] <= 0.10
    ]
    scores = [0, 5, 8]
    data['score_roa'] = np.select(conditions, scores, default=10)

    # net_margin: <0 = 0; 0–5% = 5; 5–15% = 8; >15% = 10
    conditions = [
        data['net_margin'] < 0.0,
        data['net_margin'] <= 0.05,
        data['net_margin'] <= 0.15
    ]
    scores = [0, 5, 8]
    data['score_net_margin'] = np.select(conditions, scores, default=10)

    # operating_margin: <0 = 0; 0–10% = 5; 10–20% = 8; >20% = 10
    conditions = [
        data['operating_margin'] < 0.0,
        data['operating_margin'] <= 0.10,
        data['operating_margin'] <= 0.20
    ]
    scores = [0, 5, 8]
    data['score_operating_margin'] = np.select(conditions, scores, default=10)

    # --- 2. Pontuação: Liquidez & Solvência ---

    # current_ratio: <1 = 0; 1–1.5 = 5; 1.5–2.5 = 8; >2.5 = 10
    conditions = [
        data['current_ratio'] < 1.0,
        data['current_ratio'] < 1.5,
        data['current_ratio'] <= 2.5
    ]
    scores = [0, 5, 8]
    data['score_current_ratio'] = np.select(conditions, scores, default=10)

    # quick_ratio: <0.5 = 0; 0.5–1.0 = 5; 1–1.5 = 8; >1.5 = 10
    conditions = [
        data['quick_ratio'] < 0.5,
        data['quick_ratio'] < 1.0,
        data['quick_ratio'] <= 1.5
    ]
    scores = [0, 5, 8]
    data['score_quick_ratio'] = np.select(conditions, scores, default=10)

    # debt_to_equity: >3.0 = 0; 2–3 = 3; 1–2 = 6; <1 = 10 (Lógica invertida)
    conditions = [
        data['debt_to_equity'] > 3.0,
        data['debt_to_equity'] > 2.0,
        data['debt_to_equity'] > 1.0
    ]
    scores = [0, 3, 6]
    data['score_debt_to_equity'] = np.select(conditions, scores, default=10)

    # debt_to_assets: >0.8 = 0; 0.6–0.8 = 3; 0.4–0.6 = 6; <0.4 = 10 (Lógica invertida)
    conditions = [
        data['debt_to_assets'] > 0.8,
        data['debt_to_assets'] > 0.6,
        data['debt_to_assets'] > 0.4
    ]
    scores = [0, 3, 6]
    data['score_debt_to_assets'] = np.select(conditions, scores, default=10)

    # interest_coverage: <1 = 0; 1–3 = 5; 3–5 = 8; >5 = 10
    conditions = [
        data['interest_coverage'] < 1.0,
        data['interest_coverage'] < 3.0,
        data['interest_coverage'] <= 5.0
    ]
    scores = [0, 5, 8]
    data['score_interest_coverage'] = np.select(conditions, scores, default=10)

    # retained_to_assets: <0 = 0; 0–0.1 = 4; 0.1–0.3 = 8; >0.3 = 10
    conditions = [
        data['retained_to_assets'] < 0.0,
        data['retained_to_assets'] < 0.1,
        data['retained_to_assets'] <= 0.3
    ]
    scores = [0, 4, 8]
    data['score_retained_to_assets'] = np.select(conditions, scores, default=10)

    # --- 3. Pontuação: Eficiência (Gestão de Ativos) ---

    # asset_turnover: <0.3 = 0; 0.3–0.6 = 5; 0.6–1.0 = 8; >1.0 = 10
    conditions = [
        data['asset_turnover'] < 0.3,
        data['asset_turnover'] < 0.6,
        data['asset_turnover'] <= 1.0
    ]
    scores = [0, 5, 8]
    data['score_asset_turnover'] = np.select(conditions, scores, default=10)

    # inventory_turnover: <2 = 0; 2–4 = 5; 4–8 = 8; >8 = 10
    conditions = [
        data['inventory_turnover'] < 2.0,
        data['inventory_turnover'] < 4.0,
        data['inventory_turnover'] <= 8.0
    ]
    scores = [0, 5, 8]
    data['score_inventory_turnover'] = np.select(conditions, scores, default=10)

    # receivable_turnover: <2 = 0; 2–5 = 5; 5–10 = 8; >10 = 10
    conditions = [
        data['receivable_turnover'] < 2.0,
        data['receivable_turnover'] < 5.0,
        data['receivable_turnover'] <= 10.0
    ]
    scores = [0, 5, 8]
    data['score_receivable_turnover'] = np.select(conditions, scores, default=10)

    # --- 4. Pontuação: Métricas de Crescimento ---

    # sales_growth: <0 = 0; 0–5% = 4; 5–15% = 7; >15% = 10
    conditions = [
        data['sales_growth'] < 0.0,
        data['sales_growth'] <= 0.05,
        data['sales_growth'] <= 0.15
    ]
    scores = [0, 4, 7]
    data['score_sales_growth'] = np.select(conditions, scores, default=10)

    # asset_growth: <0 = 0; 0–5% = 4; 5–15% = 7; >15% = 10
    conditions = [
        data['asset_growth'] < 0.0,
        data['asset_growth'] <= 0.05,
        data['asset_growth'] <= 0.15
    ]
    scores = [0, 4, 7]
    data['score_asset_growth'] = np.select(conditions, scores, default=10)

    # net_income_growth: <0 = 0; 0–5% = 4; 5–20% = 8; >20% = 10
    conditions = [
        data['net_income_growth'] < 0.0,
        data['net_income_growth'] <= 0.05,
        data['net_income_growth'] <= 0.20
    ]
    scores = [0, 4, 8]
    data['score_net_income_growth'] = np.select(conditions, scores, default=10)

    # --- 5. Pontuação: Risco / Exposição Cambial ---
    # < -0.2 = 0; -0.1–0 = 5; 0–0.1 = 8; >0.1 = 10
    conditions = [
        data['fx_position_ratio'] < -0.2,
        data['fx_position_ratio'] <= 0.0,
        data['fx_position_ratio'] <= 0.1
    ]
    scores = [0, 5, 8]
    data['score_fx_position_ratio'] = np.select(conditions, scores, default=10)

    # --- 6. Criar Pontuação Total (Média Ponderada por Setor) ---
    
    # 6a. Definir as colunas de score para cada categoria (baseado na Metodologia)
    cols_rentabilidade = [
        'score_ebitda_margin', 'score_ebitda_to_interest', 'score_ebitda_to_debt',
        'score_roe', 'score_roa', 'score_net_margin', 'score_operating_margin'
    ] # 7 colunas
    
    cols_liquidez = [
        'score_current_ratio', 'score_quick_ratio', 'score_debt_to_equity',
        'score_debt_to_assets', 'score_interest_coverage', 'score_retained_to_assets'
    ] # 6 colunas
    
    cols_eficiencia = [
        'score_asset_turnover', 'score_inventory_turnover', 'score_receivable_turnover'
    ] # 3 colunas
    
    cols_crescimento = [
        'score_sales_growth', 'score_asset_growth', 'score_net_income_growth'
    ] # 3 colunas
    
    cols_fx = [
        'score_fx_position_ratio'
    ] # 1 coluna

    # 6b. Calcular a pontuação média para cada setor
    # .mean(axis=1) calcula a média de todas as colunas para cada linha (empresa-ano)
    score_setor_rentabilidade = data[cols_rentabilidade].mean(axis=1)
    score_setor_liquidez = data[cols_liquidez].mean(axis=1)
    score_setor_eficiencia = data[cols_eficiencia].mean(axis=1)
    score_setor_crescimento = data[cols_crescimento].mean(axis=1)
    score_setor_fx = data[cols_fx].mean(axis=1) # (é a própria coluna, mas .mean() é seguro)

    # 6c. Definir os pesos
    W_RENTABILIDADE = 0.30  # 30%
    W_LIQUIDEZ = 0.25       # 25%
    W_EFICIENCIA = 0.20     # 20%
    W_CRESCIMENTO = 0.10    # 10%
    W_FX = 0.15             # 15%
    # Total = 1.0 (100%)

    # 6d. Calcular o total_score ponderado
    data['total_score'] = (
        (score_setor_rentabilidade * W_RENTABILIDADE) +
        (score_setor_liquidez * W_LIQUIDEZ) +
        (score_setor_eficiencia * W_EFICIENCIA) +
        (score_setor_crescimento * W_CRESCIMENTO) +
        (score_setor_fx * W_FX)
    )

    return data

