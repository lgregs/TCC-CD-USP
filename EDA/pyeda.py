# %%
import pandas as pd

# %%
df = pd.read_csv('C:/Users/gregorio/TCC-CD-USP/archives/balancos_periodo_2008_2024.csv')
df.head()

# %%
df['Desc'].unique()

# %% [markdown]
# ## Tradução
# * Colunas e tipos de documento.
# * Utilizei Google Tradutor.

# %%
colunas_traduzidas = {
    'Desc': 'Descricao',
    'Yıllık': 'Anual',
    '9 Aylık': '9_Meses',
    '6 Aylık': '6_Meses',
    '3 Aylık': '3_Meses',
    'Year':'Ano'
}

df = df.rename(columns=colunas_traduzidas)

# %%
# Usei o Google Tradutor
traducao_termos_desc = {
    'Dönen Varlıklar': 'Ativos Circulantes',
    '  Nakit ve Nakit Benzerleri': 'Caixa e Equivalentes de Caixa',
    '  Finansal Yatırımlar': 'Investimentos Financeiros',
    '  Ticari Alacaklar': 'Contas a Receber',
    '  Finans Sektörü Faaliyetlerinden Alacaklar': 'Contas a Receber de Atividades do Setor Financeiro',
    '  Diğer Alacaklar': 'Outros Recebíveis',
    '  Stoklar': 'Estoques',
    '  Canlı Varlıklar': 'Ativos Biológicos',
    '  Diğer Dönen Varlıklar': 'Outros Ativos Circulantes',
    '    (Ara Toplam)': '(Subtotal)',
    '  Satış Amacıyla Elde Tutulan Duran Varlıklar': 'Ativos Não Circulantes Mantidos para Venda',
    'Duran Varlıklar': 'Ativos Não Circulantes',
    '  Özkaynak Yöntemiyle Değerlenen Yatırımlar': 'Investimentos Avaliados pelo Método da Equivalência Patrimonial',
    '  Yatırım Amaçlı Gayrimenkuller': 'Imóveis de Investimento',
    '  Maddi Duran Varlıklar': 'Ativos Imobilizados',
    '  Şerefiye': 'Goodwill',
    '  Maddi Olmayan Duran Varlıklar': 'Ativos Intangíveis',
    '  Ertelenmiş Vergi Varlığı': 'Ativo Fiscal Diferido',
    '  Diğer Duran Varlıklar': 'Outros Ativos Não Circulantes',
    'TOPLAM VARLIKLAR': 'TOTAL DE ATIVOS',
    'KAYNAKLAR': 'PASSIVO E PATRIMÔNIO LÍQUIDO',
    'Kısa Vadeli Yükümlülükler': 'Passivos Circulantes',
    '  Finansal Borçlar': 'Dívidas Financeiras',
    '  Diğer Finansal Yükümlülükler': 'Outras Obrigações Financeiras',
    '  Ticari Borçlar': 'Contas a Pagar',
    '  Diğer Borçlar': 'Outras Dívidas',
    '  Finans Sektörü Faaliyetlerinden Borçlar': 'Dívidas de Atividades do Setor Financeiro',
    '  Devlet Teşvik ve Yardımları': 'Incentivos e Ajuda Governamental',
    '  Dönem Karı Vergi Yükümlülüğü': 'Obrigações Fiscais sobre o Lucro do Período',
    '  Borç Karşılıkları': 'Provisões para Dívidas',
    '  Diğer Kısa Vadeli Yükümlülükler': 'Outros Passivos Circulantes',
    '  Satış Amaçlı Elde Tutulan Duran Varlıklara İlişkin Yükümlülükler': 'Passivos Relacionados a Ativos Não Circulantes Mantidos para Venda',
    'Uzun Vadeli Yükümlülükler': 'Passivos Não Circulantes',
    '    Uzun vadeli karşılıklar': 'Provisões de Longo Prazo',
    '  Çalışanlara Sağlanan Faydalara İliş.Karş.': 'Provisões para Benefícios a Empregados',
    '  Ertelenmiş Vergi Yükümlülüğü': 'Passivo Fiscal Diferido',
    '  Diğer Uzun Vadeli Yükümlülükler': 'Outros Passivos Não Circulantes',
    'Özkaynaklar': 'Patrimônio Líquido',
    '  Ana Ortaklığa Ait Özkaynaklar': 'Patrimônio Líquido Atribuível aos Acionistas da Controladora',
    '  Ödenmiş Sermaye': 'Capital Social Integralizado',
    '  Karşılıklı İştirak Sermayesi Düzeltmesi (-)': 'Ajuste de Capital de Participação Mútua (-)',
    '  Hisse Senedi İhraç Primleri': 'Reservas de Capital de Emissão de Ações',
    '  Değer Artış Fonları': 'Fundos de Reavaliação / Valorização',
    '  Yabancı Para Çevrim Farkları': 'Diferenças de Conversão de Moeda Estrangeira',
    '  Kardan Ayrılan Kısıtlanmış Yedekler': 'Reservas Restritas Separadas do Lucro',
    '  Geçmiş Yıllar Kar/Zararları': 'Lucros/Prejuízos Acumulados',
    '  Dönem Net Kar/Zararı': 'Lucro/Prejuízo Líquido do Período',
    '  Diğer Özsermaye Kalemleri': 'Outros Itens do Patrimônio Líquido',
    '  Azınlık Payları': 'Participações de Não Controladores',
    'TOPLAM KAYNAKLAR': 'TOTAL DO PASSIVO E PATRIMÔNICO LÍQUIDO',
    'Sürdürülen Faaliyetler': 'Operações Continuadas',
    'Satış Gelirleri': 'Receita de Vendas',
    'Satışların Maliyeti (-)': 'Custo dos Produtos/Serviços Vendidos (-)',
    'Ticari Faaliyetlerden Diğer Kar (Zarar)': 'Outros Ganhos (Perdas) de Atividades Comerciais',
    'Ticari Faaliyetlerden Brüt Kar (Zarar)': 'Lucro Bruto (Prejuízo) de Atividades Comerciais',
    'Faiz, Ücret, Prim, Komisyon ve Diğer Gelirler': 'Receitas de Juros, Taxas, Prêmios, Comissões e Outras',
    'Faiz, Ücret, Prim, Komisyon ve Diğer Giderler (-)': 'Despesas de Juros, Taxas, Prêmios, Comissões e Outras (-)',
    'Finans Sektörü Faaliyetlerinden Diğer Kar (Zarar)': 'Outros Ganhos (Perdas) de Atividades do Setor Financeiro',
    'Finans Sektörü Faaliyetlerinden Brüt Kar (Zarar)': 'Lucro Bruto (Prejuízo) de Atividades do Setor Financeiro',
    'Diğer Gelir ve Giderler': 'Outras Receitas e Despesas',
    'BRÜT KAR (ZARAR)': 'LUCRO BRUTO (PREJUÍZO)',
    'Pazarlama, Satış ve Dağıtım Giderleri (-)': 'Despesas de Marketing, Vendas e Distribuição (-)',
    'Genel Yönetim Giderleri (-)': 'Despesas Gerais e Administrativas (-)',
    'Araştırma ve Geliştirme Giderleri (-)': 'Despesas de Pesquisa e Desenvolvimento (-)',
    'Diğer Faaliyet Gelirleri': 'Outras Receitas Operacionais',
    'Diğer Faaliyet Giderleri (-)': 'Outras Despesas Operacionais (-)',
    'Faaliyet Karı Öncesi Diğer Gelir ve Giderler': 'Outras Receitas e Despesas Antes do Lucro Operacional',
    'FAALİYET KARI (ZARARI)': 'LUCRO OPERACIONAL (PREJUÍZO)',
    'Net Faaliyet Kar/Zararı': 'Lucro/Prejuízo Operacional Líquido',
    'Özkaynak Yöntemiyle Değerlenen Yatırımların Kar/Zararlarındaki Paylar': 'Participação nos Lucros/Prejuízos de Investimentos Avaliados pelo Método da Equivalência Patrimonial',
    '(Esas Faaliyet Dışı) Finansal Gelirler': 'Receitas Financeiras (Não Operacionais)',
    '(Esas Faaliyet Dışı) Finansal Giderler (-)': 'Despesas Financeiras (Não Operacionais) (-)',
    'Vergi Öncesi Diğer Gelir ve Giderler': 'Outras Receitas e Despesas Antes do Imposto',
    'SÜRDÜRÜLEN FAaliyetLER VERGİ ÖNCESİ KARI (ZARARI)': 'LUCRO (PREJUÍZO) ANTES DO IMPOSTO DAS OPERAÇÕES CONTINUADAS',
    'Sürdürülen Faaliyetler Vergi Geliri (Gideri)': 'Receita (Despesa) de Imposto das Operações Continuadas',
    '  Dönem Vergi Geliri (Gideri)': 'Receita (Despesa) de Imposto do Período',
    '  Ertelenmiş Vergi Geliri (Gideri)': 'Receita (Despesa) de Imposto Diferido',
    '  Diğer Vergi Geliri (Gideri)': 'Outra Receita (Despesa) de Imposto',
    'SÜRDÜRÜLEN FAALİYETLER DÖNEM KARI/ZARARI': 'LUCRO/PREJUÍZO LÍQUIDO DO PERÍODO DAS OPERAÇÕES CONTINUADAS',
    'DURDURULAN FAALİYETLER': 'OPERAÇÕES DESCONTINUADAS',
    'Durdurulan Faaliyetler Vergi Sonrası Dönem Karı (Zararı)': 'Lucro (Prejuízo) do Período Após Imposto das Operações Descontinuadas',
    'DÖNEM KARI (ZARARI)': 'LUCRO (PREJUÍZO) DO PERÍODO',
    'Dönem Kar/Zararının Dağılımı': 'Distribuição do Lucro/Prejuízo do Período',
    'Azınlık Payları': 'Participações de Não Controladores',
    'Ana Ortaklık Payları': 'Participações da Controladora',
    'Hisse Başına Kazanç': 'Lucro por Ação',
    'Seyreltilmiş Hisse Başına Kazanç': 'Lucro por Ação Diluído',
    'Sürdürülen Faaliyetlerden Hisse Başına Kazanç': 'Lucro por Ação de Operações Continuadas',
    'Sürdürülen Faaliyetlerden Seyreltilmiş Hisse Başına Kazanç': 'Lucro por Ação Diluído de Operações Continuadas',
    'Amortisman Giderleri': 'Despesas de Amortização',
    'Kıdem Tazminatı': 'Indenização por Antiguidade',
    'Finansman Giderleri': 'Despesas Financeiras',
    'Yurtiçi Satışlar': 'Vendas Domésticas',
    'Yurtdışı Satışlar': 'Vendas Internacionais',
    'Net Yabancı Para Pozisyonu': 'Posição Cambial Líquida',
    '  Müşteri Sözleşmelerinden Doğan Varlıklar': 'Ativos de Contratos com Clientes',
    '  Kullanım Hakkı Varlıkları': 'Ativos de Direito de Uso',
    '  Müşteri Söz. Doğan Yük.': 'Passivos de Contratos com Clientes',
    '  Ertelenmiş Gelirler (Müşteri Söz. Doğan Yük. Dış.Kal.)': 'Receitas Diferidas (Exceto Passivos de Contratos com Clientes)',
    '  Müşteri Söz.Doğan Yük.': '  Passivos de Contratos com Clientes',
    '  Ertelenmiş Gelirler (Müşteri Söz.Doğan Yük. Dış.Kal.)': 'Receitas Diferidas (Exceto Passivos de Contratos com Clientes)',
    '  Yatırım Faaliyetlerinden Gelirler': 'Receitas de Atividades de Investimento',
    '  Yatırım Faaliyetlerinden Giderler (-)': 'Despesas de Atividades de Investimento (-)',
    '  Diğer Gelir ve Giderler': 'Outras Receitas e Despesas',
    'Finansman Gideri Öncesi Faaliyet Karı/Zararı': 'Lucro/Prejuízo Operacional Antes das Despesas Financeiras',
    'Parasal net yabancı para varlık/(yükümlülük) pozisyonu': 'Posição Líquida (Ativo/Passivo) Monetária em Moeda Estrangeira',
    'Net YPP (Hedge Dahil)': 'Posição Cambial Líquida (Incluindo Hedge)',
    ' İşletme Faaliyetlerinden Kaynaklanan Net Nakit': 'Fluxo de Caixa Líquido das Atividades Operacionais',
    ' Düzeltme Öncesi Kar': 'Lucro Antes dos Ajustes',
    ' Düzeltmeler:': 'Ajustes:',
    '  Amortisman & İtfa Payları': 'Amortização e Quotas de Exaustão',
    '  Karşılıklardaki Değişim': 'Mudança nas Provisões',
    '  Diğer Gelir/ Gider': 'Outras Receitas/Despesas',
    ' İşletme Sermayesinde Değişikler Öncesi Faaliyet Karı (+)': 'Lucro Operacional Antes das Mudanças no Capital de Giro (+)',
    '  İşletme Sermayesindeki Değişiklikler': 'Mudanças no Capital de Giro',
    ' Esas Faaliyet ile İlgili Oluşan Nakit (+)': 'Caixa Gerado por Atividades Principais (+)',
    '  Diğer İşletme Faaliyetlerinden Nakit': 'Fluxo de Caixa de Outras Atividades Operacionais',
    '  Sabit Sermaye Yatırımları': '  Investimentos em Capital Fixo',
    '  Diğer Yatırım Faaliyetlerinden Nakit': 'Fluxo de Caixa de Outras Atividades de Investimento',
    ' Yatırım Faaliyetlerinden Kaynaklanan Nakit': 'Fluxo de Caixa das Atividades de Investimento',
    'Serbest Nakit Akım': 'Fluxo de Caixa Livre',
    'Finansal Borçlardaki Değişim': 'Variação nas Dívidas Financeiras',
    'Temettü Ödemeleri': 'Pagamento de Dividendos',
    'Sermaye Artırımı': 'Aumento de Capital',
    'Diğer Finansman Faaliyetlerinden Nakit': 'Fluxo de Caixa de Outras Atividades de Financiamento',
    'Finansman Faaliyetlerden Kaynaklanan Nakit': 'Fluxo de Caixa das Atividades de Financiamento',
    'Yab. Para Çev. Fark. Etk. Önc.Nak.Ve Nak. Benz. Net Artış/Azalış': 'Aumento/Diminuição Líquido de Caixa e Equivalentes de Caixa Antes do Efeito das Diferenças de Conversão de Moeda Estrangeira',
    ' Yab.ı Para Çevrim Fark. Nakit Ve Nakit Benz. Üzerindeki Etkisi': 'Efeito das Diferenças de Conversão de Moeda Estrangeira sobre o Caixa e Equivalentes de Caixa',
    ' Diğer Nakit Girişi/Çıkışı': 'Outras Entradas/Saídas de Caixa',
    'Nakit ve Benzerlerindeki Değişim': 'Variação no Caixa e Equivalentes',
    'Diğer Nakit ve Nakit Benzerlerindeki Artış': 'Aumento em Outros Caixas e Equivalentes de Caixa',
    'Dönem Başı Nakit Değerler': 'Valores de Caixa no Início do Período',
    'Dönem Sonu Nakit': 'Caixa no Final do Período',
    ' Ertelenmiş Vergi Geliri (Gideri)': 'Receita (Despesa) de Imposto Diferido'
}

df['Descricao'] = df['Descricao'].map(traducao_termos_desc)

print(df['Descricao'].unique())

# %%
df.head()

# %% [markdown]
# ## Tratativa de Valores Nulos

# %%
df.isnull().sum()

# %%
(df.isnull().sum() / len(df)) * 100

# %%
# Count duplicates
df.duplicated().sum()

# %% [markdown]
# * Após identificar muitos valores duplicados zerados, vou tratar primeiro dos zerados e nulos depois volto neles, pois boa parte deles se trata de indicadores zerados e seria interressante analisar isso ... 

# %%
df[df.duplicated()]

# %%
df[df.duplicated()].describe()

# %% [markdown]
# * Muitos Valores Nulos ao longo do DF.

# %%
# Checar quantos tipos diferentes de indicadores existem.
doc_count = df["Descricao"].nunique()
doc_types = df["Descricao"].unique()

print("Quantidade de Indicadores:", doc_count)
print("Indicadores:")
print(doc_types)

# %%
# Checar valores nulos em todos os periodos de tempo
null_counts = df[["Anual", "9_Meses", "6_Meses", "3_Meses"]].isnull().sum()
print("\nNull counts por coluna:")
print(null_counts)

# %%
# 3. Checar quantidade de colunas com dados completos em todos os periodos de tempo
rows_with_complete_data = df.dropna(subset=["Anual", "9_Meses", "6_Meses", "3_Meses"])
print("\nTotal rows:", len(df))
print("Linhas com os 4 periodos de tempo nao nulos:", len(rows_with_complete_data))

# %%
rows_with_complete_data

# %%
# Pivot for each time period
periods = ['Anual', '9_Meses', '6_Meses', '3_Meses']
dfs = []

for period in periods:
    df_temp = rows_with_complete_data.pivot_table(
        index=['CompanyCode', 'Ano'],
        columns='Descricao',
        values=period,
        aggfunc='first'
    )
    # Add suffix to distinguish time periods
    df_temp.columns = [f"{col}_{period}" for col in df_temp.columns]
    dfs.append(df_temp)

# Combine all periods
df_wide = pd.concat(dfs, axis=1).reset_index()

# %%
df_wide

# %%
import matplotlib.pyplot as plt
import seaborn as sns
'''
sample_cols = df_wide.select_dtypes('number').columns[:6]

fig, axes = plt.subplots(2, 3, figsize=(12, 6))
for col, ax in zip(sample_cols, axes.flatten()):
    sns.histplot(df_wide[col], kde=True, ax=ax, bins=30)
    ax.set_title(col)
plt.tight_layout()
plt.show()
'''

# %%
# Each period becomes a separate observation
df_long = []

for period in ['3_Meses', '6_Meses', '9_Meses', 'Anual']:
    df_temp = rows_with_complete_data.pivot_table(
        index=['CompanyCode', 'Ano'],
        columns='Descricao',
        values=period,
        aggfunc='first'
    ).reset_index()
    
    df_temp['Periodo'] = period  # Add period identifier
    df_long.append(df_temp)

df_ml = pd.concat(df_long, ignore_index=True)

print(f"New shape: {df_ml.shape}")
# Expected: ~15,000 rows with your financial indicators as columns

# %%
# LIMPEZA DOS NOMES DAS COLUNAS
def clean_col_name(col_name):
    name = col_name.strip()
    name = name.replace(' ', '_').replace('(-)', '').replace('(PREJUÍZO)', '').replace('/', '_')
    name = ''.join(e for e in name if e.isalnum() or e == '_')
    name = name.lower()
    name = name.strip('_')
    return name

df_ml.columns = [clean_col_name(col) for col in df_ml.columns]
df_ml

# %%
df_ml.columns.tolist()

# %%
#df_ml.to_csv('C:/Users/gregorio/TCC-CD-USP/archives/df_ml.csv', index=False)

# %%
# Define the columns you want to keep
selected_columns = [
    'companycode',
    'ano',
    'periodo',
    'ativos_circulantes',
    'ativos_não_circulantes',
    'total_de_ativos',
    'passivos_circulantes',
    'passivos_não_circulantes',
    'total_do_passivo_e_patrimônico_líquido',
    'patrimônio_líquido',
    'receita_de_vendas',
    'lucro_bruto',
    'lucro_operacional',
    'lucro__do_período',    
    'lucro_prejuízo_líquido_do_período',
    'despesas_financeiras',
    'despesas_gerais_e_administrativas',
    'custo_dos_produtos_serviços_vendidos',
    'fluxo_de_caixa_líquido_das_atividades_operacionais',
    'fluxo_de_caixa_livre',
    'fluxo_de_caixa_das_atividades_de_financiamento',
    'fluxo_de_caixa_das_atividades_de_investimento',
    'estoques',
    'contas_a_receber',
    'contas_a_pagar',
    'dívidas_financeiras',
    'despesas_de_amortização',
    'amortização_e_quotas_de_exaustão',
    'lucro_operacional_antes_das_mudanças_no_capital_de_giro',
]

# Check which columns actually exist in df_ml (case-insensitive matching)
# This helps identify any naming mismatches
available_columns = []
df_ml_lower = {col.lower(): col for col in df_ml.columns}

for col in selected_columns:
    col_lower = col.lower()
    if col_lower in df_ml_lower:
        available_columns.append(df_ml_lower[col_lower])
    else:
        print(f"⚠️ Column not found: '{col}'")

print(f"\n✅ Found {len(available_columns)} out of {len(selected_columns)} columns")
print(f"Available columns: {available_columns}\n")

# Create clean dataframe
df_clean = df_ml[available_columns].copy()

# %%
df_clean.columns.tolist()

# %%
# Mostra todas as colunas e quantas vezes cada uma aparece
print(df_clean.columns)

# Contar duplicadas
print("\nColunas duplicadas:")
print(df_clean.columns[df_clean.columns.duplicated(keep=False)])


# %%
df_clean.rename(columns={
    "lucro_operacional_antes_das_mudanças_no_capital_de_giro": "ebitda",
    "lucro_operacional": "ebit",
    "amortização_e_quotas_de_exaustão": "amortization"
}, inplace=True)

# %%
df_clean.columns.tolist()

# %%
df_clean.isnull().sum() 

# %%
import numpy as np

print("=" * 60)
print("BEFORE EBITDA CALCULATION")
print("=" * 60)
print(f"\nMissing values:")
print(f"  EBIT: {df_clean['ebit'].isnull().sum()} ({df_clean['ebit'].isnull().sum()/len(df_clean)*100:.2f}%)")
print(f"  Amortization: {df_clean['amortization'].isnull().sum()} ({df_clean['amortization'].isnull().sum()/len(df_clean)*100:.2f}%)")
print(f"  EBITDA (original): {df_clean['ebitda'].isnull().sum()} ({df_clean['ebitda'].isnull().sum()/len(df_clean)*100:.2f}%)")


# %%
# Step 2: Create a working copy of amortization
df_clean['amortization_filled'] = df_clean['amortization'].copy()
df_clean.head()

# %%
# Step 3: Only fill missing amortization with 5% of revenue
missing_amort_mask = df_clean['amortization'].isnull()
df_clean.loc[missing_amort_mask, 'amortization_filled'] = (
    df_clean.loc[missing_amort_mask, 'receita_de_vendas'] * 0.05
)

print(f"\n✅ Estimated {missing_amort_mask.sum()} missing amortization values as 5% of revenue")

# %%
# Step 4: Only calculate EBITDA where it's missing
# EBITDA = EBIT + Amortization (only for missing EBITDA values)
missing_ebitda_mask = df_clean['ebitda'].isnull()
has_ebit = df_clean['ebit'].notnull()

# Calculate missing EBITDA only where we have EBIT
can_calculate = missing_ebitda_mask & has_ebit

df_clean.loc[can_calculate, 'ebitda'] = (
    df_clean.loc[can_calculate, 'ebit'] + 
    df_clean.loc[can_calculate, 'amortization_filled']
)

print(f"✅ Calculated {can_calculate.sum()} missing EBITDA values using EBIT + Amortization")
print(f"⚠️  Still missing: {(missing_ebitda_mask & ~has_ebit).sum()} EBITDA values (missing EBIT)")

# Step 5: Final validation
print("\n" + "=" * 60)
print("AFTER EBITDA CALCULATION")
print("=" * 60)
print(f"\nMissing values:")
print(f"  EBIT: {df_clean['ebit'].isnull().sum()} ({df_clean['ebit'].isnull().sum()/len(df_clean)*100:.2f}%)")
print(f"  Amortization (filled): {df_clean['amortization_filled'].isnull().sum()} ({df_clean['amortization_filled'].isnull().sum()/len(df_clean)*100:.2f}%)")
print(f"  EBITDA (final): {df_clean['ebitda'].isnull().sum()} ({df_clean['ebitda'].isnull().sum()/len(df_clean)*100:.2f}%)")


# %%
# Step 6: Show breakdown of EBITDA sources
original_ebitda = (~missing_ebitda_mask).sum()
calculated_ebitda = can_calculate.sum()
still_missing = df_clean['ebitda'].isnull().sum()

print(f"\n📊 EBITDA Data Sources:")
print(f"  Original values kept: {original_ebitda} ({original_ebitda/len(df_clean)*100:.2f}%)")
print(f"  Calculated from EBIT+Amort: {calculated_ebitda} ({calculated_ebitda/len(df_clean)*100:.2f}%)")
print(f"  Still missing: {still_missing} ({still_missing/len(df_clean)*100:.2f}%)")

# %%
# Step 7: Sample of calculated values
if can_calculate.sum() > 0:
    print("\n" + "=" * 60)
    print("SAMPLE: Rows where EBITDA was CALCULATED")
    print("=" * 60)
    sample = df_clean[can_calculate].head(5)[
        ['companycode', 'ano', 'ebit', 'amortization', 
         'amortization_filled', 'ebitda']
    ]
    print(sample.to_string())

# %%
# Step 8: Sample of original values
if original_ebitda > 0:
    print("\n" + "=" * 60)
    print("SAMPLE: Rows where EBITDA was KEPT (original)")
    print("=" * 60)
    sample_orig = df_clean[~missing_ebitda_mask].head(5)[
        ['companycode', 'ano', 'ebit', 'amortization', 
         'amortization_filled', 'ebitda']
    ]
    print(sample_orig.to_string())

# %%
# Step 9: EBITDA statistics
print("\n" + "=" * 60)
print("EBITDA STATISTICS")
print("=" * 60)
print(df_clean['ebitda'].describe())

# %%
df_clean['amortization'] = df_clean['amortization_filled']
df_clean.drop('amortization_filled', axis=1, inplace=True)
df_clean.head()

# %%
df_clean.columns.tolist()

# %%
df_clean.isnull().sum()

# %%
df_clean = df_clean.rename(columns={
    'lucro_prejuízo_líquido_do_período_das_operações_continuadas': 'lucro_liquido_op_continuas',
    'custo_dos_produtos_serviços_vendidos': 'cogs', 
    'lucro__do_período': 'lucro_periodo',
})

# %%
# Selecionar uma empresa com dados faltantes antes da interpolação
empresa_exemplo = df_clean[df_clean['fluxo_de_caixa_líquido_das_atividades_operacionais'].isnull()]['companycode'].iloc[0]
empresa_exemplo

# %%
df_original = df_clean.copy()

# %%
df_original

# %%
# Mapeia os períodos para datas de fim de trimestre
periodo_map = {
    '3_Meses': '-03-31',
    '6_Meses': '-06-30',
    '9_Meses': '-09-30',
    'Anual': '-12-31'
}

# Cria a coluna 'data' com base no ano e no final do período correspondente
df_clean['data'] = df_clean['ano'].astype(str) + df_clean['periodo'].map(periodo_map)

# Converte para datetime
df_clean['data'] = pd.to_datetime(df_clean['data'])
df_clean

# %%
df_original = df_clean.copy()

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Criar a versão interpolada
df_interpolado = df_clean.copy()
cols_fluxo = [
    'fluxo_de_caixa_líquido_das_atividades_operacionais'
]
df_interpolado[cols_fluxo] = df_interpolado.groupby('companycode')[cols_fluxo].transform(lambda g: g.interpolate(method='linear', limit_direction='both'))


# %%
df_interpolado[cols_fluxo] = df_interpolado.groupby('companycode')[cols_fluxo].transform(lambda g: g.interpolate(method='linear', limit_direction='both'))


# %%
# Selecionar uma empresa com dados faltantes
empresa_exemplo = df_original[df_original['fluxo_de_caixa_líquido_das_atividades_operacionais'].isnull()]['companycode'].iloc[0]
empresa_exemplo

# %%
# Filtrar essa empresa nas duas versões
df_orig_empresa = df_original[df_original['companycode'] == empresa_exemplo]
df_interp_empresa = df_interpolado[df_interpolado['companycode'] == empresa_exemplo]


# %%
# Plotar
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_interp_empresa,
    x='data',
    y='fluxo_de_caixa_líquido_das_atividades_operacionais',
    label='Interpolado',
    color='blue'
)

sns.scatterplot(
    data=df_orig_empresa,
    x='data',
    y='fluxo_de_caixa_líquido_das_atividades_operacionais',
    label='Original (com NaN)',
    color='red',
    zorder=5
)

plt.title(f'Fluxo de Caixa Operacional - Empresa {empresa_exemplo}\nAntes (pontos vermelhos) e Depois (linha azul) da Interpolação')
plt.xlabel('Data')
plt.ylabel('Fluxo de Caixa Operacional')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
df_clean.isnull().sum()

# %%
# Ordenar por empresa e data
df_clean.sort_values(by=['companycode', 'data'], inplace=True)

# Interpolar fluxos de caixa por empresa no tempo
cols_fluxo = [
    'fluxo_de_caixa_líquido_das_atividades_operacionais',
    'fluxo_de_caixa_livre',
    'fluxo_de_caixa_das_atividades_de_financiamento',
    'fluxo_de_caixa_das_atividades_de_investimento'
]

df_clean[cols_fluxo] = df_clean.groupby('companycode')[cols_fluxo].transform(lambda g: g.interpolate(method='linear', limit_direction='both'))

# %%
df_clean

# %%
df_clean.isnull().sum()

# %%
df_clean.columns.tolist()

# %%
from feature_engineering import criar_indicadores_credito

df_indicadores = criar_indicadores_credito(df_clean)
df_indicadores   

# %%
print(df_indicadores.isnull().sum())

# %%
df_indicadores.columns.tolist()

# %%
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df_indicadores[['margem_operacional', 'margem_ebitda']])
plt.title('Distribuição das Margens Operacionais e EBITDA')
plt.grid(True)
plt.show()


# %%
from avaliar import avaliar_indicadores_financeiros
df_avaliado = avaliar_indicadores_financeiros(df_indicadores)

# %%
df_avaliado

# %%
print(df_avaliado.isnull().sum().to_string())

# %%
from total_score import calcular_score_total
df_scored = calcular_score_total(df_avaliado)
df_scored

# %%
df_scored['score_total'].mean()

# %%
df_scored['score_total'].max()

# %%
df_scored['score_total'].min()

# %%
df_scored['score_total'].nunique()

# %%
def checar_scores_validos(df):
    """
    Verifica se todas as colunas *_score possuem valores válidos (0 a 5).
    Retorna dicionário com percentual de valores válidos por coluna.
    """
    import numpy as np

    score_cols = [col for col in df.columns if col.endswith('_score')]
    resultados = {}

    for col in score_cols:
        total = df[col].notnull().sum()
        validos = df[col].isin([0, 1, 2, 3, 4, 5]).sum()
        resultados[col] = {
            'percentual_valido': round(100 * validos / total, 2),
            'total_valores': total,
            'valores_invalidos': total - validos
        }

    return resultados


# %%
resultados_validacao = checar_scores_validos(df_scored)
import pprint
pprint.pprint(resultados_validacao)


# %%
# Seleção das empresas desejadas
empresas_destaque = ['THYAO', 'CCOLA', 'ASELS']
df_empresas = df_scored[df_scored['companycode'].isin(empresas_destaque)]
ultimos_scores = {}
for empresa in empresas_destaque:
    ult_score = df_scored[df_scored['companycode'] == empresa].sort_values('data', ascending=True).iloc[-1]['score_total']
    ultimos_scores[empresa] = ult_score

# %%
df_empresas['companycode'].unique()

# %%
# Score médio e mediano geral
media_geral = df_scored['score_total'].mean()
mediana_geral = df_scored['score_total'].median()
print(f'Media geral = {media_geral} e Mediana Geral = {mediana_geral}')

# %%
# Plot
plt.figure(figsize=(12, 6))
sns.histplot(df_scored['score_total'], kde=True, bins=30, color='lightgray', label='Distribuição Geral')

# Linhas de média e mediana
plt.axvline(media_geral, color='red', linestyle='--', label=f'Média Geral: {media_geral:.2f}')
plt.axvline(mediana_geral, color='green', linestyle='--', label=f'Mediana Geral: {mediana_geral:.2f}')

# Linhas dos scores mais recentes das empresas
for empresa, score in ultimos_scores.items():
    plt.axvline(score, linestyle='-', label=f'{empresa} (Score mais recente): {score:.2f}')

plt.title('Distribuição do Score Total com Destaque para Últimos Scores de Empresas Selecionadas')
plt.xlabel('Score Total (0 a 5)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# %%
# Média de score por data (trimestre)
media_por_periodo = df_scored.groupby('data')['score_total'].mean().sort_values(ascending=False)

# Top 10 trimestres com maior média
top_periodos = media_por_periodo.head(10)

print("Top períodos com maior score médio:")
print(top_periodos)


# %%
# Média de score por data (trimestre)
media_por_periodo = df_scored.groupby('data')['score_total'].median().sort_values(ascending=False)

# Top 10 trimestres com maior média
top_periodos = media_por_periodo.head(10)

print("Top períodos com maior score mediano:")
print(top_periodos)


# %%
# Último período do dataset
ultimo_periodo = df_scored['data'].max()

# Filtrar pelo último período
df_ultimo = df_scored[df_scored['data'] == ultimo_periodo]

# Top 5 empresas com maior score_total
top_empresas = df_ultimo[['companycode', 'score_total']].sort_values(by='score_total', ascending=False).head(5)

print("Top 5 empresas com maior score no período mais recente:")
print(top_empresas)

# %%
# Empresas alvo
empresas_destaque = ['THYAO', 'CCOLA', 'ASELS']

# Filtrar somente essas empresas
df_empresas = df_scored[df_scored['companycode'].isin(empresas_destaque)]

# Ordenar por empresa e data
df_empresas = df_empresas.sort_values(by=['companycode', 'data'])

# Agrupar e pegar os 3 últimos períodos
ultimos_tres = df_empresas.groupby('companycode').tail(4)

# Resultado organizado
print(ultimos_tres[['companycode', 'data', 'score_total']].sort_values(['companycode', 'data']))


# %%
# Identificar os 3 últimos períodos disponíveis
ultimos_tres_periodos = df_scored['data'].drop_duplicates().sort_values(ascending=False).head(4)

# Filtrar os dados para esses 3 períodos
df_ultimos_tres = df_scored[df_scored['data'].isin(ultimos_tres_periodos)]

# Para cada período, pegar o Top 5 empresas com maior score
for periodo in sorted(ultimos_tres_periodos):
    print(f"\n📅 Período: {periodo.strftime('%Y-%m-%d')}")
    top_empresas = (
        df_ultimos_tres[df_ultimos_tres['data'] == periodo]
        .sort_values(by='score_total', ascending=False)
        .head(5)
    )
    print(top_empresas[['companycode', 'score_total']])


# %%
from collections import Counter

# Lista para guardar todas as aparições no top 5 por trimestre
top5_empresas_ao_longo_do_tempo = []

# Iterar sobre cada trimestre (data)
for periodo in df_scored['data'].drop_duplicates().sort_values():
    top5 = (
        df_scored[df_scored['data'] == periodo]
        .sort_values(by='score_total', ascending=False)
        .head(5)
        ['companycode']
        .tolist()
    )
    top5_empresas_ao_longo_do_tempo.extend(top5)

# Contar quantas vezes cada empresa apareceu no Top 5
contagem_top5 = Counter(top5_empresas_ao_longo_do_tempo)

# Converter para DataFrame e ordenar
df_top5_frequentes = (
    pd.DataFrame.from_dict(contagem_top5, orient='index', columns=['aparicoes_top5'])
    .sort_values(by='aparicoes_top5', ascending=False)
    .reset_index()
    .rename(columns={'index': 'companycode'})
)

# Mostrar Top 5 empresas mais frequentes no Top 5
print("Empresas com mais aparições no Top 5 de score total por trimestre:")
print(df_top5_frequentes.head(5))


# %%
'''
from ydata_profiling import ProfileReport

profile = ProfileReport(
    df_scored,
    title="Credit Default EDA (Minimal)",
    explorative=True,   # less visual complexity, faster
    minimal=False,        
    progress_bar=True
)

profile.to_file("FINAL_EDA_MODEL_V2.html")
print(" EDA report generated successfully: FINAL_EDA_MODEL.html")

'''

# %%
df_model = df_scored.copy()

# %%
df_model=df_model.drop(columns=[
'liquidez_corrente_score',
 'liquidez_seca_score',
 'endividamento_total_score',
 'divida_patrimonio_score',
 'margem_bruta_score',
 'margem_operacional_score',
 'margem_ebitda_score',
 'margem_liquida_score',
 'roa_score',
 'roe_score',
 'fco_divida_score',
 'fcf_divida_score',
 'cobertura_juros_score',
 'ebitda_divida_score',
 'giro_ativos_score',
 'ciclo_estoques_score',
 'ciclo_recebiveis_score',
 'ciclo_pagamentos_score',
 'liquidez_media',
 'alavancagem_media',
 'rentabilidade_media',
 'retornos_media',
 'caixa_media',
 'eficiencia_media'],axis=1)

# %%
df_corr = df_model.copy()
df_corr = df_corr.drop(columns=['companycode', 'ano', 'periodo'])

# %%
# Calculate correlation matrix
corr_matrix = df_corr.corr()

# %%
corrs=corr_matrix.loc['score_total'].drop('score_total').sort_values(ascending=False)
print(corrs)

# %%
import phik
from phik import resources, report
phi_k_corr = df_corr.phik_matrix()
phi_k_corr

# %%
phik_corrs=phi_k_corr.loc['score_total'].drop('score_total').sort_values(ascending=False)
phik_corrs

# %%
df_model.columns.tolist()

# %%
df_model.to_csv('C:/Users/gregorio/TCC-CD-USP/archives/df_model_V3.csv', index=False)


