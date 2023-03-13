import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image
import plotly.express as px
import plotly.graph_objs as go

def config_page():
    st.set_page_config(page_title = "EDA ALVARO JAEN", page_icon=":shark:", layout="wide")


def home():
    st.title(":video_game:_:blue[VISUALIZACIONES DE LOS CANALES DE VIDEOJUEGOS EN LA PLATAFORMA TWITCH]_:video_game:")
    
    img =Image.open("EDA/imagen/introduccion.jpeg")
    st.image(img,use_column_width="always")
    
    st.subheader(':red[Introducción]')
    st.markdown('''
    Este EDA comienzacon la recopilacion de datos de las visualizaciones desde 2016 hasta principio de 2023 de los principales canales
    de de videojuegos que hay en la plataforma Twitch para poder recopilar informacion y elaborar nuestras preguntas.
    ''')
    
    st.subheader(':green[¿QUÉ ES TWITCH?]')
    st.markdown('''
    Twitch es una plataforma estadounidense perteneciente a la empresa Amazon, Inc., que permite realizar transmisiones en vivo
    ''')
    with st.expander("CUESTION PRINCIPAL:sparkles:"):
        st.write('''
    ¿Será comparable la final de un E-Sport a un evento deportivo como la final del mundial?
    ''')
    with st.expander("CUESTIONES SECUNDARIAS:question:"):
        st.markdown("""
                * ¿Cuáles son los juegos mas visualizados cada año?¿Y en estos 7 años? \n
                * La tendencia de visualizaciones, ¿Aumenta o disminuye con los años?¿Ha afectado el covid a la visualizaciones en Twitch?\n
                
                Cuestiones interesantes surgidas tras la obtención de los datos:
                * ¿Cual es la variedad de juego más visualizado cada año?¿y en estos 7 años? \n
                * ¿Oscilan las visualizaciones según el mes del año?\n
                """)
def juegos_vistos_2016(): 
    df_juegos_2016 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2016.csv')
    pie1 = df_juegos_2016['Hours_watched']
    labels = df_juegos_2016["Game"]
         
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2016",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2016",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2017(): 
    df_juegos_2017 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2017.csv')
    pie1 = df_juegos_2017['Hours_watched']
    labels = df_juegos_2017["Game"]
        
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2017",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2017",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2018(): 
    df_juegos_2018 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2018.csv')
    pie1 = df_juegos_2018['Hours_watched']
    labels = df_juegos_2018["Game"]
         
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2018",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2018",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2019(): 
    df_juegos_2019 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2019.csv')
    pie1 = df_juegos_2019['Hours_watched']
    labels = df_juegos_2019["Game"]
         
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2019",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2019",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2020(): 
    df_juegos_2020 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2020.csv')
    pie1 = df_juegos_2020['Hours_watched']
    labels = df_juegos_2020["Game"]
         
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2020",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2020",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2021(): 
    df_juegos_2021 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2021.csv')
    pie1 = df_juegos_2021['Hours_watched']
    labels = df_juegos_2021["Game"]
         
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2021",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2021",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_2022(): 
    df_juegos_2022 = pd.read_csv('EDA/CSV/juegos mas jugados al año/juegos2022.csv')
    pie1 = df_juegos_2022['Hours_watched']
    labels = df_juegos_2022["Game"]
        
    fig = {
        "data": [
            {
        "values": pie1,
        "labels": labels,
        "domain": {"x": [0, .5]},
        "name": "Juegos más vistos en 2022",
        "hoverinfo":"label+percent+name",
        "hole": .3,
        "type": "pie"
        },],
        "layout": {
            "title":"",
            "annotations": [
                { "font": { "size": 20},
                "showarrow": False,
                "text": "Juegos más vistos en 2022",
                "x": 0.7,
                "y": 1.2
                },
            ]
        }
    }
    return fig
def juegos_vistos_total():
    
    df_lol = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/League of legends.csv')
    df_cod = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Call of Duty Warzone.csv')
    df_counter = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Counter Strike Global Offensive.csv')
    df_dota2 = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Dota 2.csv')
    df_Fortnite = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Fortnite.csv')
    df_gta = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Grand Theft Auto V.csv')
    df_hearstone = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Hearstone.csv')
    df_minecraft = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Minecraft.csv')
    df_wow = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/World of Warcraft.csv')
    df_valorant = pd.read_csv('EDA/CSV/juegos mas jugados en 7 años/Valorant.csv')

    lol = go.Scatter(
                    x = df_lol["Year"],
                    y = df_lol['Hours_watched'],
                    name = 'League of Legends',
                    mode= 'lines',
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text = "League of Legends")

    counter = go.Scatter(
                    x = df_counter["Year"],
                    y = df_counter['Hours_watched'],
                    name = 'Counter Strike Global Offensive',
                    mode= 'lines',
                    marker = dict(color = 'red'),
                    text = ['Counter Strike Global Offensive'])
    cod = go.Scatter(
                    x = df_cod["Year"],
                    y = df_cod['Hours_watched'],
                    name = 'Call of Duty Warzone',
                    mode= 'lines',
                    marker = dict(color = 'rgba(55, 128, 255, 0.8)'),
                    text = ['Call of Duty Warzone'])
    dota2 = go.Scatter(
                    x = df_dota2["Year"],
                    y = df_dota2['Hours_watched'],
                    name = 'Dota 2',
                    mode= 'lines',
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text = ['Dota2'])
    Fortnite = go.Scatter(
                    x = df_Fortnite["Year"],
                    y = df_Fortnite['Hours_watched'],
                    name = 'Fortnite',
                    mode= 'lines',
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text = ['Fortnite'])
    gta = go.Scatter(
                    x = df_gta["Year"],
                    y = df_gta['Hours_watched'],
                    name = 'Grand Theft Auto V',
                    mode= 'lines',
                    marker = dict(color = 'pink'),
                    text = ['Grand Theft Auto V'])
    hearstone = go.Scatter(
                    x = df_hearstone["Year"],
                    y = df_hearstone['Hours_watched'],
                    name = 'Hearstone',
                    mode= 'lines',
                    marker = dict(color = 'rgba(255, 255, 128, 1.5)'),
                    text = ['Hearstone'])
    minecraft = go.Scatter(
                    x = df_minecraft["Year"],
                    y = df_minecraft['Hours_watched'],
                    name = 'Minecraft',
                    mode= 'lines',
                    marker = dict(color = 'rgba(171, 50, 96, 0.6)'),
                    text = ['Minecraft'])
    wow = go.Scatter(
                    x = df_wow["Year"],
                    y = df_wow['Hours_watched'],
                    name = 'World of Warcraft',
                    mode= 'lines',
                    marker = dict(color = 'brown'),
                    text = ['World of Warcraft'])
    valorant = go.Scatter(
                    x = df_valorant["Year"],
                    y = df_valorant['Hours_watched'],
                    name = 'Valorant',
                    mode= 'lines',
                    marker = dict(color = 'rgba(248, 248, 255)'),
                    text = ['Valorant'])
    
    data = [lol,counter,cod,dota2,Fortnite,hearstone,minecraft,wow,gta,valorant]

    layout = dict(title = 'JUEGOS MAS VISUALIZADOS EN 7 AÑOS (DATOS DE 2016-2022)',
             xaxis= dict(title= 'YEARS',ticklen=5, ticks="outside", tickson="boundaries",), 
             yaxis= dict(title= 'HORAS VISUALIZADAS',ticklen=5, ticks="outside", tickson="boundaries",)
           )
    fig = go.Figure(data = data, layout=layout)
    return fig

def tipo_juegos(): 
    
    df_tipo_juegos = pd.read_csv('EDA/CSV/tipo de juego en 7 años/tipo juegos en 7 años.csv')
    
    Data = go.Bar(x = df_tipo_juegos["Tipo de juego"],
                y = df_tipo_juegos['Recuento'],
                name = 'Tipos de juegos más populares en 7 años',
                marker = dict(color = 'Orange',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_tipo_juegos["Tipo de juego"])
    layout  = {
    'xaxis': {'title': 'TIPO DE JUEGO'},
    'yaxis': {'title': 'ACUMULADO EN 7 AÑOS'},
    'barmode': 'group',
    'title': 'TIPO DE JUEGOS MAS SEGUIDOS EN 7 AÑOS (DATOS DE 2016-2022)'
    }

    fig = go.Figure(data = Data, layout = layout)
    
    return fig

def viewers(): 
    df_viewer_total = pd.read_csv('EDA/CSV/total viewer 7 años/total viewers 7 años.csv')
    data = go.Scatter(
                    x = df_viewer_total["Year"],
                    y = df_viewer_total['Hours_watched'],
                    name = 'TOTAL HORAS VISUALIZADAS EN CANALES DE JUEGOS EN 7 AÑOS',
                    mode= 'lines+markers',
                    marker = dict(color = 'green'),
                    text = df_viewer_total["Year"])
    layout = dict(title = 'TOTAL HORAS VISUALIZADAS EN CANALES DE JUEGOS EN 7 AÑOS (DATOS DE 2016-2022)',
             xaxis= dict(title= 'YEAR',ticklen=5, ticks="outside", tickson="boundaries",), 
           )

    fig = go.Figure(data = data, layout=layout)
    
    return fig    
    
def viewer_mes(): 
    df_viewer_mes = pd.read_csv('EDA/CSV/viewer por mes/visualizaciones por mes.csv')
    
    Data = go.Bar(x = df_viewer_mes["Month"],
                y = df_viewer_mes['Hours_watched'],
                name = 'Diferenciacion de visualizaciones por cada mes',
                marker = dict(color = 'blue',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = ["Enero","Febrero","MArzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
    layout  = {
    'xaxis': {'title': 'MES'},
    'yaxis': {'title': 'HORAS/VISUALIZADAS'},
    'barmode': 'group',
    'title': 'HORAS VISUALIZADA DIFERENCIADAS POR MES (DATOS DE 2016-2022)'
    }

    fig = go.Figure(data = Data, layout = layout)

    return fig

def pico_viewer(): 
    
    df_pico_viewer = pd.read_csv('EDA/CSV/pico viewer en 7 años/pico visualizaciones en 7 años.csv')
    
    Data = go.Bar(x = df_pico_viewer["Year"],
                y = df_pico_viewer['Peak_viewers'],
                name = 'Diferenciacion de visualizaciones por cada mes',
                marker = dict(color = 'red',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_pico_viewer["Game"])
    layout  = {
    'xaxis': {'title': 'AÑO'},
    'yaxis': {'title': 'MAXIMO HORAS/VISUALIZADAS'},
    'barmode': 'group',
    'title': 'MAXIMA AUDIENCIA POR AÑO (DATOS DE 2016-2022)'
    }

    fig = go.Figure(data = Data, layout = layout)
    
    return fig
def comparativa(): 
    df_twitch = pd.read_csv('EDA/CSV/pico viewer en 7 años/twitch.csv')
    df_2022_españa = pd.read_csv('EDA/CSV/pico viewer en 7 años/mundial 2022 españa.csv')
    df_2022_francia= pd.read_csv('EDA/CSV/pico viewer en 7 años/mundial 2022 francia.csv')
    df_2010 = pd.read_csv('EDA/CSV/pico viewer en 7 años/mundial 2010.csv')
    
    españa_2022 = go.Bar(x = df_2022_españa["Game"],
                y = df_2022_españa['Peak_viewers'],
                name = 'Final mundial 2022 España',
                marker = dict(color = 'yellow',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_2022_españa["Game"])
    twitch = go.Bar(x = df_twitch["Game"],
                y = df_twitch['Peak_viewers'],
                name = 'Final mundial Lol 2021',
                marker = dict(color = 'green',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_twitch["Game"])
    españa_2010 = go.Bar(x = df_2010["Game"],
                y = df_2010['Peak_viewers'],
                name = 'Final mundial 2010',
                marker = dict(color = 'red',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_2010["Game"])
    francia_2022 = go.Bar(x = df_2022_francia["Game"],
                y = df_2022_francia['Peak_viewers'],
                name = 'Final mundial 2022 Francia',
                marker = dict(color = 'blue',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
                text = df_2022_francia["Game"])
    layout  = {
    'xaxis': {'title': 'EVENTO'},
    'yaxis': {'title': 'MAXIMa AUDIENCIA HORAS/VISUALIZADAS'},
    'barmode': 'group',
    'title': 'MAXIMA AUDIENCIA TWITCH VS EVENTOS FUTBOLISTICOS'
    }
    data=[españa_2022,twitch,españa_2010,francia_2022]
    fig = go.Figure(data = data, layout = layout)
    
    return fig

def conclusiones(): 
    with st.expander("JUEGOS MÁS VISUALIZADOS"):
        st.markdown("Hay un claro patron de repetición de forma general de los juegos en el top10")
    with st.expander("TIPO DE JUEGOS MÁS VISUALIZADOS"):
        st.markdown("El tipo 'Shooter' es el favorito con clara ventaja")
    with st.expander("LA TENDENCIA DE VISUALIZACIONES,¿AUMENTA O DISMINUYE CON LOS AÑOS?¿HA AFECTADO EL COVID A LAS VISUALIZACIONES DE TWITCH?"):
        st.markdown("Vemos que hay una tendencia de crecimiento cada año, la cual fue mucho más acentuada durante la pandemia por Covid")
    with st.expander("¿OSCILAN LAS VISUALIZACIONES SEGÚN EL MES DEL AÑO?"):
        st.markdown("Las visualizaciones se mantienen lineales durante el año exceptuando en el mes de enero que son ligeramente superiores.")
    with st.expander("¿SERÁ COMPARABLE LA FINAL DE UN E-SPORT CON UN EVENTO DEPORTIVO COMO LA FINAL DEL MUNDIAL DE FUTBOL?"):
        st.markdown("""Tras realizar este EDA, llego a la conclusión que aunque los picos de audencia solo son medibles por canales de television y no a nivel mundial
                    (Twitch es también un canal como una televisión),solamente con coger un canal nacional podemos ver que no son comparables AÚN:exclamation: (Hay que verlo dentro de 10 años)""")
