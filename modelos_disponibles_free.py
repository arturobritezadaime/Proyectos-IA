import google.generativeai as genai
import os
from dotenv import load_dotenv

# -------------------- Cargar API Key --------------------
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key or not api_key.strip():
    raise ValueError("❌ API_KEY no encontrada o vacía en las variables de entorno.")

genai.configure(api_key=api_key)

# -------------------- Mostrar modelos disponibles --------------------
try:
    modelos = genai.list_models()

    print("\n📌 Modelos disponibles en tu cuenta:\n")

    for model in modelos:
        nombre = model.name
        metodos = model.supported_generation_methods
        soporta_generate = 'generateContent' in metodos

        print(f"🔹 Nombre: {nombre}")
        print(f"   Métodos soportados: {', '.join(metodos)}")
        print(f"   ¿Compatible con generate_content()? {'✅ Sí' if soporta_generate else '❌ No'}\n")

except Exception as e:
    print(f"\n⚠️ Error al obtener la lista de modelos: {e}")
