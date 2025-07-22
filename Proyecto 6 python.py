#Cuestionario NIST 800-53 del Instituto Nacional de Estándares y Tecnología

import streamlit as st
import pandas as pd
import datetime
import io

# --- Cargar archivo Excel ---
@st.cache_data
def cargar_cuestionario():
    xls = pd.ExcelFile("Cuestionario_NIST_Likert.xlsx")
    df = xls.parse("Sheet1")
    df = df.iloc[3:].reset_index(drop=True)
    df.columns = ['Pregunta', '1', '2', '3', '4', '5']
    df = df[['Pregunta']].dropna().reset_index(drop=True)
    return df

df_preguntas = cargar_cuestionario()

# --- Recomendaciones por nivel ---
recomendaciones = {
    "1": "Implementar controles urgentes y desarrollar políticas de seguridad específicas.",
    "2": "Fortalecer controles existentes y capacitar al personal sobre buenas prácticas.",
    "3": "Optimizar procesos actuales e incorporar auditorías regulares para mejora continua.",
    "4": "Mantener controles, realizar auditorías frecuentes y promover la cultura de seguridad.",
    "5": "Documentar y compartir las buenas prácticas como modelo a seguir dentro de la organización."
}

# --- Título ---
st.title("🛡️ Cuestionario NIST 800-53 del Instituto Nacional de Estándares y Tecnología")
st.markdown("Responda cada pregunta en una escala del 1 al 5:")

st.markdown("""
**Escala:**
- 1: No cumple  
- 2: Cumple parcialmente  
- 3: Cumple en gran medida  
- 4: Cumple totalmente  
- 5: Cumple y supera expectativas
""")

# --- Formulario de respuestas ---
respuestas = []
for idx, fila in df_preguntas.iterrows():
    pregunta = fila["Pregunta"]
    respuesta = st.radio(
        label=f"**{pregunta}**",
        options=[1, 2, 3, 4, 5],
        key=f"pregunta_{idx}",
        horizontal=True
    )
    respuestas.append({
        "Pregunta": pregunta,
        "Respuesta": respuesta,
        "Recomendación": recomendaciones[str(respuesta)]
    })

# --- Mostrar resultados ---
if st.button("📊 Ver resultados"):
    df_resultado = pd.DataFrame(respuestas)
    st.success("Respuestas recopiladas correctamente.")
    st.dataframe(df_resultado)

    # --- Promedios por dominio (si existiera columna Dominio) ---
    # Aquí solo tenemos preguntas, pero podrías agrupar por categorías si las añades

    st.subheader("📈 Gráfico de cumplimiento")
    promedio = df_resultado['Respuesta'].mean()
    st.metric(label="Promedio General", value=f"{promedio:.2f} / 5")

    # --- Recomendaciones descargables ---
    csv_buffer = io.StringIO()
    df_resultado.to_csv(csv_buffer, index=False)

    st.download_button(
        label="⬇️ Descargar resultados en CSV",
        data=csv_buffer.getvalue(),
        file_name=f"respuestas_nist_{datetime.date.today()}.csv",
        mime="text/csv"
    )

    # Excel de resultados
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df_resultado.to_excel(writer, index=False, sheet_name="Resultados")
    st.download_button(
        label="⬇️ Descargar resultados en Excel",
        data=excel_buffer.getvalue(),
        file_name=f"recomendaciones_nist_{datetime.date.today()}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )