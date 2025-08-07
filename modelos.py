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
