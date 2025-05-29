# ChallengeAluraStore

# 🛍️ Desafio Alura Store – Análise de Lojas

## 📌 Objetivo

Este projeto tem como missão auxiliar o Senhor João, dono da rede **Alura Store**, a decidir **qual das suas quatro lojas vender** para iniciar um novo empreendimento. Com base em dados reais de vendas, avaliações e frete, realizamos uma análise detalhada e visual dos dados para tomar a melhor decisão.

---

# 🧾 Sumário
- 🔍 Visão Geral
- 🔍 O que foi analisado
- 📊 Gráficos Gerados
- 📈 Principais Resultados
- ✅ Resumo das Análises
- 🧠 Conclusões
- 🧠 Tecnologias Utilizadas
- ☁️ Como Executar no Google Colab
- 📫 Contato
  
---

# 🔍 Visão Geral

Os dados analisados abrangem as seguintes colunas por loja:

- Produto, Categoria, Preço, Avaliação, Frete, lat, lon (coordenadas geográficas dos clientes)

Cada loja possui um arquivo .csv com seu histórico de vendas.

---

## 🔍 O que foi analisado

Utilizando a biblioteca **Pandas** para tratamento de dados e **Matplotlib** para visualizações, foram exploradas as seguintes métricas:

- **💰 Faturamento total** de cada loja
- **📦 Vendas por categoria de produto** por loja
- **⭐ Média de avaliação dos clientes** por loja
- **📈 Produtos mais vendidos e produtos menos vendidos** por loja
- **🚚 Frete médio** por loja

---

## 📊 Gráficos Gerados

### 1. **Faturamento Total por Loja**
> Gráfico de barras verticais destacando o total vendido por cada loja.

![image](https://github.com/user-attachments/assets/d529f560-c2b6-43f5-9d1d-3439d0576bbe)

### 2. **Vendas por Categoria**
> Gráficos de pizza (um para cada loja) + um gráfico adicional com a **média de vendas por categoria** entre todas as lojas.

![image](https://github.com/user-attachments/assets/e2241eb5-7600-4bcd-a121-b3e7825697ce)

### 3. **Média de Avaliações**
> Gráfico de dispersão comparando a satisfação dos clientes de cada loja.

![image](https://github.com/user-attachments/assets/cb151821-d920-48a0-bafa-5e8e846750de)

### 4. **Produtos Mais e Menos Vendidos**
> Gráfico de barras horizontais para identificar os produtos com maior e menor saída por loja.

![image](https://github.com/user-attachments/assets/1a91a4a1-6d97-478c-a9a6-7c3645121cd8)

### 5. **Frete Médio por Loja**
> Gráfico de linha comparando o custo médio de frete entre as lojas.

![image](https://github.com/user-attachments/assets/5e569452-bf0d-4fac-a052-32d084337d8a)

---

## 📈 Principais Resultados

| Loja     | Faturamento     | Avaliação Média | Frete Médio              | Produto Mais Vendido     |
|----------|-----------------|-----------------|--------------------------|--------------------------|
| Loja 1   | R$ 1.534.509,12 | 3,98            | R$ 34,69                 | Micro-ondas              |
| Loja 2   | R$ 1.488.459,06 | 4,04            | R$ 33,62                 | Iniciando em programação |
| Loja 3   | R$ 1.464.025,03 | *4,05 (melhor)* | R$ 33,07                 | Kit banquetas            |
| Loja 4   | R$ 1.384.497,58 | 4,00            | *R$ 31,28 (menor custo)* | Cama box                 |

---

## ✅Resumo das Análises:

- Faturamento: Loja 4 teve o pior desempenho de vendas.
- Avaliações: Loja 3 é a mais bem avaliada; Loja 1 é a mais criticada.
- Produtos: Loja 4 teve os produtos menos vendidos em geral.
- Frete: Loja 4 tem o menor custo de frete.

## 🧠 Conclusões

> Com base nos dados, a Loja 4 apresenta o pior desempenho geral:
  - Menor faturamento total
  - Menor média de avaliação (exceto Loja 1)
  - Menor valor de frete (positivo, mas insuficiente para compensar)
  - Vendas por categoria não se destacam
  - Produtos mais vendidos têm pouca diferença de volume em relação aos menos vendidos, indicando baixa performance comercial diferenciada.

## ✅ Recomendação:

> Recomendamos considerar **vender a Loja 4**, pois ela é a que apresenta menor eficiência nos principais indicadores analisados:
### 1. Menor Faturamento Geral
  - Com o pior desempenho em receita total, manter essa loja representa menor retorno financeiro.

### 2. Vendas mais fracas por produto
  - Os produtos da Loja 4 apresentam menor volume de vendas, indicando menor giro de estoque.

### 3. Frete mais barato não compensa a baixa performance
  - Apesar do frete ser o mais barato, isso não está se convertendo em vantagem competitiva ou maior volume de vendas.

### 4. Avaliação apenas mediana
  - A avaliação dos clientes é estável, mas não compensa os pontos negativos em faturamento e desempenho de produto.

---

# 🧠 Tecnologias Utilizadas

   - Python
   - Pandas
   - Matplotlib
   - Google Colab

---

# ☁️ Como Executar no Google Colab

Você pode rodar este projeto diretamente no navegador usando o Google Colab, sem precisar instalar nada no seu computador.

**Passos:**
**1. Acesse o Google Colab:**

  - [Clique aqui para acessar]https://colab.research.google.com/

**2. Abra o notebook do projeto:**
  - Clique em **"Arquivo"** > **"Abrir notebook"**
  - Vá até a aba **"Upload"** e envie o arquivo **AluraStoreBr_completo.ipynb**

**3.Execute todas as células do notebook:**
  - Vá em **"Ambiente de Execução"** > **"Executar tudo"** para rodar o notebook completo.

**5. Pronto!**
  Os gráficos e análises serão gerados automaticamente.

---

# 📫 Contato
Dúvidas ou sugestões? Entre em contato:

 📧 Email: mequiasjunior@gmail.com

 💼 LinkedIn: [Mequias Júnior](https://www.linkedin.com/in/mequiasjunior/)
