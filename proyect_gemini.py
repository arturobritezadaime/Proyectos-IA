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
# Solo se incluyen modelos vigentes que soportan generate_content (salida de texto)

MODELOS = {
    1: {
        "id": "models/gemini-2.5-pro",
        "uso": "Generación de contenido más largo y complejo",
        "calidad": "Alta calidad, más preciso que Flash",
        "característica": "Ideal para razonamiento, escritura y análisis"
    },
    2: {
        "id": "models/gemini-2.5-flash",
        "uso": "Respuestas rápidas y eficientes con menor costo",
        "calidad": "Buen rendimiento y eficiencia de costos",
        "característica": "Pensamiento adaptativo, ideal para tareas frecuentes"
    },
    3: {
        "id": "models/gemini-2.5-flash-lite",
        "uso": "Procesamiento de alto volumen con bajo costo",
        "calidad": "Velocidad alta, menor carga de recursos",
        "característica": "Modelo más rentable con buena capacidad"
    },
    4: {
        "id": "models/gemini-2.0-flash",
        "uso": "Respuestas veloces con capacidades modernas",
        "calidad": "Muy buena velocidad, soporte para streaming",
        "característica": "Modelo de nueva generación, optimizado para rendimiento"
    },
    5: {
        "id": "models/gemini-2.0-flash-lite",
        "uso": "Tareas de texto simples y económicas",
        "calidad": "Rendimiento aceptable con bajos recursos",
        "característica": "Modelo económico y de baja latencia"
    }
}


# Mostrar menú
print("\n📌 Modelos gratuitos disponibles:\n")
for k, v in MODELOS.items():
    print(f"{k}. {v['id']}")
    print(f"   → Uso: {v['uso']}")
    print(f"   → Calidad: {v['calidad']}")
    print(f"   → Destacado: {v['característica']}\n")

# Elegir modelo
try:
    modelo_elegido = int(input("🔢 Elegí el número del modelo: ").strip())
    modelo_info = MODELOS.get(modelo_elegido)

    if not modelo_info:
        raise ValueError("❌ Número de modelo no válido.")

    model = genai.GenerativeModel(modelo_info["id"])

    prompt = input("\n📝 Escribí el contenido que querés generar: ").strip()

    if not prompt:
        raise ValueError("❌ El contenido no puede estar vacío.")

    response = model.generate_content(prompt)

    print("\n📄 Respuesta del modelo:\n")
    print(response.text)

except Exception as e:
    print(f"\n ⚠️ Error: {e}")
