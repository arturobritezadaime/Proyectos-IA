import google.generativeai as genai
import os
from dotenv import load_dotenv

# ================================
# 🔹 Cargar configuración y entorno
# ================================

def cargar_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key or not api_key.strip():
        raise ValueError("API_KEY no encontrada o vacía en las variables de entorno.")

    genai.configure(api_key=api_key)