# ChallengeAluraStore

# 🛍️ Desafio Alura Store – Análise de Lojas

## 📌 Objetivo

Este projeto tem como missão auxiliar o Senhor João, dono da rede **Alura Store**, a decidir **qual das suas quatro lojas vender** para iniciar um novo empreendimento. Com base em dados reais de vendas, avaliações, frete e localização, realizamos uma análise detalhada e visual dos dados para tomar a melhor decisão.

---

## 🔍 O que foi analisado

Utilizando a biblioteca **Pandas** para tratamento de dados e **Matplotlib** para visualizações, exploramos as seguintes métricas:

- **💰 Faturamento total** de cada loja
- **📦 Vendas por categoria de produto**
- **⭐ Média de avaliação dos clientes**
- **📈 Produtos mais e menos vendidos**
- **🚚 Frete médio por loja**
- **🗺️ Desempenho geográfico** com dados de latitude e longitude

---

## 📊 Gráficos Gerados

### 1. **Faturamento Total por Loja**
> Gráfico de barras verticais destacando o total vendido por cada loja.

### 2. **Vendas por Categoria**
> Gráficos de pizza (um para cada loja) + um gráfico adicional com a **média de vendas por categoria** entre todas as lojas.

### 3. **Média de Avaliações**
> Gráfico de dispersão comparando a satisfação dos clientes de cada loja.

### 4. **Produtos Mais e Menos Vendidos**
> Gráfico de barras horizontais para identificar os produtos com maior e menor saída por loja.

### 5. **Frete Médio por Loja**
> Gráfico de linha comparando o custo médio de frete entre as lojas.

### 6. **Distribuição Geográfica das Vendas**
> Gráfico de dispersão com coordenadas geográficas das transações (latitude e longitude), indicando o alcance de vendas por loja.

---

## 📈 Principais Resultados

| Loja     | Faturamento     | Avaliação Média | Frete Médio              | Produto Mais Vendido     |
|----------|-----------------|-----------------|--------------------------|--------------------------|
| Loja 1   | R$ 1.534.509,12 | 3,98            | R$ 34,69                 | TV Led UHD 4K            |
| Loja 2   | R$ 1.488.459,06 | 4,04            | R$ 33,62                 | Iniciando em programação |
| Loja 3   | R$ 1.464.025,03 | *4,05 (melhor)* | R$ 33,07                 | Kit banquetas            |
| Loja 4   | R$ 1.384.497,58 | 4,00            | *R$ 31,28 (menor custo)* | Cama box                 |

---

## ✅Resumo das Análises:

- Faturamento: Loja 4 teve o pior desempenho de vendas.
- Avaliações: Loja 3 é a mais bem avaliada; Loja 1 é a mais criticada.
- Produtos: Loja 4 teve os produtos menos vendidos em geral.
- Frete: Loja 4 tem o menor custo de frete, o que é positivo.
- Distribuição Geográfica:
  - As vendas estão distribuídas em várias regiões do Brasil.
  - Loja 1 e Loja 2 têm maior abrangência geográfica.
  - Loja 4 possui menor densidade geográfica de vendas.
  - Loja 4 atua em menos regiões do que as demais.

## ✅ Recomendação Final

> Com base nos dados, a Loja 4 apresenta o pior desempenho geral:
  - Menor faturamento total
  - Menor média de avaliação (exceto Loja 1)
  - Menor valor de frete (positivo, mas insuficiente para compensar)
  - Vendas por categoria não se destacam
  - Produtos mais vendidos têm pouca diferença de volume em relação aos menos vendidos, indicando baixa performance comercial diferenciada.

## ✅ Recomendação:

> Recomendamos considerar **vender a Loja 4**, pois ela é a que apresenta menor eficiência nos principais indicadores analisados: faturamento, avaliação dos clientes e diversidade de produtos vendidos.
