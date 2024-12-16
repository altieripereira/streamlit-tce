import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("https://consultas.transparencia.mt.gov.br/dados_abertos/despesa/Despesa_2024.csv", encoding="cp1252", sep=';', nrows=3000)
    # df_data = pd.read_csv("datasets/despesa_2024.csv", encoding="cp1252", encoding_errors='ignore', sep=';')
    columns = ['NUANO', 'NMMES', 'NUBIMESTRE', 'DTEMISSAODESPESA', 'TPDESPESA', 'NMUNIDADEORCAMENTARIA', 
               'NMUNIDADEGESTORA', 'NMCREDOR', 'CPF_CNPJ', 'NMTIPOCREDOR', 'NMFUNCAO', 'NMSUBFUNCAO', 'NMPROGRAMA',
               'NMACAO', 'NMFONTERECURSO', 'NMCATEGORIA', 'NMGRUPONATUREZADESPESA', 'NMMODALIDADEAPLICACAO',
               'NMELEMENTODESPESA', 'VLDESPESA', 'HISTORICODESPESA']
    df = df_data[columns]
    st.session_state["data"] = df

st.markdown("# 🏠 OBSERVATÓRIO TCE - DESPESAS 2024")

st.markdown('''
### Introdução

O **Observatório de Despesas Públicas** é uma ferramenta inovadora desenvolvida pelo **Tribunal de Contas do Estado de Mato Grosso (TCE-MT)** para promover a transparência e o controle social sobre os gastos públicos no estado. Com foco em facilitar o acesso aos dados de despesas estaduais, a plataforma empodera o cidadão ao oferecer uma visão clara e detalhada sobre como os recursos públicos estão sendo utilizados.
### Objetivos
- **Promover a Transparência:** Disponibilizar dados de despesas públicas de forma acessível e compreensível para todos os cidadãos.
- **Fomentar o Controle Social:** Permitir que qualquer pessoa possa acompanhar e fiscalizar os gastos do estado de Mato Grosso.
- **Apoiar a Gestão Pública:** Oferecer insights e informações que auxiliem na melhoria da eficiência do uso dos recursos públicos.
''')

st.link_button("Acesse os Dados Abertos", "https://www.transparencia.mt.gov.br/despesas1")

st.sidebar.video("assets/tce.mp4", format="video/mp4", start_time=0,)



