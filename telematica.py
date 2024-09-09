import streamlit as st
import pandas as pd
import ciso8601


header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()
with header:
    st.title('Departamento de Infraestructura')
    st.text('Estadísticas del correo institucional')

with dataset:
    st.header('Tabla de Registros')
    st.text('Registro de Lunes-Domingo con corte a las 11:59:00')
    df = pd.read_csv('data/registros.csv')
    fechas = list(df['Fecha'])
    print(fechas)
    df['Fecha'] = pd.to_datetime(fechas, format="mixed")
    df = df.sort_values('Fecha')
    st.write(df)
    st.header('Estadísticas por semana, quincena, mes:')
    rango = st.selectbox("Rango",['Por semana','Por quincena','Por mes'], index=None, placeholder="Elige una opción")
    bandera = 0
    if rango == 'Por semana':
        rangos = df.groupby(pd.Grouper(key="Fecha", axis=0, freq='W')).sum()
        bandera = 1
    if rango == 'Por mes':
        rangos = df.groupby(pd.Grouper(key="Fecha", axis=0, freq='MS')).sum()
        bandera = 1
    if rango == 'Por quincena':
        rangos = df.groupby(pd.Grouper(key="Fecha", axis=0, freq='SMS')).sum()
        bandera = 1

    if bandera == 1:
        st.write(rangos)
        st.header('Concentrado de Estadísticas')
        st.write(rangos.describe())

        with features:
            st.header('Gráficas')
            #st.scatter_chart(data=rangos)#, x='bill_length_mm', y='body_mass_g', color='species')
            st.area_chart(rangos)
