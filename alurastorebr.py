### Importação dos dados

import pandas as pd
import matplotlib.pyplot as plt

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja1 = pd.read_csv(url1)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja1.head()


#1. Análise do faturamento
# Faturamento total de cada loja
faturamentos = {
    "Loja 1": loja1["Preço"].sum(),
    "Loja 2": loja2["Preço"].sum(),
    "Loja 3": loja3["Preço"].sum(),
    "Loja 4": loja4["Preço"].sum(),
}
faturamento_df = pd.DataFrame(list(faturamentos.items()), columns=["Loja", "Faturamento"])
faturamento_df["Faturamento"] = faturamento_df["Faturamento"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(faturamento_df)

# Gráfico de barras - Faturamento
faturamento_valores = [loja1['Preço'].sum(), loja2['Preço'].sum(), loja3['Preço'].sum(), loja4['Preço'].sum()]
labels = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']

fig, ax = plt.subplots(figsize=(8, 6))
barras = ax.bar(labels, faturamento_valores, color=['blue', 'green', 'red', 'orange'])

# Rótulo com valor formatado em R$
for bar, valor in zip(barras, faturamento_valores):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
            f'R$ {valor:,.2f}'.replace('.', ',').replace(',', '.', 1),
            ha='center', va='bottom', fontsize=10)

ax.set_title('Faturamento Total por Loja')
ax.set_ylabel('Valor (R$)')
plt.tight_layout()
plt.show()

# 2. Vendas por Categoria

def vendas_por_categoria(df, loja_nome):
    categorias = df['Categoria do Produto'].value_counts().reset_index()
    categorias.columns = ['Categoria', 'Quantidade']
    categorias['Loja'] = loja_nome
    return categorias

vendas_cat1 = vendas_por_categoria(loja1, 'Loja 1')
vendas_cat2 = vendas_por_categoria(loja2, 'Loja 2')
vendas_cat3 = vendas_por_categoria(loja3, 'Loja 3')
vendas_cat4 = vendas_por_categoria(loja4, 'Loja 4')
print(vendas_cat1)
print(vendas_cat2)
print(vendas_cat3) 
print(vendas_cat4)

# 5 gráficos de pizza: 4 por loja + 1 média geral
fig, axs = plt.subplots(3, 2, figsize=(14, 15))

# Dados individuias
lojas_categorias = [vendas_cat1, vendas_cat2, vendas_cat3, vendas_cat4]
titulos = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']

for ax, dados, titulo in zip(axs.flatten()[:4], lojas_categorias, titulos):
    ax.pie(dados['Quantidade'], labels=dados['Categoria'], autopct='%1.1f%%', startangle=90)
    ax.set_title(f'Vendas por Categoria - {titulo}')

# Soma de todas as quantidades por categoria
todas_categorias = pd.concat(lojas_categorias)
soma_categorias = todas_categorias.groupby('Categoria')['Quantidade'].sum()
media_categorias = soma_categorias / len(lojas_categorias)  # Divide pelo número de lojas

# Grafico de pizza com média
ax_media = axs[2, 0]
ax_media.pie(media_categorias, labels=media_categorias.index, autopct='%1.1f%%', startangle=90)
ax_media.set_title('Média de Vendas por Categoria (Todas as Lojas)')

axs[2, 1].axis('off')
plt.tight_layout()
plt.show()

# 3. Média de Avaliação das Lojas

avaliacoes = {
    'Loja 1': round(loja1['Avaliação da compra'].mean(), 2),
    'Loja 2': round(loja2['Avaliação da compra'].mean(), 2),
    'Loja 3': round(loja3['Avaliação da compra'].mean(), 2),
    'Loja 4': round(loja4['Avaliação da compra'].mean(), 2)
}
avaliacoes_df = pd.DataFrame(list(avaliacoes.items()), columns=['Loja', 'Média de Avaliação'])
print(avaliacoes_df)

# Gráfico das avaliações
cores = ['orange', 'green', 'blue', 'purple']

plt.figure(figsize=(8, 5))

for i, row in avaliacoes_df.iterrows():
    plt.scatter(row['Loja'], row['Média de Avaliação'], color=cores[i], s=100, label=row['Loja'])
    plt.text(row['Loja'], row['Média de Avaliação'] + 0.1,
             f"{row['Média de Avaliação']:.2f}",
             ha='center', va='bottom', fontsize=10, fontweight='bold', color=cores[i])

plt.ylim(0, 5.1)
plt.title('Média de Avaliação por Loja')
plt.xlabel('Lojas')
plt.ylabel('Média da Avaliação')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.legend(title='Lojas')
plt.show()

# 4. Produtos Mais e Menos Vendidos

def mais_menos_vendidos(df, loja_nome):
    produto_vendas = df['Produto'].value_counts().reset_index()
    produto_vendas.columns = ['Produto', 'Quantidade']
    mais_vendido = produto_vendas.iloc[0]
    menos_vendido = produto_vendas.iloc[-1]
    return loja_nome, mais_vendido['Produto'], mais_vendido['Quantidade'], menos_vendido['Produto'], menos_vendido['Quantidade']

dados_vendas = [
    mais_menos_vendidos(loja1, 'Loja 1'),
    mais_menos_vendidos(loja2, 'Loja 2'),
    mais_menos_vendidos(loja3, 'Loja 3'),
    mais_menos_vendidos(loja4, 'Loja 4')
]

vendas_df = pd.DataFrame(dados_vendas, columns=['Loja', 'Mais Vendido', 'Qtd Mais Vendido', 'Menos Vendido', 'Qtd Menos Vendido'])
print(vendas_df)

# Gráfico produtos mais e menos vendidos

def produtos_extremos(df, loja_nome):
    contagem = df['Produto'].value_counts().reset_index()
    contagem.columns = ['Produto', 'Quantidade']
    return contagem.head(1), contagem.tail(1)

# Coletar os produtos mais e menos vendidos para cada loja
produtos_extremos_dados = {
    'Loja 1': produtos_extremos(loja1, 'Loja 1'),
    'Loja 2': produtos_extremos(loja2, 'Loja 2'),
    'Loja 3': produtos_extremos(loja3, 'Loja 3'),
    'Loja 4': produtos_extremos(loja4, 'Loja 4'),
}

# Organizar os dados para plotagem
mais_vendidos = pd.concat([v[0].assign(Loja=k) for k, v in produtos_extremos_dados.items()])
menos_vendidos = pd.concat([v[1].assign(Loja=k) for k, v in produtos_extremos_dados.items()])

# Criar gráfico de barras horizontais
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Mais vendidos
axs[0].barh(mais_vendidos['Produto'] + " - " + mais_vendidos['Loja'], mais_vendidos['Quantidade'], color='blue')
axs[0].set_title('Mais Vendidos por Loja')
axs[0].set_xlabel('Quantidade')
axs[0].invert_yaxis()

# Menos vendidos
axs[1].barh(menos_vendidos['Produto'] + " - " + menos_vendidos['Loja'], menos_vendidos['Quantidade'], color='red')
axs[1].set_title('Menos Vendidos por Loja')
axs[1].set_xlabel('Quantidade')
axs[1].invert_yaxis()

plt.tight_layout()
plt.show()

# 5. Frete Médio por Loja

frete_medio = {
    'Loja 1': round(loja1['Frete'].mean(), 2),
    'Loja 2': round(loja2['Frete'].mean(), 2),
    'Loja 3': round(loja3['Frete'].mean(), 2),
    'Loja 4': round(loja4['Frete'].mean(), 2)
}

frete_medio_df = pd.DataFrame(list(frete_medio.items()), columns=['Loja', 'Frete Médio'])

# Formatando os valores em reais (R$)
frete_medio_df['Frete Médio'] = frete_medio_df['Frete Médio'].apply(lambda x: f'R$ {x:,.2f}'.replace('.', ',').replace(',', '.', 1))
print(frete_medio_df)

frete_medio_valores = [loja1['Frete'].mean(), loja2['Frete'].mean(), loja3['Frete'].mean(), loja4['Frete'].mean()]
labels = ['Loja 1', 'Loja 2', 'Loja 3', 'Loja 4']

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(labels, frete_medio_valores, marker='o', linestyle='-', color='purple')

# Adiciona rótulo com valor formatado em R$
for x, y in zip(labels, frete_medio_valores):
    ax.text(x, y, f'R$ {y:,.2f}'.replace('.', ',').replace(',', '.', 1), ha='center', va='bottom')

ax.set_title('Frete Médio por Loja')
ax.set_ylabel('Valor (R$)')
plt.tight_layout()
plt.show()