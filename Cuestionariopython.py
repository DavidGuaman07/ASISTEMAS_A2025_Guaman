
import streamlit as st
import pandas as pd

# Cargar archivo Excel
@st.cache_data
def cargar_datos():
    xls = pd.ExcelFile("Cuestionario_NIST_Likert.xlsx")
    df = xls.parse(xls.sheet_names[0], header=None)
    return df

# Procesar preguntas agrupadas por dominio
def obtener_cuestionario(df):
    preguntas = {}
    dominio_actual = None
    for i, row in df.iterrows():
        if pd.isna(row[0]):
            continue
        if isinstance(row[0], str) and not row[0].startswith('¿'):
            dominio_actual = row[0].strip()
            preguntas[dominio_actual] = []
        elif isinstance(row[0], str) and row[0].startswith('¿'):
            preguntas[dominio_actual].append(row[0].strip())
    return preguntas

# Main app
st.title("Cuestionario de Evaluación NIST - Escala Likert")
df = cargar_datos()
cuestionario = obtener_cuestionario(df)

respuestas = {}
st.write("Seleccione una opción del 1 al 5 para cada pregunta:")

for dominio, preguntas in cuestionario.items():
    st.subheader(dominio)
    for pregunta in preguntas:
        respuesta = st.radio(
            pregunta,
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "1 - No cumple",
                2: "2 - Cumple parcialmente",
                3: "3 - Cumple en gran medida",
                4: "4 - Cumple totalmente",
                5: "5 - Cumple y supera expectativas"
            }[x],
            key=pregunta
        )
        respuestas[pregunta] = respuesta

if st.button("Mostrar resumen"):
    resumen = {}
    for dominio, preguntas in cuestionario.items():
        valores = [respuestas[p] for p in preguntas]
        promedio = sum(valores) / len(valores)
        resumen[dominio] = round(promedio, 2)
    st.write("### Resultado Promedio por Dominio")
    st.dataframe(pd.DataFrame(resumen.items(), columns=["Dominio", "Promedio Likert"]))
