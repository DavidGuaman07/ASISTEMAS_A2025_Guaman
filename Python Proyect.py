#Python Proyect

import streamlit as st
import pandas as pd
import datetime
import io

# --- DATOS DEL CUESTIONARIO (puedes importar desde Excel o pegar manualmente) ---
cuestionario_data = [
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

# --- ENCABEZADO ---
st.title("🛡️ Cuestionario NIST - Escala Likert")
st.markdown("Responda cada pregunta del siguiente cuestionario en una escala del 1 al 5:")
st.markdown("""
**Escala:**
- 1: No cumple  
- 2: Cumple parcialmente  
- 3: Cumple en gran medida  
- 4: Cumple totalmente  
- 5: Cumple y supera expectativas
""")

# --- FORMULARIO DE RESPUESTAS ---
respuestas = []
for dominio in sorted(set(item["Dominio"] for item in cuestionario_data)):
    st.subheader(f"🔹 {dominio}")
    for item in filter(lambda x: x["Dominio"] == dominio, cuestionario_data):
        key = f"{dominio}-{item['Pregunta']}"
        respuesta = st.radio(
            label=item["Pregunta"],
            options=[1, 2, 3, 4, 5],
            key=key,
            horizontal=True
        )
        respuestas.append({
            "Dominio": dominio,
            "Pregunta": item["Pregunta"],
            "Respuesta": respuesta
        })

# --- MOSTRAR RESULTADO ---
if st.button("📊 Ver resultados"):
    df_resultado = pd.DataFrame(respuestas)
    st.success("Respuestas recopiladas correctamente.")
    st.dataframe(df_resultado)

    promedio_dominio = df_resultado.groupby("Dominio")["Respuesta"].mean().reset_index()
    st.subheader("📈 Promedio por Dominio")
    st.table(promedio_dominio)

    # --- Descarga de CSV ---
    st.subheader("⬇️ Descargar respuestas en CSV")
    csv_buffer = io.StringIO()
    df_resultado.to_csv(csv_buffer, index=False)
    st.download_button(
        label="Descargar archivo CSV",
        data=csv_buffer.getvalue(),
        file_name=f"respuestas_nist_{datetime.date.today()}.csv",
        mime="text/csv"
    )