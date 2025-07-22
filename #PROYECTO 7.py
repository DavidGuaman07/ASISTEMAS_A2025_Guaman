#PROYECTO 7

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Cuestionario NIST 800-53",
    page_icon="🛡️",
    layout="wide"
)

# Título de la aplicación
st.title("📋 Cuestionario NIST 800-53 del Instituto Nacional de Estándares y Tecnología")

# Cargar datos del cuestionario
def load_questions():
    data = {
        "Categoría": [
            "Seguridad Física", "Seguridad Física", "Seguridad Física",
            "Gestión de Riesgos", "Gestión de Riesgos", "Gestión de Riesgos",
            "Seguridad en las Operaciones", "Seguridad en las Operaciones", "Seguridad en las Operaciones"
        ],
        "Pregunta": [
            "¿Existen controles de acceso físico a las áreas sensibles de la organización (ej., servidores, centros de datos)?",
            "¿Se registran y supervisan adecuadamente las visitas a las instalaciones críticas de la organización?",
            "¿Se realizan auditorías periódicas a los sistemas de seguridad física (cámaras, alarmas, barreras, etc.) para asegurar su efectividad?",
            "¿Se realizan evaluaciones de riesgos de seguridad de la información de forma regular y sistemática en la organización?",
            "¿Se identifican y priorizan adecuadamente los activos de información críticos (ej., datos sensibles, sistemas esenciales) de la organización?",
            "¿Se cuenta con planes de tratamiento y mitigación definidos y en ejecución para los riesgos de seguridad identificados?",
            "¿Se monitorean y registran las actividades de los sistemas de información para detectar posibles anomalías, accesos no autorizados o incidentes de seguridad?",
            "¿Se realizan copias de seguridad de la información crítica de forma regular, y se verifica su integridad y capacidad de restauración?",
            "¿Se gestionan adecuadamente los registros de auditoría (logs) para fines de investigación forense, cumplimiento y análisis de seguridad?"
        ]
    }
    return pd.DataFrame(data)

df_preguntas = load_questions()

# Diccionario de niveles de cumplimiento
niveles = {
    1: "1: No cumple",
    2: "2: Cumple parcialmente",
    3: "3: Cumple en gran medida",
    4: "4: Cumple totalmente",
    5: "5: Cumple y supera expectativas"
}

# Diccionario de recomendaciones
recomendaciones = {
    1: "🔴 Implementar controles urgentes y desarrollar políticas de seguridad específicas.",
    2: "🟠 Fortalecer controles existentes y capacitar al personal sobre buenas prácticas.",
    3: "🟡 Optimizar procesos actuales e incorporar auditorías regulares para mejora continua.",
    4: "🟢 Mantener controles, realizar auditorías frecuentes y promover la cultura de seguridad.",
    5: "🔵 Documentar y compartir las buenas prácticas como modelo a seguir dentro de la organización."
}

# Sidebar
with st.sidebar:
    st.header("ℹ️ Acerca de")
    st.markdown("""
    Esta aplicación evalúa el cumplimiento de los controles de seguridad basados en el marco **NIST SP 800-53**.
    
    **NIST SP 800-53** es un estándar de seguridad de la información desarrollado por el:
    - Instituto Nacional de Estándares y Tecnología (NIST) de EE.UU.
    - Proporciona un catálogo de controles de seguridad para sistemas de información federales
    """)
    st.divider()
    st.markdown("Desarrollado por [Tu Nombre]")

# Inicializar respuestas en session_state
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}

# Formulario principal
with st.form("cuestionario_nist"):
    st.header("📝 Evaluación de Controles de Seguridad")
    
    for idx, row in df_preguntas.iterrows():
        st.subheader(f"{row['Categoría']}")
        st.markdown(f"**{row['Pregunta']}**")
        
        # Usar columnas para mejor disposición
        col1, col2 = st.columns([3, 1])
        with col1:
            respuesta = st.radio(
                "Seleccione el nivel de cumplimiento:",
                options=list(niveles.keys()),
                format_func=lambda x: niveles[x],
                key=f"pregunta_{idx}",
                horizontal=True
            )
        with col2:
            st.markdown("""
            <style>
            .stRadio [role=radiogroup]{
                align-items: center;
                gap: 5px;
            }
            </style>
            """, unsafe_allow_html=True)
        
        st.session_state.respuestas[idx] = {
            'Categoría': row['Categoría'],
            'Pregunta': row['Pregunta'],
            'Respuesta': respuesta
        }
        st.divider()
    
    submitted = st.form_submit_button("📊 Calcular Resultados")

# Mostrar resultados
if submitted:
    st.header("📈 Resultados de la Evaluación")
    
    # Convertir respuestas a DataFrame
    respuestas_df = pd.DataFrame.from_dict(st.session_state.respuestas, orient='index')
    
    # Calcular promedios por categoría
    resultados_categoria = respuestas_df.groupby('Categoría')['Respuesta'].mean().reset_index()
    resultados_categoria.columns = ['Categoría', 'Puntuación Promedio']
    
    # Gráfico de radar
    st.subheader("📊 Gráfico de Radar por Categorías")
    
    # Cerrar el círculo para el radar
    categorias = resultados_categoria['Categoría'].tolist() + [resultados_categoria['Categoría'].iloc[0]]
    valores = resultados_categoria['Puntuación Promedio'].tolist() + [resultados_categoria['Puntuación Promedio'].iloc[0]]
    
    fig = px.line_polar(
        r=valores,
        theta=categorias,
        line_close=True,
        range_r=[0, 5],
        template="plotly_white",
        title="Puntuación Promedio por Categoría",
        color_discrete_sequence=['#1f77b4']
    )
    
    fig.update_traces(fill='toself', line=dict(color='#1f77b4'))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickvals=[0, 1, 2, 3, 4, 5],
                ticktext=["0", "1", "2", "3", "4", "5"]
            )
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar recomendaciones
    st.subheader("📌 Recomendaciones por Pregunta")
    
    for idx, row in respuestas_df.iterrows():
        with st.expander(f"{row['Categoría']}: {row['Pregunta']} - Puntuación: {row['Respuesta']}"):
            st.markdown(f"**Nivel de cumplimiento:** {niveles[row['Respuesta']]}")
            st.markdown(f"**Recomendación:** {recomendaciones[row['Respuesta']]}")
    
    # Opción para descargar resultados
    st.download_button(
        label="⬇️ Descargar Resultados (CSV)",
        data=respuestas_df.to_csv(index=False, encoding='utf-8-sig'),
        file_name='resultados_nist_800_53.csv',
        mime='text/csv'
    )