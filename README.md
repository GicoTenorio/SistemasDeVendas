# 📊 Sistema de Vendas

Sistema de vendas desenvolvido em **Python** utilizando **Streamlit**, **Pandas** e **Plotly**.

O projeto permite cadastrar vendas, visualizar os registros cadastrados e acompanhar informações sobre o faturamento por meio de um dashboard interativo.

## 📌 Sobre o projeto

O sistema foi desenvolvido para praticar conceitos de desenvolvimento de aplicações web com Python e manipulação de dados.

A aplicação possui:

- Cadastro de novas vendas;
- Seleção de vendedor e produto;
- Definição de quantidade e valor;
- Validação dos dados cadastrados;
- Armazenamento das vendas em um arquivo CSV;
- Visualização das vendas cadastradas;
- Cálculo do faturamento total;
- Gráficos para análise das vendas.

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 🎨 **Streamlit**
- 📊 **Pandas**
- 📈 **Plotly**
- 📄 **CSV**

## ⚙️ Funcionalidades

### 📝 Cadastro de vendas

O usuário pode cadastrar uma venda através da barra lateral da aplicação, informando:

- Data;
- Vendedor;
- Produto;
- Quantidade;
- Valor.

Após o preenchimento, basta clicar em **Cadastrar**.

O sistema também verifica se os dados obrigatórios foram preenchidos corretamente.

### 📋 Visualização das vendas

As vendas cadastradas são exibidas em uma tabela através do `st.dataframe()`.

Os dados são armazenados no arquivo:

```text
vendas.csv
```

### 💰 Faturamento

O sistema calcula automaticamente o faturamento total utilizando os valores cadastrados:

```python
faturamento = tabela_vendas["valor"].sum()
```

O resultado é apresentado através de uma métrica no dashboard.

### 📊 Dashboard

O projeto possui dois gráficos:

**Gráfico de barras:** apresenta os valores das vendas por vendedor e produto.

**Gráfico de pizza:** apresenta a distribuição do valor das vendas por produto.

Os gráficos são criados utilizando a biblioteca Plotly.

## 📂 Estrutura do projeto

```text
📁 sistema-vendas/
├── 📄 vendas.py
├── 📄 vendas.csv
└── 📄 README.md
```

## 📄 Estrutura do CSV

O arquivo `vendas.csv` deve possuir as seguintes colunas:

```text
data
vendedor
produto
quantidade
valor
```

Exemplo:

```csv
data,vendedor,produto,quantidade,valor
2026-10-10,Alessandra,Computador,2,5000
2026-10-10,Angeluz,Celular,3,3000
2026-10-10,André,Fone,5,750
```

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd sistema-vendas
```

### 3. Instale as dependências

```bash
pip install streamlit pandas plotly
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

Depois disso, o Streamlit abrirá o sistema no navegador.

## 🎯 Objetivo

O objetivo do projeto é desenvolver uma aplicação simples de gerenciamento e análise de vendas, praticando:

- Manipulação de dados com Pandas;
- Criação de interfaces com Streamlit;
- Leitura e escrita de arquivos CSV;
- Criação de gráficos com Plotly;
- Criação de dashboards;
- Estruturas condicionais em Python.

## 👨‍💻 Autor

Projeto desenvolvido para estudos de **Python, análise de dados, Streamlit e criação de dashboards**.
