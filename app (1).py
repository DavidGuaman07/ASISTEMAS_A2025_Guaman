import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Auditoría ISO 27001", layout="wide")
st.title("🛡️ Cuestionario NIST 800-53 del Instituto Nacional de Estándares y Tecnología")

# Diccionario de preguntas por dominio
cuestionario = {
    "Seguridad Física": [
        "¿Existen controles de acceso físico a las áreas sensibles de la organización (ej., servidores, centros de datos)?",
        "¿Se registran y supervisan adecuadamente las visitas a las instalaciones críticas de la organización?",
        "¿Se realizan auditorías periódicas a los sistemas de seguridad física (cámaras, alarmas, barreras, etc.) para asegurar su efectividad?"
    ],
    "Gestión Riesgo": [
        "¿Se realizan evaluaciones de riesgos de seguridad de la información de forma regular y sistemática en la organización?",
        "¿Se identifican y priorizan adecuadamente los activos de información críticos (ej., datos sensibles, sistemas esenciales) de la organización?",
        "¿Se cuenta con planes de tratamiento y mitigación definidos y en ejecución para los riesgos de seguridad identificados?"
    ],
    "Seguridad en las Operaciones": [
        "¿Se monitorean y registran las actividades de los sistemas de información para detectar posibles anomalías, accesos no autorizados o incidentes de seguridad?",
        "¿Se realizan copias de seguridad de la información crítica de forma regular, y se verifica su integridad y capacidad de restauración?",
        "¿Se gestionan adecuadamente los registros de auditoría (logs) para fines de investigación forense, cumplimiento y análisis de seguridad?"
    ],
}

respuestas = []
st.subheader("📝 Cuestionario NIST 800-53 del Instituto Nacional de Estándares y Tecnología")

# Mostrar preguntas con subtítulos por dominio
for dominio, preguntas in cuestionario.items():
    st.markdown(f"### 🔹 {dominio}")  # Subtema como título
    for pregunta in preguntas:
        valor = st.slider(pregunta, 1, 5, 3)
        respuestas.append({"Dominio": dominio, "Pregunta": pregunta, "Respuesta": valor})

# Botón para generar informe
if st.button("✅ Generar Informe"):
    df = pd.DataFrame(respuestas)
    resumen = df.groupby("Dominio")["Respuesta"].mean().reset_index()

    st.subheader("📊 Promedios por Dominio")
    st.dataframe(resumen)

    fig = px.bar(resumen, x="Dominio", y="Respuesta", color="Dominio", range_y=[0, 5])
    st.plotly_chart(fig)

    st.subheader("🚦 Semáforo de Evaluación")
    for _, row in resumen.iterrows():
        dominio = row["Dominio"]
        promedio = row["Respuesta"]

        if promedio < 2.1:
            st.error(f"🔴 {dominio}: Riesgo Alto ({promedio:.2f}) – Se requiere intervención inmediata.")
        elif promedio < 3.6:
            st.warning(f"🟡 {dominio}: Riesgo Medio ({promedio:.2f}) – Oportunidad de mejora.")
        else:
            st.success(f"🟢 {dominio}: Cumplimiento Bueno ({promedio:.2f}) – Controles adecuados.")

        # Recomendaciones por dominio
        if dominio == "Seguridad Física":
            st.info("🔧 Recomendación: Aplica mínimo privilegio, revisiones periódicas y autenticación multifactor.")
        elif dominio == "Gestión de Riesgo":
            st.info("🔧 Recomendación: Formaliza los procedimientos de respuesta, registra y analiza los incidentes.")
        elif dominio == "Seguridad en las Operaciones":
            st.info("🔧 Recomendación: Controla accesos físicos, aplica vigilancia y registra accesos a zonas críticas.")