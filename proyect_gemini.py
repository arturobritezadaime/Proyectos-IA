import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la API Key de las variables de entorno
api_key = os.getenv("API_KEY")

# Asegúrate de que la API Key se ha cargado correctamente
if not api_key or not api_key.strip():
    raise ValueError("API_KEY no encontrada o vacía en las variables de entorno.")

genai.configure(api_key=api_key)

# Modelos gratuitos disponibles y sus características
MODELOS = {
    1: {
        "id": "models/gemini-1.5-flash",
        "uso": "Consultas rápidas y tareas interactivas",
        "calidad": "Alta velocidad, buena para respuestas breves",
        "característica": "Modelo rápido y eficiente"
    },
    2: {
        "id": "models/gemini-1.0-pro",
        "uso": "Generación de contenido más largo y complejo",
        "calidad": "Alta calidad, más preciso que flash",
        "característica": "Ideal para razonamiento, escritura y análisis"
    }
}

# Mostrar menú
print("Modelos gratuitos disponibles:")
for k, v in MODELOS.items():
    print(f"{k}. {v['id']} → Uso: {v['uso']} | Calidad: {v['calidad']} | Destacado: {v['característica']}")

# Elegir modelo
try:
    modelo_elegido = int(input("Elegí un número de modelo: ").strip())
    modelo_info = MODELOS.get(modelo_elegido)

    if not modelo_info:
        raise ValueError("Número de modelo no válido.")

    model = genai.GenerativeModel(modelo_info["id"])

    prompt = input("Escribí el contenido que querés generar: ")
    response = model.generate_content(prompt)

    print("\n📄 Respuesta del modelo:")
    print(response.text)

except Exception as e:
    print(f"⚠️ Error: {e}")
