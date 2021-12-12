import plotly.express as px
import pandas as pd
import streamlit as st
from streamlit.proto.Markdown_pb2 import Markdown



df = pd.read_csv('./bd_final.csv', encoding='UTF-8')

header_principal = st.container()
col_1, col_2 = st.columns(2)

with col_1:
    st.title('PROYECTO EMPRESARIAL NODOS TIGO')
with col_2: st.image('./assets/imagen.png', width=200)

st.header('Equipo DATA INTELLIGENCE')

st.sidebar.header('Seleccione una opción')

opciones_presentacion = st.sidebar.selectbox('', ['Introduccion', 'Modelo', 'Gráficos de interés'])


if opciones_presentacion == 'Introduccion':
    intro = st.container()

    with intro:
        
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 20px;">Grupo número 3 del curso DATA SCIENCE intermedio - Sapiencia con iData y EAFIT</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.text('')
        st.header('INTEGRANTES')
        st.markdown('Nuestro equipo está conformado por: ')

        int_1, int_2, int_3, int_4 = st.columns(4)
        with int_1:
            st.image('./assets/Foto_JC.jpeg', width=150)
            st.markdown('**Juan Camilo Cárdenas**')
            st.markdown('Economista / Magíster Estadística')
        with int_2:
            st.image('./assets/DSOA.png', width=115)
            st.markdown('**David Santiago Osorio**')
            st.markdown('Administrador Financiero')
        with int_3:
            st.image('./assets/foto_camiloE.jpeg', width=115)
            st.markdown('**Camilo Ramirez**')
            st.markdown('Ingeniero Civil')
        with int_4:
            st.image('./assets/FOTO_william.jpg', width=140)
            st.markdown('**William Úsuga**') 
            st.markdown('Ingeniero Mecánico')
        
        
        st.header('El Reto:')
        st.write('En el marco del objetivo del ejercicio del reto empresarial asignado, en este caso para la empresa TIGO COLOMBIA, como equipo desarrollamos un modelo de clasificación para identificar las cabinas de red o nodos cuyas características permitieran una mayor eficacia en ventas, para lo cuál nos entregaron una base de datos con información de los nodos. ')

        st.header('La Data ')
        st.write('Datos entregados por tigo para el análisis de negocio. Una muestra de los datos recibidos:')
        st.write('')
        st.write(df.head(3))




elif opciones_presentacion == 'Modelo':
    
    
    model_training = st.container()
    

    with model_training:
        st.header('Modelo de clasificación')
        st.subheader('Escribe aquí los datos del nodo a analizar para obtener su clasificación')

        input_tasaocu = st.number_input('Escribe la Tasa de Ocupación', help='ejemplo: 40.25', min_value=0, max_value=111, value=36)
        input_instrgu = st.number_input('Escribe la Instalación RGU', help='ejemplo: 30', min_value=0, max_value=269, value=30)
        input_churn = st.number_input('Escribe el Churn RGU', help='ejemplo: -18', min_value=-103, max_value=30, value= -18)


        tasa_ocu_score = 0
        if input_tasaocu <= 37.93:
            st.write('Puntaje TASA DE OCUPACIÓN: 2')
            tasa_ocu_score = 2
        elif input_tasaocu > 37.93 and input_tasaocu <= 66.27:
            st.write('Puntaje TASA DE OCUPACIÓN: 1')
            tasa_ocu_score = 1
        elif input_tasaocu > 66.27 and input_tasaocu <= 110:
            st.write('Puntaje TASA DE OCUPACIÓN: 0')
            tasa_ocu_score = 0
        else:
            st.write('VALOR INGRESADO FUERA DE RANGOS NORMALES')

        
        inst_rgu_score = 0
        if input_instrgu <= 14:
            st.write('Puntaje INSTALACIÓN RGU: 0')
            inst_rgu_score = 2
        elif input_instrgu > 14 and input_instrgu <= 37:
            st.write('Puntaje INSTALACIÓN RGU: 1')
            inst_rgu_score = 1
        elif input_instrgu > 37 and input_instrgu <= 269:
            st.write('Puntaje INSTALACIÓN RGU: 0')
            inst_rgu_score = 0
        else:
            st.write('VALOR INGRESADO FUERA DE RANGOS NORMALES')
       

        churn_rgu_score = 0
        if input_churn >= -11:
            st.write('Puntaje CHURN RGU: 0')
            churn_rgu_score = 0
        elif input_churn < -12 and input_churn >= -30:
            st.write('Puntaje CHURN RGU: 1')
            churn_rgu_score = 1
        elif input_churn < -30 and input_churn >= -103:
            st.write('Puntaje CHURN RGU: 2')
            churn_rgu_score = 2
        else:
            st.write('VALOR INGRESADO FUERA DE RANGOS NORMALES')

        puntaje_total =  tasa_ocu_score + inst_rgu_score + churn_rgu_score
        st.subheader('Puntaje TOTAL del NODO:  ' + str(puntaje_total))


        if puntaje_total > 4:
            st.write('Según el modelo, el nodo cumple con las expectativas')
        else:
            st.write('El nodo no cumple con las expectativas, debe obtener un puntaje mayor a 4. Se recomienda revisar el nodo y sus características')
    

elif opciones_presentacion == 'Gráficos de interés':
    st.title('Algunos gráficos de linterés')
    st.header('')
    
    grafico1 = st.container()
    with grafico1:

        st.subheader('GRÁFICO 1: Facturación de los nodos dependiendo de su respectiva clasificación.')
        fig_variables = px.bar(df, y='FACTURACION', x='Score_segmentation')
        st.plotly_chart(fig_variables)
    
    grafico2 = st.container()
    with grafico2:
        st.header('GRÁFICO 2: Distribución de la puntuación en relación a la facturación y el número de instalaciones.')
        fig_scatter = px.scatter(df, y="FACTURACION",  x  = "INST RGU_x",  color="Score_segmentation")
        st.plotly_chart(fig_scatter)

    grafico3 = st.container()
    with grafico3:
        st.header('GRÁFICO 3: Nodos más rentables según departamento..')
        fig = px.histogram(df[df["Score_segmentation"] > 4], x="DEPARTAMENTO")
        st.plotly_chart(fig)








