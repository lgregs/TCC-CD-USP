import pandas as pd
import numpy as np
# Importa as funções dos seus novos arquivos .py
from EDA.financial_ratios import create_financial_ratios
from EDA.score import score_financial_ratios

def clean_col_name(col_name):
    """Limpa os nomes das colunas para um formato padronizado."""
    name = col_name.strip().replace(' ', '_').replace('(-)', '').replace('(PREJUÍZO)', '').replace('/', '_')
    name = ''.join(e for e in name if e.isalnum() or e == '_').lower().strip('_')
    return name

def run_data_preparation(csv_path):
    """
    Executa o pipeline completo de preparação de dados.
    """
    # 1. Carregar os dados
    try:
        df_raw = pd.read_csv(csv_path)
        print(f"Dados brutos carregados: {df_raw.shape}")
    except FileNotFoundError:
        print(f"Arquivo '{csv_path}' não encontrado. Encerrando.")
        return None

    # 2. Limpeza de colunas (similar à Célula 2 do notebook)
    threshold = 0.45
    cols_to_drop = [
        col for col in df_raw.columns
        if (df_raw[col].isna().mean() > threshold) or ((df_raw[col] == 0).mean() > threshold)
    ]
    df_clean = df_raw.drop(columns=cols_to_drop)
    print(f"Dados após limpeza de nulos/zeros: {df_clean.shape}")

    # 3. Renomear colunas CRÍTICAS (da Célula 9)
    # Esta é a lógica que cria as colunas para 'ebit' e 'amortization'
    df_clean.rename(columns={
        "LUCRO OPERACIONAL (PREJUÍZO)": "EBIT",
        "Amortização e Quotas de Exaustão": "Amortization"
    }, inplace=True)

    # 4. Criar a coluna 'ebitda_final' (lógica da Célula 9)
    # Preenchemos EBIT e Amortization com 0 onde estão nulos para a soma
    df_clean['EBIT'] = df_clean['EBIT'].fillna(0)
    df_clean['Amortization'] = df_clean['Amortization'].fillna(0)
    
    # Agora, calculamos ebitda_final
    df_clean["ebitda_final"] = df_clean["EBIT"] + df_clean["Amortization"]
    print("Coluna 'ebitda_final' calculada.")

    # 5. Limpar todos os nomes de colunas (da Célula 17)
    df_clean.columns = [clean_col_name(col) for col in df_clean.columns]
    print("Nomes de colunas limpos (ex: 'ebitda_final').")
    
    # 6. Renomear colunas para os rácios (da Célula 18)
    df_clean = df_clean.rename(columns={
        'custo_dos_produtos_serviços_vendidos': 'cogs',
        'lucro_prejuízo_líquido_do_período_das_operações_continuadas': 'lucro_liquido_op_continuas',
        'lucro_bruto_prejuizo': 'lucro_bruto',
        'lucro_prejuizo_do_periodo': 'lucro_periodo'
    })
    
    # 7. Preencher nulos restantes com mediana (da Célula 13)
    # É importante fazer isso *antes* de calcular os rácios
    df_clean = df_clean.fillna(df_clean.median(numeric_only=True))
    print("Valores nulos preenchidos com mediana.")

    # 8. ETAPA 1: Criar Rácios
    df_with_ratios = create_financial_ratios(df_clean)
    print(f"Rácios financeiros criados. Novo shape: {df_with_ratios.shape}")

    # 9. ETAPA 2: Criar Pontuações (com a função CORRIGIDA)
    df_scored = score_financial_ratios(df_with_ratios)
    print(f"Pontuações financeiras criadas. Novo shape: {df_scored.shape}")

    # 10. Ver resultado
    print("\n--- Processamento Concluído ---")
    print("Amostra do DataFrame final com 'total_score' (corrigido):")
    print(df_scored[['companycode', 'ano', 'ebitda_final', 'ebitda_margin', 'score_ebitda_margin', 'total_score']].head())

    return df_scored

# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    
    # Defina o caminho para o seu arquivo CSV aqui
    CSV_FILE_PATH = 'C:/Users/gregorio/TCC-CD-USP/archives/df_wide.csv'
    
    # Executa o pipeline
    df_final_data = run_data_preparation(CSV_FILE_PATH)
    
    if df_final_data is not None:
        # Você pode salvar o arquivo final aqui
        # df_final_data.to_csv("df_final_com_scores.csv", index=False)
        # print("\nArquivo 'df_final_com_scores.csv' salvo com sucesso.")
        pass
