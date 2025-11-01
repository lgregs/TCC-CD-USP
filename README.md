# Projeto de Análise de Dados e Concessão de Crédito
* MBA Ciência de Dados - USP ICMC São Carlos

* Dados retirados do [Kaggle](https://www.kaggle.com/datasets/agrafintech/turkish-public-companies-balance-sheets-from-kap).
* Também podem ser encontrados em [KAP](https://kap.org.tr/).

## Planejamento Inicial
* Extrair os dados do Kaggle - ok
* Construir um banco de dados SQLite - ok 
* Extrair do banco o maior periodo de empresas com dados durante os mesmos anos. - ok
* Tirar um Dataset do BD - ok
* Entendimento dos Dados Contexto Financeiro - ok
* Limpeza e Análise do Dataset - ok
* Engenharia de Features - em andamento ...
* Exploração dos Dados - por fazer
* Visualização dos Dados com Gráficos e Dashboards - por fazer
* Modelagem - por fazer
* Validação - por fazer 
* SHAP para explicaçaõ do Modelo - por fazer

### Engenharia de Dados

---

### **Índices de Liquidez** (saúde financeira de curto prazo)

| Índice                          | Fórmula                                                                       | Significado                                                                                            |
| ------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Índice de Liquidez Corrente** | Ativos Circulantes / Passivos Circulantes                                     | Mede se a empresa consegue pagar suas dívidas de curto prazo com ativos de curto prazo. >1 é saudável. |
| **Índice de Liquidez Seca**     | (Caixa + Contas a Receber + Outros Ativos Circulantes) / Passivos Circulantes | Igual ao índice corrente, mas exclui os estoques — mostra a *liquidez imediata*.                       |

 **Por que importa:** Alta liquidez reduz o risco de inadimplência. O índice seco é mais conservador.

---

###  **Índices de Alavancagem** (endividamento e solvência)

| Índice                                       | Fórmula                                  | Significado                                                                    |
| -------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------ |
| **Dívida sobre Patrimônio (Debt-to-Equity)** | Dívidas Financeiras / Patrimônio Líquido | Compara capital de terceiros com o capital próprio — mede risco financeiro.    |
| **Dívida sobre Ativos (Debt-to-Assets)**     | Dívidas Financeiras / Total de Ativos    | Percentual dos ativos financiados por dívida — quanto maior, mais alavancagem. |

 **Por que importa:** Alta alavancagem = maior risco de inadimplência, mas alavancagem moderada = uso eficiente do capital.

---

###  **Índices de Rentabilidade** (capacidade de gerar lucro)

| Índice                                     | Fórmula                               | Significado                                                               |
| ------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------- |
| **ROE (Retorno sobre Patrimônio Líquido)** | Lucro Líquido / Patrimônio Líquido    | Mede o retorno para os acionistas — eficiência no uso do capital próprio. |
| **ROA (Retorno sobre Ativos)**             | Lucro Líquido / Total de Ativos       | Avalia a eficiência dos ativos em gerar lucro.                            |
| **Margem Líquida**                         | Lucro Líquido / Receita de Vendas     | Percentual da receita que vira lucro líquido — lucratividade geral.       |
| **Margem Operacional**                     | Lucro Operacional / Receita de Vendas | Lucratividade das operações principais antes de juros e impostos.         |

 **Por que importa:** Mostra força e eficiência operacional — empresas lucrativas resistem melhor a crises.

---

###  **Índices de Eficiência** (desempenho operacional)

| Índice                       | Fórmula                                | Significado                                                                             |
| ---------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------- |
| **Giro do Ativo**            | Receita de Vendas / Total de Ativos    | Mede quão eficientemente os ativos geram vendas.                                        |
| **Giro de Estoques**         | Custo dos Produtos Vendidos / Estoques | Mede a velocidade de venda dos estoques — alto = eficiente, baixo = excesso de estoque. |
| **Giro de Contas a Receber** | Receita de Vendas / Contas a Receber   | Mede a rapidez dos recebimentos — alto = bom gerenciamento de caixa.                    |

 **Por que importa:** Mostra quão bem a empresa utiliza seus recursos para gerar receita e fluxo de caixa.

---

###  **Índices de Cobertura** (capacidade de pagamento da dívida)

| Índice                                     | Fórmula                                  | Significado                                             |
| ------------------------------------------ | ---------------------------------------- | ------------------------------------------------------- |
| **Cobertura de Juros (Interest Coverage)** | Lucro Operacional / Despesas Financeiras | Mede quantas vezes o lucro cobre as despesas com juros. |

 **Por que importa:** Baixa cobertura = dificuldade em pagar dívidas → sinal precoce de estresse financeiro.

---

###  **Índices de Crescimento** (momentum e tendência)

| Índice                           | Fórmula                          | Significado                              |
| -------------------------------- | -------------------------------- | ---------------------------------------- |
| **Crescimento das Vendas**       | Δ Receita de Vendas / Receitaₜ₋₁ | Mede o crescimento da receita ano a ano. |
| **Crescimento dos Ativos**       | Δ Total de Ativos / Ativosₜ₋₁    | Mostra a expansão dos recursos totais.   |
| **Crescimento do Lucro Líquido** | Δ Lucro Líquido / Lucroₜ₋₁       | Indica a tendência de lucratividade.     |

 **Por que importa:** Crescimento consistente indica uma empresa saudável e em expansão — bom sinal para estabilidade de crédito.

---

###  **Solvência e Estabilidade**

| Índice                                    | Fórmula                                   | Significado                                                                           |
| ----------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------- |
| **Lucros Retidos sobre Ativos**           | Lucros Acumulados / Total de Ativos       | Percentual de ativos financiados por lucros passados — mede solvência de longo prazo. |
| **Posição Cambial Líquida (FX Position)** | Posição Cambial Líquida / Total de Ativos | Mede exposição cambial — valores negativos = risco de câmbio.                         |

 **Por que importa:** Lucros retidos = força interna; exposição cambial = vulnerabilidade a choques externos.

---

###  **Resumo**

Cada índice revela **quão forte ou frágil** é uma empresa sob um aspecto específico:

| Área Financeira | O que Responde                               |
| --------------- | -------------------------------------------- |
| Liquidez        | A empresa consegue pagar as contas em breve? |
| Alavancagem     | Está excessivamente endividada?              |
| Rentabilidade   | Está realmente gerando lucro?                |
| Eficiência      | Usa bem seus recursos?                       |
| Cobertura       | Consegue pagar os juros das dívidas?         |
| Crescimento     | Está melhorando com o tempo?                 |
| Solvência       | Possui estabilidade de longo prazo?          |
| Câmbio (FX)     | Está exposta ao risco cambial?               |

---

 **Em resumo:**
Esses índices formam um *check-up financeiro 360°* — mostram **capacidade de pagamento**, **geração de lucro** e **resiliência ao risco** — essenciais para avaliar a probabilidade de inadimplência e a saúde financeira da empresa.

