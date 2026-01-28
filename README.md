# Análise de Crédito PJ com Machine Learning
Este projeto desenvolve um modelo preditivo para mensurar o risco de crédito de Pessoas Jurídicas (PJ) utilizando **Machine Learning**. Diferente das abordagens tradicionais de classificação binária (Inadimplente/Não Inadimplente), este projeto propõe um **Score de Crédito Contínuo (0 a 5)**, permitindo uma análise de granularidade fina sobre a saúde financeira das empresas.

## Planejamento Inicial
* Extrair os dados do Kaggle - ok
* Construir um banco de dados SQLite - ok 
* Extrair do banco o maior periodo de empresas com dados durante os mesmos anos. - ok
* Tirar um Dataset do BD - ok
* Entendimento dos Dados Contexto Financeiro - ok
* Limpeza e Análise do Dataset - ok
* Engenharia de Features - ok
* Exploração dos Dados - ok
* Visualização dos Dados com Gráficos e Dashboards - ok
* Modelagem - ok
* Validação - ok
* SHAP para explicaçaõ do Modelo - ok

## 1. Contexto Financeiro
A análise de crédito é vital para mitigar riscos de inadimplência e garantir a sustentabilidade do sistema financeiro. No entanto, modelos tradicionais muitas vezes falham em capturar a **não linearidade** dos indicadores financeiros.

A abordagem deste projeto utiliza algoritmos de *Ensemble* (Random Forest) para prever um score de risco baseado em demonstrações financeiras auditadas. O modelo prioriza a capacidade de geração de caixa e solvência sobre o tamanho absoluto da empresa, alinhando-se à teoria financeira moderna.

## 2. Fonte de Dados
Os dados utilizados referem-se a empresas públicas da **Turquia**, escolhidas pela disponibilidade e transparência, servindo como *proxy* para mercados emergentes.

*   **Fonte Original:** Plataforma de Transparência Pública da Turquia [KAP](https://kap.org.tr/) .
*   **Repositório:** [Kaggle](https://www.kaggle.com/datasets/agrafintech/turkish-public-companies-balance-sheets-from-kap). ("Turkish Public Companies Balance Sheets from KAP").
*   **Volume:** Demonstrações financeiras de **227 empresas** abrangendo o período de **2008 a 2024**,.
*   **Estrutura:** Os dados brutos foram consolidados via script Python em um banco SQLite e posteriormente transformados em formato tabular (`csv`) para análise.

## 3. Metodologia de Avaliação de Scores (Target)
Como a base de dados não possuía um rótulo confiável de "inadimplência" (default), foi construída uma variável alvo (*Target*) sintética baseada na metodologia de **Joel Bessis** (*Risk Management in Banking*) e literatura financeira clássica.

O **Score Total** é uma média ponderada de 6 dimensões financeiras, onde cada dimensão recebe uma nota de 0 a 5 baseada em *thresholds* de mercado:

$$ Score = (S_{Liq} \times 0.15) + (S_{Alav} \times 0.20) + (S_{Rent} \times 0.20) + (S_{Ret} \times 0.15) + (S_{Efic} \times 0.20) + (S_{Cic} \times 0.10) $$

*Os pesos foram definidos para priorizar a solvência (Alavancagem/Eficiência) sobre a liquidez imediata.*

## 4. Engenharia de Atributos (Feature Engineering)
A partir de 27 contas contábeis brutas (Ativos, Passivos, Receita, etc.), foram gerados **49 indicadores financeiros** (ratios). A escolha por *ratios* em vez de valores absolutos é crucial para eliminar o viés de tamanho da empresa (magnitude).

### Principais Atributos Criados:

| Categoria | Principais Indicadores | Por que foram escolhidos? |
| :--- | :--- | :--- |
| **Eficiência Operacional** | **EBITDA/Dívida**, Cobertura de Juros | **Cruciais:** Medem a capacidade real da empresa gerar caixa para pagar suas dívidas. O SHAP revelou que o `ebitda_divida` é o fator mais importante do modelo. |
| **Liquidez** | Liquidez Corrente, **Liquidez Seca** | Avaliam a capacidade de pagamento de curto prazo. A Liquidez Seca foi selecionada por excluir estoques, oferecendo uma visão mais conservadora da solvência imediata. |
| **Rentabilidade** | Margem Líquida, Margem EBITDA | Indicam a eficiência da gestão em converter vendas em lucro real, essencial para a continuidade do negócio. |
| **Retornos** | **ROA** (Retorno sobre Ativos), ROE | Medem o retorno sobre o investimento. O ROA demonstrou alta correlação com o score final, indicando qualidade na gestão dos ativos. |
| **Alavancagem** | Dívida/Patrimônio, Endividamento Total | Indicam o nível de risco e dependência de capital de terceiros. Foram usados para penalizar empresas excessivamente endividadas. |
| **Ciclos** | Ciclo de Estoques, Recebíveis | Medem a velocidade da operação. Têm peso menor no score final (10%), servindo para ajuste fino da eficiência operacional. |

## 5. Resultados do Modelo
O projeto comparou Regressão Linear com Random Forest, validando a complexidade não linear dos dados.

*   **Modelo Campeão:** Random Forest Regressor.
*   **Performance:** R² de **0.97** e MAE de **0.06**.
*   **Validação:** Testado via *Cross-Validation* (K-Fold) e *Blind Test* temporal (ano de 2024) e por entidade (Caso *Turkish Airlines*), demonstrando alta capacidade de generalização sem *overfitting*.

*Autor: Lucas Gregório Silva - TCC MBA em Ciência de Dados (USP/ICMC)*