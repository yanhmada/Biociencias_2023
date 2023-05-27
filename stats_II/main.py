import streamlit as st
import pandas as pd
import plotly.express as px

import plotly.io as pio
pio.renderers.default = "browser"
from scipy import stats
from scipy.stats.mstats import kruskal

header = st.container ()
dataset = st.container ()
features = st.container ()

with header:
    st.title( 'Biociencias 2023\n\n' 
             'Maestria en Ciencia de Datos. Universidad de Sonora')

st.header(':blue[Observar diferencias en colonización ] _micorrícica_ :blue[entre plantas] ')

text = ("Uno de los beneficios de la colonizacion micorrícica es el aumento de nutrientes, "
        "especialmente fósforo y nitrógeno. Se buscaría probar que los tratamientos con inóculo "
        "tienen mejor absorción de fósforo.\n\n"
        "* The Role of the Mycorrhizal Symbiosis in Nutrient Uptake of Plants and the Regulatory "
        "Mechanisms Underlying These Transport Processes")
st.write(text)


@st.cache

def get_data() -> pd.DataFrame:
        return pd.read_csv("./Base_datos_1.csv")

df_ = get_data()

"""
# Add common name
dict_common  = {'V. farnesiana':'Vinorama','R. communis':'Ricino'}

# agregar 'common_name' 
df_['common_name'] = df_['Especie'].replace(dict_common)

df_ = df_[(df_['Trat'] != 'J') & (df_['Trat'] != 'JI')] #remove Jal an

#list for selection
listd = ['P','As', 'Ca', 'Cu', 'Fe',
       'K', 'Mg', 'Mn', 'Pb', 'Zn', 'Biomasa']

# Allow the user to select columns
selected_columns = st.selectbox('Select Element to chart', options = listd, index = 0)

# Filter the DataFrame based on selected columns
filtered_df = df_[selected_columns]


# Crear la grafica de caja
fig = px.box(df_, x="common_name", y=selected_columns, color="common_name", points="all", facet_col="Trat")

# Mostrar grafica
st.write(fig)

# valores de 'Tratamiento' 
trat_values = ['C', 'CI', 'J', 'JI', 'SN']

# iniciar diccionario

dfs_vinorama = {}

# Crear dataframe Vinorama
for trat in trat_values:
    # Filter the dataframe and select only the 'P' column
    dfs_vinorama[trat] = df_[(df_['Trat'] == trat) & (df_['common_name'] == 'Vinorama')][[selected_columns]].copy()

st.markdown("### Levene Test result")
from scipy.stats import levene
#data = dfs_vinorama.values.ravel()
stat, p_value = levene(dfs_vinorama['C'][selected_columns], 
                 dfs_vinorama['CI'][selected_columns], 
                 dfs_vinorama['SN'][selected_columns])

st.write("Segun la prueba  Levene el p-valor es :", p_value)

st.markdown("###  Kruskal~ Wallis")
from scipy.stats import levene
#data = dfs_vinorama.values.ravel()
stat, p_value = levene(dfs_vinorama['C'][selected_columns], 
                 dfs_vinorama['CI'][selected_columns], 
                 dfs_vinorama['SN'][selected_columns])


#perform Kruskal-Wallis Test 
statistic, pi_value = stats.kruskal(dfs_vinorama['C'][selected_columns], 
                 dfs_vinorama['CI'][selected_columns], 
                 dfs_vinorama['SN'][selected_columns])

st.write('El p- valor para la prueba Kruskal - wallis es ', pi_value)
"""
