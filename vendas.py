import streamlit as st
import pandas as pd
import plotly.express as px
# títulos
st.write("# Sistema de vendas")

tabela_vendas = pd.read_csv("vendas.csv")

# Cadastro de vendas
st.sidebar.write("##Cadastrar Vendas")

data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Alessandra", "Angeluz", "André"])
produto = st.sidebar.selectbox("Produto", ["Computador", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor", step=0.5)
botao_cadastrar = st.sidebar.button ("Cadastrar")

#logica do botão
if botao_cadastrar:
    if valor <= 0 or vendedor == "" or produto == "" or quantidade <= 0:
        st.warning("Cadastro incompleto")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada!")

# Seção de visualizar vendas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)

# Seção de Dashboard
st.write("## Dashboard")

faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total",f"R$ {faturamento}")

#gráficos
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)