import numpy as np

def criar_indicadores_credito(df):

    df = df.copy()

    # Liquidez
    df['liquidez_corrente'] = df['ativos_circulantes'] / df['passivos_circulantes']
    df['liquidez_seca'] = (df['ativos_circulantes'] - df['estoques']) / df['passivos_circulantes']

    # Endividamento
    df['endividamento_total'] = (
        df['passivos_circulantes'] + df['passivos_não_circulantes']
    ) / df['total_de_ativos']

    df['divida_patrimonio'] = df['dívidas_financeiras'] / df['patrimônio_líquido']

    # Rentabilidade
    df['margem_bruta'] = df['lucro_bruto'] / df['receita_de_vendas']
    df['margem_operacional'] = df['ebit'] / df['receita_de_vendas']
    df['margem_liquida'] = df['lucro_periodo'] / df['receita_de_vendas']
    df['margem_ebitda'] = df['ebitda'] / df['receita_de_vendas']

    # Retornos
    df['roa'] = df['lucro_periodo'] / df['total_de_ativos']
    df['roe'] = df['lucro_periodo'] / df['patrimônio_líquido']

    # Caixa e dívida
    df['fco_divida'] = df['fluxo_de_caixa_líquido_das_atividades_operacionais'] / df['dívidas_financeiras']
    df['fcf_divida'] = df['fluxo_de_caixa_livre'] / df['dívidas_financeiras']

    # Cobertura financeira
    df['cobertura_juros'] = df['ebit'] / df['despesas_financeiras']
    df['ebitda_divida'] = df['ebitda'] / df['dívidas_financeiras']

    # Eficiência
    df['giro_ativos'] = df['receita_de_vendas'] / df['total_de_ativos']
    df['ciclo_estoques'] = df['estoques'] / df['cogs']
    df['ciclo_recebiveis'] = df['contas_a_receber'] / df['receita_de_vendas']
    df['ciclo_pagamentos'] = df['contas_a_pagar'] / df['cogs']
    df['ciclo_estoques_dias'] = df['estoques'] / (df['cogs'] / 365)


    # Limpeza de infinitos
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    return df
