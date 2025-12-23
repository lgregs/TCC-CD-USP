# %%
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
DF_PATH = os.getenv('DF_MODEL')
df = pd.read_csv(DF_PATH)
df.head()

# %%
df.isnull().sum()

# %%
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

# %%
import matplotlib.pyplot as plt
import seaborn as sns
# Mapa de correlação das features.

df_corr = df.copy()
df_corr = df_corr.drop(columns=['companycode', 'ano', 'periodo', 'data'])

# %%
# Calculate correlation matrix
corr_matrix = df_corr.corr()

# %%
# Set up the matplotlib figure
plt.figure(figsize=(14, 10))

# Create a heatmap using seaborn
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, square=True, linewidths=.5)

# Titles and labels
plt.title('Correlation Matrix Heatmap', fontsize=16)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Features', fontsize=12)

plt.show()

# %%
corrs=corr_matrix.loc['score_total'].drop('score_total').sort_values(ascending=False)
corrs

# %%
import phik
from phik import resources, report
phi_k_corr = df_corr.phik_matrix()

# %%
phi_k_corr

# %%
phik_corrs=phi_k_corr.loc['score_total'].drop('score_total').sort_values(ascending=False)
phik_corrs

# %%
# Features and target
X = df.drop(columns=['score_total','companycode','ano','periodo','data'])
y = df['score_total']

# %%
X.columns.to_list()

# %%
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
# Build da pipeline Linear Regression
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value=0)),
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# %%
# Fit model
print('Treinando o modelo')
pipeline.fit(X_train, y_train)
print('Modelo treinado com sucesso!')

# %%
# Predictions
y_pred = pipeline.predict(X_test)

# %%
# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
r2 = r2_score(y_test, y_pred)

# %%
# Results summary
metrics = {
    'MAE': mae,
    'MSE': mse,
    'RMSE': rmse,
    'MAPE': mape,
    'R²': r2
}

# %%
# Display results
metrics_df = pd.DataFrame([metrics])
metrics_df

# %%
# Residuals
residuals = y_test - y_pred

# %%
# Plot residuals vs index
plt.figure(figsize=(12, 6))
plt.scatter(range(len(residuals)), residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Index')
plt.xlabel('Index')
plt.ylabel('Residuals')
plt.show()

# %%
# Residuals vs estimated response values
plt.figure(figsize=(12, 6))
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Estimated Response Values')
plt.xlabel('Estimated Values')
plt.ylabel('Residuals')
plt.show()

# %%
# Residuals vs observations (actual values)
plt.figure(figsize=(12, 6))
plt.scatter(y_test, residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Observed Values')
plt.xlabel('Observed Values')
plt.ylabel('Residuals')
plt.show()

# %%
# Residuals vs predicted values
plt.figure(figsize=(12, 6))
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Predicted Values')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()

# %%
# --- PIPELINE 2: RANDOM FOREST ---
pipeline_rf = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value=0)), 
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
])

# %%
print("\nTreinando o modelo RandomForestRegressor...")
pipeline_rf.fit(X_train, y_train)
print("Modelo RandomForestRegressor treinado com sucesso.")

# %%
# 2. Previsões e Métricas (Random Forest)
y_pred_rf = pipeline_rf.predict(X_test)
metrics_rf = {
    'Modelo': 'Random Forest',
    'MAE': mean_absolute_error(y_test, y_pred_rf),
    'MSE': mean_squared_error(y_test, y_pred_rf),
    'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
    'MAPE (%)': np.mean(np.abs((y_test - y_pred_rf) / (y_test + 1e-6))) * 100,
    'R²': r2_score(y_test, y_pred_rf)
}
metrics_rf_df= pd.DataFrame([metrics_rf])
metrics_rf_df

# %%
# Residuals para Random Forest
residuals_rf = y_test - y_pred_rf

# Plot residuals vs index para Random Forest
plt.figure(figsize=(12, 6))
plt.scatter(range(len(residuals_rf)), residuals_rf, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Index (Random Forest)')
plt.xlabel('Index')
plt.ylabel('Residuals')
plt.show()

# %%
# Residuals vs estimated response values para Random Forest
plt.figure(figsize=(12, 6))
plt.scatter(y_pred_rf, residuals_rf, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Estimated Response Values (Random Forest)')
plt.xlabel('Estimated Values')
plt.ylabel('Residuals')
plt.show()

# %%
# Residuals vs observations (actual values) para Random Forest
plt.figure(figsize=(12, 6))
plt.scatter(y_test, residuals_rf, alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Observed Values (Random Forest)')
plt.xlabel('Observed Values')
plt.ylabel('Residuals')
plt.show()

# %%
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, make_scorer
import numpy as np

# %%
# Definir modelo
model = RandomForestRegressor(random_state=42)


# %%
# Definir KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
kfold

# %%
# Definir métrica de avaliação
#mae_scorer = make_scorer(mean_absolute_error)

# %%
# Aplicar validação cruzada
#mae_scores = cross_val_score(model, X, y, cv=kfold, scoring=mae_scorer)

# %%
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# %%
# Listas para armazenar métricas
mae_list, mse_list, rmse_list, mape_list, r2_list = [], [], [], [], []

# Loop pelos folds
for train_index, val_index in kfold.split(X):
    X_train_fold, X_val_fold = X.iloc[train_index], X.iloc[val_index]
    y_train_fold, y_val_fold = y.iloc[train_index], y.iloc[val_index]

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train_fold, y_train_fold)
    y_pred = model.predict(X_val_fold)

    # Calcular métricas
    mae = mean_absolute_error(y_val_fold, y_pred)
    mse = mean_squared_error(y_val_fold, y_pred)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_val_fold - y_pred) / y_val_fold)) * 100
    r2 = r2_score(y_val_fold, y_pred)

    # Armazenar
    mae_list.append(mae)
    mse_list.append(mse)
    rmse_list.append(rmse)
    mape_list.append(mape)
    r2_list.append(r2)

# Resultados Médios
print("Validação Cruzada (K-Fold = 5):")
print(f"MAE médio: {np.mean(mae_list):.4f}")
print(f"MSE médio: {np.mean(mse_list):.4f}")
print(f"RMSE médio: {np.mean(rmse_list):.4f}")
print(f"MAPE médio (%): {np.mean(mape_list):.4f}")
print(f"R² médio: {np.mean(r2_list):.4f}")


# %%
#print("Validação Cruzada (K-Fold):")
#print(f"MAE médio: {mae_scores.mean():.4f}")
#print(f"MAE desvio-padrão: {mae_scores.std():.4f}")

# %%
# Separar último ano como teste (ex: 2023)
df_train = df[df['data'] < '2023-01-01']
df_test  = df[df['data'] >= '2023-01-01']

# %%
# Features e target corretos
feat = df_train.drop(columns=['score_total','companycode','ano','periodo','data']).columns.to_list()

# %%

X_train = df_train[feat]
y_train = df_train['score_total']

# %%
X_test = df_test[feat]
y_test = df_test['score_total']

# %%
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# %%
# Prever
y_pred = model.predict(X_test)

# Avaliação
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\nValidação Temporal (Holdout - Teste em 2023):")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")


# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Previsão
y_pred = model.predict(X_test)

# Gráfico
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')
plt.xlabel('Valor Real')
plt.ylabel('Valor Previsto')
plt.title('📊 Score Total: Real vs Previsto (2023)')
plt.grid(True)
plt.tight_layout()
plt.show()


# %%
import pandas as pd

# Importância
importances = model.feature_importances_
feat_importance = pd.Series(importances, index=feat).sort_values(ascending=False)

# Gráfico
plt.figure(figsize=(10, 8))
sns.barplot(x=feat_importance.values[:15], y=feat_importance.index[:15])
plt.title('15 Features Mais Importantes no Modelo')
plt.xlabel('Importância')
plt.ylabel('Variável')
plt.tight_layout()
plt.show()


# %%
# Adiciona erro absoluto à base de teste
df_test = df_test.copy()
df_test['y_pred'] = y_pred
df_test['erro_absoluto'] = abs(df_test['score_total'] - df_test['y_pred'])

# Agrupamento por empresa
erro_por_empresa = df_test.groupby('companycode')['erro_absoluto'].mean().sort_values(ascending=False)

# Gráfico
plt.figure(figsize=(12, 6))
erro_por_empresa.head(15).plot(kind='barh', color='coral')
plt.xlabel('Erro Absoluto Médio')
plt.title('Erro Médio por Empresa (Top 15)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


# %%
import shap

# Criar explainer SHAP (para modelos baseados em árvore)
#explainer = shap.TreeExplainer(model)

# Calcular valores SHAP (pode demorar para muitos dados)
#shap_values = explainer.shap_values(X_test)


# %%
# Sumário global: impacto médio de cada variável
#shap.summary_plot(shap_values, X_test, plot_type="bar")


# %%
# Mostra como cada feature afeta o output (positivo ou negativo)
#shap.summary_plot(shap_values, X_test)


# %%
# Exemplo: primeira empresa do conjunto de teste
#idx = 3 # ou use um index específico

# Força da contribuição de cada feature para o score
#shap.plots.waterfall(explainer(X_test.iloc[idx]))


# %%
#Isso mostra exatamente por que aquela empresa recebeu aquele score — quais indicadores ajudaram ou prejudicaram a nota.

# %%
# Filtrar apenas THYAO
df_thyao_real = df[df['companycode'] == 'THYAO'].copy()

# Prever usando o modelo treinado (usando todas as colunas de features já conhecidas)
X_thyao = df_thyao_real.drop(columns=['score_total', 'companycode', 'ano', 'periodo', 'data'])
y_thyao_pred = model.predict(X_thyao)

# Adicionar coluna de previsão ao DataFrame
df_thyao_real['score_predito'] = y_thyao_pred

# Plotar
plt.figure(figsize=(14, 6))
plt.plot(df_thyao_real['data'], df_thyao_real['score_total'], label='Real', color='blue', linewidth=2)
plt.plot(df_thyao_real['data'], df_thyao_real['score_predito'], label='Previsto', color='orange', linestyle='--', linewidth=2)

plt.title('Comparação: Score Total Real vs Previsto - THYAO')
plt.xlabel('Ano')
plt.ylabel('Score Total (0 a 5)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Criar um ranking baseado na média histórica do Score Total
ranking_historico = df.groupby('companycode')['score_total'].mean().sort_values(ascending=False)

# 2. Identificar os extremos
melhor_empresa = ranking_historico.index[0]   # A primeira da lista
pior_empresa = ranking_historico.index[-1]    # A última da lista

# Garantir que não selecionamos a própria THYAO como melhor/pior (para não duplicar)
if melhor_empresa == 'THYAO':
    melhor_empresa = ranking_historico.index[1]
if pior_empresa == 'THYAO':
    pior_empresa = ranking_historico.index[-2]

print(f"✈️ Empresa Foco: THYAO")
print(f"🏆 Melhor Desempenho (Benchmark Positivo): {melhor_empresa} (Média: {ranking_historico[melhor_empresa]:.2f})")
print(f"⚠️ Pior Desempenho (Benchmark Negativo): {pior_empresa} (Média: {ranking_historico[pior_empresa]:.2f})")

# 3. Filtrar o DataFrame apenas para essas 3 empresas
empresas_selecionadas = ['THYAO', melhor_empresa, pior_empresa]
df_comparacao = df[df['companycode'].isin(empresas_selecionadas)].copy()

# Definir uma ordem fixa para as cores nos gráficos
ordem_empresas = [melhor_empresa, 'THYAO', pior_empresa]
paleta_cores = {melhor_empresa: 'green', 'THYAO': 'blue', pior_empresa: 'red'}

# %%
# Usar mesma estrutura do gráfico anterior, mas substituir score de THYAO pelo previsto
df_thyao_pred = df_thyao_real[['data', 'score_predito']].copy()
df_thyao_pred['companycode'] = 'THYAO'
df_thyao_pred.rename(columns={'score_predito': 'score_total'}, inplace=True)

# Substituir os dados de THYAO no gráfico anterior pelos previstos
df_comparacao_previsto = df[df['companycode'].isin([melhor_empresa, pior_empresa])].copy()
df_comparacao_previsto = pd.concat([df_comparacao_previsto, df_thyao_pred], ignore_index=True)

# Plotar
plt.figure(figsize=(14, 7))
sns.lineplot(
    data=df_comparacao_previsto,
    x='data',
    y='score_total',
    hue='companycode',
    palette=paleta_cores,
    hue_order=ordem_empresas,
    linewidth=2.5
)

plt.title('Score Previsto de THYAO vs. Melhor e Pior do Mercado', fontsize=16)
plt.ylabel('Score Total (0 a 5)', fontsize=12)
plt.xlabel('Ano', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Empresa', loc='upper right')
plt.axhspan(4, 5, color='green', alpha=0.05)
plt.axhspan(0, 2, color='red', alpha=0.05)
plt.tight_layout()
plt.show()


# %%
# Criar uma cópia do DataFrame original
df_sem_thyao = df[df['companycode'] != 'THYAO'].copy()

# Verificar que THYAO foi removido
print("THYAO removido?", 'THYAO' in df_sem_thyao['companycode'].unique())

# %%
df_sem_thyao

# %%
# Separar treino e teste com base em data (2023 como holdout)
df_train = df_sem_thyao[df_sem_thyao['data'] < '2023-01-01']
df_test  = df_sem_thyao[df_sem_thyao['data'] >= '2023-01-01']

# Definir colunas de features
feat = df_train.drop(columns=['score_total', 'companycode', 'ano', 'periodo', 'data']).columns.tolist()

# Criar conjuntos
X_train = df_train[feat]
y_train = df_train['score_total']
X_test  = df_test[feat]
y_test  = df_test['score_total']

# Treinar modelo
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

model_holdout = RandomForestRegressor(random_state=42)
model_holdout.fit(X_train, y_train)

# Avaliar
y_pred = model_holdout.predict(X_test)
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("🔍 Holdout - Validação com Empresas (exceto THYAO):")
print(f"MAE: {mae:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")


# %%
# Prever THYAO com modelo que nunca a viu
df_thyao = df[df['companycode'] == 'THYAO'].copy()
X_thyao = df_thyao[feat]
df_thyao['score_predito'] = model_holdout.predict(X_thyao)


# %%
plt.figure(figsize=(14, 6))
plt.plot(df_thyao['data'], df_thyao['score_total'], label='Real', color='blue', linewidth=2)
plt.plot(df_thyao['data'], df_thyao['score_predito'], label='Previsto', color='orange', linestyle='--', linewidth=2)
plt.title('Comparação: Score Total Real vs Previsto - THYAO (Modelo sem ver THYAO)')
plt.xlabel('Ano')
plt.ylabel('Score Total (0 a 5)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# %%
# Selecionar empresas extremas
ranking = df.groupby('companycode')['score_total'].mean().sort_values(ascending=False)
melhor_empresa = ranking.index[0] if ranking.index[0] != 'THYAO' else ranking.index[1]
pior_empresa = ranking.index[-1] if ranking.index[-1] != 'THYAO' else ranking.index[-2]

# Dados reais das outras duas empresas
df_extremos = df[df['companycode'].isin([melhor_empresa, pior_empresa])].copy()

# Substituir dados reais de THYAO pelo previsto
df_thyao_prev = df_thyao[['data', 'score_predito']].copy()
df_thyao_prev['companycode'] = 'THYAO'
df_thyao_prev.rename(columns={'score_predito': 'score_total'}, inplace=True)

# Combinar os três
df_final = pd.concat([df_extremos, df_thyao_prev], ignore_index=True)

# Plotar
plt.figure(figsize=(14, 7))
sns.lineplot(
    data=df_final,
    x='data',
    y='score_total',
    hue='companycode',
    palette={melhor_empresa: 'green', 'THYAO': 'blue', pior_empresa: 'red'},
    hue_order=[melhor_empresa, 'THYAO', pior_empresa],
    linewidth=2.5
)
plt.title('THYAO Previsto vs Benchmark Positivo e Negativo')
plt.axhspan(4, 5, color='green', alpha=0.05)
plt.axhspan(0, 2, color='red', alpha=0.05)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylabel('Score Total (0 a 5)')
plt.xlabel('Ano')
plt.tight_layout()
plt.show()


# %%
# Selecionar empresas extremas
ranking = df.groupby('companycode')['score_total'].mean().sort_values(ascending=False)
melhor_empresa = ranking.index[0] if ranking.index[0] != 'THYAO' else ranking.index[1]
pior_empresa = ranking.index[-1] if ranking.index[-1] != 'THYAO' else ranking.index[-2]

# Dados reais das outras duas empresas
df_extremos = df[df['companycode'].isin([melhor_empresa, pior_empresa])].copy()

# Substituir dados reais de THYAO pelo previsto
df_thyao_prev = df_thyao[['data', 'score_predito']].copy()
df_thyao_prev['companycode'] = 'THYAO'
df_thyao_prev.rename(columns={'score_predito': 'score_total'}, inplace=True)

# Combinar os três
df_final = pd.concat([df_extremos, df_thyao_prev], ignore_index=True)

# Plotar
plt.figure(figsize=(14, 7))
sns.lineplot(
    data=df_final,
    x='data',
    y='score_total',
    hue='companycode',
    palette={melhor_empresa: 'green', 'THYAO': 'blue', pior_empresa: 'red'},
    hue_order=[melhor_empresa, 'THYAO', pior_empresa],
    linewidth=2.5
)
plt.title('THYAO Previsto vs Benchmark Positivo e Negativo')
plt.axhspan(4, 5, color='green', alpha=0.05)
plt.axhspan(0, 2, color='red', alpha=0.05)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylabel('Score Total (0 a 5)')
plt.xlabel('Ano')
plt.tight_layout()
plt.show()



