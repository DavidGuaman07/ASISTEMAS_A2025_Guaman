cuestionario_nist = {
    "AC - Control de Acceso": [
        {
            "pregunta": "¿Se aplican controles de acceso basados en roles para todos los sistemas?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se revisan periódicamente los privilegios de acceso asignados a los usuarios?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se requiere autenticación multifactor para accesos críticos?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se eliminan las cuentas de usuarios inactivos o desvinculados oportunamente?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se registra y supervisa el acceso a información sensible?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        }
    ],
    "AU - Auditoría y Rendición de Cuentas": [
        {
            "pregunta": "¿Se registran todos los eventos relevantes de seguridad?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se revisan y analizan los registros de auditoría con regularidad?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se conserva evidencia de acceso y modificación a datos críticos?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se emplean herramientas automáticas para la supervisión de auditoría?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Los registros de auditoría son protegidos contra alteración no autorizada?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        }
    ],
    "CP - Planificación de Contingencia": [
        {
            "pregunta": "¿La organización cuenta con un plan formal de contingencia aprobado?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se realizan pruebas periódicas del plan de recuperación ante desastres?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se mantienen copias de seguridad de los datos esenciales?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Las copias de seguridad se almacenan en ubicaciones seguras y externas?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        },
        {
            "pregunta": "¿Se capacita al personal sobre los procedimientos de continuidad operativa?",
            "respuestas_posibles": [
                "No cumple",
                "Cumple parcialmente",
                "Cumple en gran medida",
                "Cumple totalmente",
                "Cumple y supera expectativas"
            ]
        }
    ]
}

# Ejemplo de cómo acceder a los datos:
# Imprimir todas las preguntas de "AC - Control de Acceso"
print("Preguntas de Control de Acceso:")
for pregunta in cuestionario_nist["AC - Control de Acceso"]:
    print(f"- {pregunta['pregunta']}")

# Imprimir las respuestas posibles para la primera pregunta de "AU - Auditoría y Rendición de Cuentas"
print("\nRespuestas posibles para la primera pregunta de Auditoría:")
print(cuestionario_nist["AU - Auditoría y Rendición de Cuentas"][0]["respuestas_posibles"])