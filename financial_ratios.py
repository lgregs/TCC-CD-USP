import numpy as np
import pandas as pd
def create_financial_ratios(df):
    """
    Calculates a comprehensive set of financial ratios based on the provided dataframe.

    The function correctly handles time-series data (like 'companycode' and 'ano')
    for calculating growth ratios and cleans up infinite values that may result
    from division by zero, replacing them with NaN.

    Args:
        df (pd.DataFrame): The input dataframe with the required financial columns.
                           Must include 'companycode' and 'ano'.

    Returns:
        pd.DataFrame: A new dataframe with all the original columns plus the
                      newly calculated ratio columns.
    """
    # Create a copy to avoid modifying the original dataframe
    data = df.copy()

    # --- 1. Liquidity Ratios ---
    data['current_ratio'] = data['ativos_circulantes'] / data['passivos_circulantes']
    
    quick_assets = (data['caixa_e_equivalentes_de_caixa'] + 
                    data['contas_a_receber'] + 
                    data['outros_ativos_circulantes'])
    data['quick_ratio'] = quick_assets / data['passivos_circulantes']

    # --- 2. Leverage Ratios ---
    data['debt_to_equity'] = data['dívidas_financeiras'] / data['patrimônio_líquido']
    data['debt_to_assets'] = data['dívidas_financeiras'] / data['total_de_ativos']

    # --- 3. Profitability Ratios ---
    # Using 'lucro_prejuízo_líquido_do_período' as "Lucro Líquido"
    # Using 'lucro_prejuízo_operacional_líquido' as "Lucro Operacional"
    data['roe'] = data['lucro_prejuízo_líquido_do_período'] / data['patrimônio_líquido']
    data['roa'] = data['lucro_prejuízo_líquido_do_período'] / data['total_de_ativos']
    data['net_margin'] = data['lucro_prejuízo_líquido_do_período'] / data['receita_de_vendas']
    data['operating_margin'] = data['lucro_prejuízo_operacional_líquido'] / data['receita_de_vendas']

    # --- 4. Efficiency Ratios ---
    data['asset_turnover'] = data['receita_de_vendas'] / data['total_de_ativos']
    data['inventory_turnover'] = data['cogs'] / data['estoques']
    data['receivable_turnover'] = data['receita_de_vendas'] / data['contas_a_receber']

    # --- 5. Coverage Ratio ---
    data['interest_coverage'] = data['lucro_prejuízo_operacional_líquido'] / data['despesas_financeiras']

    # --- 6. Solvency & Stability ---
    data['retained_to_assets'] = data['lucros_prejuízos_acumulados'] / data['total_de_ativos']
    data['fx_position_ratio'] = data['posição_cambial_líquida'] / data['total_de_ativos']

    # --- 7. Growth Ratios (Time-Series Dependent) ---
    # We must sort by company and year to calculate percent change correctly.
    data = data.sort_values(by=['companycode', 'ano'])

    # .pct_change() calculates (current - previous) / previous
    # This is grouped by company to avoid comparing company A's 2010 to company B's 2009
    data['sales_growth'] = data.groupby('companycode')['receita_de_vendas'].pct_change()
    data['asset_growth'] = data.groupby('companycode')['total_de_ativos'].pct_change()
    data['net_income_growth'] = data.groupby('companycode')['lucro_prejuízo_líquido_do_período'].pct_change()

    # --- 8. Final Cleanup ---
    # Ratios can create infinite values (e.g., 100 / 0).
    # We replace all 'inf' and '-inf' with 'NaN' (Not a Number)
    # This makes the data ready for machine learning models.
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    return data

# --- EXAMPLE USAGE ---

# 1. Load your data (assuming you have it in a DataFrame called 'df')
# Example: df = pd.read_csv('your_financial_data.csv') 
# For this example, I'll create a small mock DataFrame.

# 2. Apply the function to your DataFrame
#df_with_ratios = create_financial_ratios(df)