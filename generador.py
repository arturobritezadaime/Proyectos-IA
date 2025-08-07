import google.generativeai as genai

# ================================
# 🔹 Generar contenido con modelo
# ================================

def generar_contenido(modelo_id, prompt):
    modelo = genai.GenerativeModel(modelo_id)
    respuesta = modelo.generate_content(prompt)
    return respuesta.text