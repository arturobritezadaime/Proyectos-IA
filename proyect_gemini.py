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


# ================================
# 🔹 Definición de modelos gratuitos
# ================================

def obtener_modelos():
    return {
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


# ================================
# 🔹 Mostrar modelos disponibles
# ================================

def mostrar_modelos(modelos):
    print("\n📌 Modelos gratuitos disponibles:\n")
    for clave, datos in modelos.items():
        print(f"{clave}. {datos['id']}")
        print(f"   → Uso: {datos['uso']}")
        print(f"   → Calidad: {datos['calidad']}")
        print(f"   → Destacado: {datos['característica']}\n")


# ================================
# 🔹 Pedir selección del usuario
# ================================

def seleccionar_modelo(modelos):
    try:
        eleccion = int(input("🔢 Elegí el número del modelo: ").strip())
        return modelos.get(eleccion)
    except ValueError:
        return None


# ================================
# 🔹 Obtener prompt del usuario
# ================================

def obtener_prompt():
    texto = input("\n📝 Escribí el contenido que querés generar: ").strip()
    if not texto:
        raise ValueError("❌ El contenido no puede estar vacío.")
    return texto


# ================================
# 🔹 Generar contenido con modelo
# ================================

def generar_contenido(modelo_id, prompt):
    modelo = genai.GenerativeModel(modelo_id)
    respuesta = modelo.generate_content(prompt)
    return respuesta.text


# ================================
# 🔹 Función principal
# ================================

def main():
    try:
        cargar_api_key()
        modelos = obtener_modelos()
        mostrar_modelos(modelos)

        modelo_info = seleccionar_modelo(modelos)
        if not modelo_info:
            raise ValueError("❌ Número de modelo no válido.")

        prompt = obtener_prompt()
        respuesta = generar_contenido(modelo_info["id"], prompt)

        print("\n📄 Respuesta del modelo:\n")
        print(respuesta)

    except Exception as e:
        print(f"\n⚠️ Error: {e}")


# ================================
# 🔹 Ejecutar
# ================================

if __name__ == "__main__":
    main()
