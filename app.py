
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import datetime

# Configuración inicial
st.set_page_config(page_title="Cuestionario NIST", layout="wide")
st.title("🛡️ Cuestionario de Seguridad - NIST")
st.markdown("Responda cada pregunta usando la **escala Likert (1 a 5)**:")
st.info("""
**Escala Likert:**
- 1️⃣ No cumple  
- 2️⃣ Cumple parcialmente  
- 3️⃣ Cumple en gran medida  
- 4️⃣ Cumple totalmente  
- 5️⃣ Cumple y supera expectativas
""")

# Base de datos
cuestionario = [
    {"Dominio": "Seguridad Física", "Pregunta": "¿Existen controles de acceso físico a las áreas sensibles de la organización (ej., servidores, centros de datos)?"},
    {"Dominio": "Seguridad Física", "Pregunta": "¿Se registran y supervisan adecuadamente las visitas a las instalaciones críticas de la organización?"},
    {"Dominio": "Seguridad Física", "Pregunta": "¿Se realizan auditorías periódicas a los sistemas de seguridad física (cámaras, alarmas, barreras, etc.) para asegurar su efectividad?"},
    {"Dominio": "Gestión de Riesgos", "Pregunta": "¿Se realizan evaluaciones de riesgos de seguridad de la información de forma regular y sistemática en la organización?"},
    {"Dominio": "Gestión de Riesgos", "Pregunta": "¿Se identifican y priorizan adecuadamente los activos de información críticos (ej., datos sensibles, sistemas esenciales) de la organización?"},
    {"Dominio": "Gestión de Riesgos", "Pregunta": "¿Se cuenta con planes de tratamiento y mitigación definidos y en ejecución para los riesgos de seguridad identificados?"},
    {"Dominio": "Seguridad en las Operaciones", "Pregunta": "¿Se monitorean y registran las actividades de los sistemas críticos para detectar eventos sospechosos?"},
    {"Dominio": "Seguridad en las Operaciones", "Pregunta": "¿Se realizan copias de seguridad de la información crítica con una frecuencia adecuada y se almacenan en ubicaciones seguras?"},
    {"Dominio": "Seguridad en las Operaciones", "Pregunta": "¿Se gestionan adecuadamente los registros de auditoría y se protegen contra alteraciones no autorizadas?"}
]

# Formulario interactivo
respuestas = []
for dominio in sorted(set(q["Dominio"] for q in cuestionario)):
    st.subheader(f"🔹 {dominio}")
    for q in filter(lambda x: x["Dominio"] == dominio, cuestionario):
        key = f"{dominio}-{q['Pregunta']}"
        respuesta = st.radio(q["Pregunta"], [1, 2, 3, 4, 5], key=key, horizontal=True)
        respuestas.append({"Dominio": dominio, "Pregunta": q["Pregunta"], "Respuesta": respuesta})

# Botón de resultados
if st.button("📊 Ver resultados"):
    df = pd.DataFrame(respuestas)

    # Mostrar resumen en tabla
    st.success("✅ Respuestas recopiladas correctamente.")
    st.subheader("📋 Resumen de respuestas")
    st.dataframe(df, use_container_width=True)

    # Promedio por dominio
    promedio = df.groupby("Dominio")["Respuesta"].mean().reset_index()
    promedio.columns = ["Dominio", "Promedio"]

    # Mostrar tabla
    st.subheader("📈 Promedio por Dominio")
    st.table(promedio)

    # Gráfico de barras
    st.subheader("📊 Visualización Gráfica")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=promedio, x="Dominio", y="Promedio", palette="viridis", ax=ax)
    ax.set_ylim(1, 5)
    ax.set_ylabel("Promedio Likert")
    ax.set_title("Resultado por dominio (escala 1 a 5)")
    st.pyplot(fig)

    # Descargar CSV
    st.subheader("⬇️ Descargar respuestas")
    csv = df.to_csv(index=False)
    st.download_button("📥 Descargar CSV", csv, f"respuestas_nist_{datetime.date.today()}.csv", "text/csv")
