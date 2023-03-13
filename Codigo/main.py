import pandas as pd
import streamlit as st
from PIL import Image
import funciones as ft
import plotly.express as px
import plotly.graph_objs as go
from streamlit_lottie import st_lottie
import json

ft.config_page()

menu = st.sidebar.selectbox('Elige una sección:', ('Introducción', 'Juegos mas visualizados','Tipo de juego','Tendencia visualizaciones', 'Visualizaciones por mes', 'Comparativa','Conclusiones'))

if menu == 'Introducción':
    ft.home()

elif menu == 'Juegos mas visualizados':
    fig_vistos_2016 = ft.juegos_vistos_2016()
    fig_vistos_2017 = ft.juegos_vistos_2017()
    fig_vistos_2018 = ft.juegos_vistos_2018()
    fig_vistos_2019 = ft.juegos_vistos_2019()
    fig_vistos_2020 = ft.juegos_vistos_2020()
    fig_vistos_2021 = ft.juegos_vistos_2021()
    fig_vistos_2022 = ft.juegos_vistos_2022()
    fig_vistos_total = ft.juegos_vistos_total()
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2016 :bow_and_arrow:"): 
        st.plotly_chart(fig_vistos_2016, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2017 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2017, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2018 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2018, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2019 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2019, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2020 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2020, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2021 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2021, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS CADA AÑO:2022 :bow_and_arrow:"):
        st.plotly_chart(fig_vistos_2022, use_container_width=True)
    with st.expander("JUEGOS MAS VISUALIZADOS EN 7 AÑOS:trophy:"):
        st.plotly_chart(fig_vistos_total, use_container_width=True)
    img =Image.open("EDA/imagen/minecraft.jpg")
    st.image(img,use_column_width="always")
elif menu == 'Tipo de juego':
    fig_tipo_juegos = ft.tipo_juegos()
    with st.expander("TIPO DE JUEGOS MAS VISUALIZADOS EN 7 AÑOS:european_castle:"):
        st.plotly_chart(fig_tipo_juegos, use_container_width=True)
    img =Image.open("EDA/imagen/apex.png")
    st.image(img,use_column_width="always")
elif menu == 'Tendencia visualizaciones':
    fig_viewers = ft.viewers()
    with st.expander("HISTORIAL TOTAL VISUALIZACIONES CADA AÑO EN 7 AÑOS:dragon:"):
        st.plotly_chart(fig_viewers, use_container_width=True)
        
    img =Image.open("EDA/imagen/amongus.jpg")
    st.image(img,use_column_width="always")
elif menu == 'Visualizaciones por mes':
    fig_viewers_mes = ft.viewer_mes()
    with st.expander("VISUALIZACIONES POR CADA MES:space_invader:"):
        st.plotly_chart(fig_viewers_mes, use_container_width=True) 
    img =Image.open("EDA/imagen/wow.jpg")
    st.image(img,use_column_width="always")  
 
elif menu == 'Comparativa' :
    fig_pico_año = ft.pico_viewer()
    fig_comparativa = ft.comparativa()
    with st.expander("PICOS DE MAXIMAS VISUALIZACIONES AL AÑO (2016-2022):dagger_knife:"):
        st.plotly_chart(fig_pico_año, use_container_width=True)
    with st.expander("COMPARATIVA CON ALGUNOS FINALES DE EVENTOS DE FUTBOL:dagger_knife:"):
        st.markdown("""
                Vamos a comprar con los siguientes 3 eventos futbolísticos:\n
                * Máxima audiencia en la Final del mundial 2010 Sudafrica (España Holanda) en ESPAÑA - (Telecinco + Canal+)\n
                * Máxima audiencia en la Final del mundial 2022 Catar (Argentina-Francia) en ESPAÑA - (TVE +  Gol Mundial)\n
                * Máxima audiencia en la Final del mundial 2022 Catar (Argentina-Francia) en FRANCIA - (TF1 -Television francesa) \n
                """)
        st.plotly_chart(fig_comparativa, use_container_width=True)  
    img =Image.open("EDA/imagen/lol.jpg")
    st.image(img,use_column_width="always")
else:
    st.header('Conclusiones')
    ft.conclusiones()
    with open("EDA/imagen/gift 2.json") as source:
        animation = json.load(source)
    st_lottie(animation, height=1000, width=1000)
