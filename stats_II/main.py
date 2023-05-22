import streamlit as st
import pandas as pd
import plotly.express as px
#interactive = st.beta.container()

import plotly.io as pio
pio.renderers.default='notebook'



header = st.container ()
dataset = st.container ()
features = st.container ()

with header:
    st.title( 'Welcome to Biociencias 2023\n\n' 
             'Maestria en Ciencia de Datos. Universidad de Sonora')

st.header('Biociencias 2023')
st.header(':blue[Observar diferencias en colonización ] _micorrícica_ :blue[entre plantas] ')

text = ("Uno de los beneficios de la colonizacion micorrícica es el aumento de nutrientes, "
        "especialmente fósforo y nitrógeno. Se buscaría probar que los tratamientos con inóculo "
        "tienen mejor absorción de fósforo.\n\n"
        "* The Role of the Mycorrhizal Symbiosis in Nutrient Uptake of Plants and the Regulatory "
        "Mechanisms Underlying These Transport Processes")

streamlined_text = text.replace("\n", " ").strip()

print(streamlined_text)



df_  = pd.read_csv(("Base_datos_1.csv"))

#dict to update  species to common name 
dict_common  = {'V. farnesiana':'Vinorama','R. communis':'Ricino'}

#update each
for key, value in dict_common.items():
    df_['Especie'] = df_['Especie'].replace(key, value)


#list for selection
listd = ['P','As', 'Ca', 'Cu', 'Fe',
       'K', 'Mg', 'Mn', 'Pb', 'Zn', 'Biomasa']

# Allow the user to select columns
selected_columns = st.selectbox('Select Element to chart', options = listd, index = 0)

# Filter the DataFrame based on selected columns
filtered_df = df_[selected_columns]


# Crear la grafica de violin
fig = px.violin(df_, x="Tejido", y="P", color="Especie", box=True, points="all", facet_col="Trat")

# Agregar el tratamiento 
fig = fig.update_layout(violingap=0, violingroupgap=0, violinmode="overlay")

# Mostrar grafica
st.write(fig)


# Crear la gráfica de histograma
fig2 = px.histogram(df_, x=selected_columns, y="Especie", color="Tejido", facet_row="Trat")

fig2.update_layout(
    barmode="overlay",  # Para superponer los histogramas
    bargap=0.1,  # Espacio entre las barras
    bargroupgap=0.05,  
)

fig2.update_traces(opacity=0.55)
# Mostrar la gráfica
st.write(fig2)