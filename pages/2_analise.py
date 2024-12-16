import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Despesas",
    page_icon="💸",
    layout="wide"
)

st.markdown("## 💸DESPESAS 2024")
st.markdown("⚠️ Selecione ao menos um dos filtros disponíveis *")
st.sidebar.markdown("")


df_data = st.session_state['data']
meses = df_data["NMMES"].unique().tolist()
unidades = df_data["NMUNIDADEORCAMENTARIA"].unique().tolist()

unidade = st.sidebar.selectbox("Selecionar Unidade", unidades, index=None)
st.sidebar.video("assets/tce.mp4", format="video/mp4", start_time=0,)

st.markdown(f"🔽 Analisando dados de **{unidade or 'Todos'}** ")

mes = st.segmented_control("Meses", meses)

df_filtered = df_data[(df_data["NMMES"] == mes) | (df_data["NMUNIDADEORCAMENTARIA"] == unidade)]

# Calcular KPI
conta_total = df_filtered.shape[0]

total_geral = df_data["VLDESPESA"].sum()
total_geral_format = f"{total_geral:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

total_despesa = df_filtered["VLDESPESA"].sum()
total_despesa_format = f"{total_despesa:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

perc_despesa = total_despesa / total_geral

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Despesa Selecionada (R$)", value=f"{total_despesa_format}", border=True)
col2.metric(label="Despesa Selecionada", value=f"{conta_total:,}".replace(",", "X").replace(".", ",").replace("X", "."),border=True)
col3.metric(label="% Despesa", value=f"{perc_despesa * 100:.2f}%",border=True)

col4.metric(label="Despesa Total (R$)", value=f"{total_geral_format}",border=True)

st.divider()
col1, col2 = st.columns(2)

agrupado_Despesa = df_filtered.groupby("NMELEMENTODESPESA", as_index=False)["VLDESPESA"].sum()
topN_Despesa = agrupado_Despesa.sort_values(by="VLDESPESA", ascending=True).head(10)

col1.markdown("### 🔺 10 Maiores Despesas")
col1.bar_chart(topN_Despesa, x="NMELEMENTODESPESA", y_label="", y="VLDESPESA", use_container_width=True, horizontal=True)
col1.dataframe(topN_Despesa, 
               column_config={
                "NMELEMENTODESPESA": "Elemento",
                "VLDESPESA": "Despesa",
               },
               hide_index=True, use_container_width=True)

agrupado_credor = df_filtered.groupby("NMCREDOR", as_index=False)['VLDESPESA'].sum()
topN_credor = agrupado_credor.nlargest(10, "VLDESPESA")

col2.markdown("### 🔺 10 Maiores Credores")
col2.bar_chart(topN_credor, x="NMCREDOR", y_label="", y="VLDESPESA", use_container_width=True, horizontal=True)
col2.dataframe(topN_credor, 
               column_config={
                "NMCREDOR": "Credor",
                "VLDESPESA": "Despesa",
               },
               hide_index=True, use_container_width=True)

st.divider()

columsView = ["NMUNIDADEORCAMENTARIA", "NMCREDOR", "NMELEMENTODESPESA", "VLDESPESA", "HISTORICODESPESA"]
st.markdown("### 🔺 Detalhamento da Despesa")
st.dataframe(df_filtered[columsView], use_container_width=True, hide_index=True,
             column_config={
                "NMUNIDADEORCAMENTARIA": "Unidade",
                "VLDESPESA": st.column_config.NumberColumn("Despesa", format="%.2f 🔻"),
                'NMCREDOR': "Credor",
                "NMELEMENTODESPESA": "Elemento"
             })

