def create_financial_ratios(df):
    """
    Calcula um conjunto abrangente de rácios financeiros com base no dataframe fornecido.

    A função lida corretamente com dados de séries temporais (como 'companycode' e 'ano')
    para calcular rácios de crescimento e limpa valores infinitos que podem resultar
    de divisão por zero, substituindo-os por NaN.

    Args:
        df (pd.DataFrame): O dataframe de entrada com as colunas financeiras necessárias.
                           Deve incluir 'companycode' e 'ano'.

    Returns:
        pd.DataFrame: Um novo dataframe com todas as colunas originais mais as
                      novas colunas de rácios calculados.
    """
    # Cria uma cópia para evitar modificar o dataframe original
    data = df.copy()

    # --- 1. Rácios de Liquidez ---
    data['current_ratio'] = data['ativos_circulantes'] / data['passivos_circulantes']
    
    quick_assets = (data['caixa_e_equivalentes_de_caixa'] + 
                    data['contas_a_receber'] + 
                    data['outros_ativos_circulantes'])
    data['quick_ratio'] = quick_assets / data['passivos_circulantes']

    # --- 2. Rácios de Alavancagem ---
    data['debt_to_equity'] = data['dívidas_financeiras'] / data['patrimônio_líquido']
    data['debt_to_assets'] = data['dívidas_financeiras'] / data['total_de_ativos']

    # --- 3. Rácios de Rentabilidade ---
    # Usando 'lucro_prejuízo_líquido_do_período' como "Lucro Líquido"
    # Usando 'lucro_prejuízo_operacional_líquido' como "Lucro Operacional"
    data['roe'] = data['lucro_prejuízo_líquido_do_período'] / data['patrimônio_líquido']
    data['roa'] = data['lucro_prejuízo_líquido_do_período'] / data['total_de_ativos']
    data['net_margin'] = data['lucro_prejuízo_líquido_do_período'] / data['receita_de_vendas']
    data['operating_margin'] = data['lucro_prejuízo_operacional_líquido'] / data['receita_de_vendas']

    # --- 4. Rácios de Eficiência ---
    data['asset_turnover'] = data['receita_de_vendas'] / data['total_de_ativos']
    data['inventory_turnover'] = data['cogs'] / data['estoques']
    data['receivable_turnover'] = data['receita_de_vendas'] / data['contas_a_receber']

    # --- 5. Rácio de Cobertura ---
    data['interest_coverage'] = data['lucro_prejuízo_operacional_líquido'] / data['despesas_financeiras']

    # --- 6. Solvência & Estabilidade ---
    data['retained_to_assets'] = data['lucros_prejuízos_acumulados'] / data['total_de_ativos']
    data['fx_position_ratio'] = data['posição_cambial_líquida'] / data['total_de_ativos']

    # --- 7. Rácios de Crescimento (Dependente de Série Temporal) ---
    # Devemos ordenar por empresa e ano para calcular a variação percentual corretamente.
    data = data.sort_values(by=['companycode', 'ano'])

    # .pct_change() calcula (atual - anterior) / anterior
    # Agrupado por empresa para evitar comparar 2010 da empresa A com 2009 da empresa B
    data['sales_growth'] = data.groupby('companycode')['receita_de_vendas'].pct_change()
    data['asset_growth'] = data.groupby('companycode')['total_de_ativos'].pct_change()
    data['net_income_growth'] = data.groupby('companycode')['lucro_prejuízo_líquido_do_período'].pct_change()

    # --- 8. Limpeza Final ---
    # Rácios podem criar valores infinitos (ex: 100 / 0).
    # Substituímos todos 'inf' e '-inf' por 'NaN' (Not a Number)
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    return data