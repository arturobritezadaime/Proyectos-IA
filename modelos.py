# ================================
# 🔹 Definición de modelos gratuitos
# ================================
from rich.console import Console
from rich.table import Table

console = Console()

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
    table = Table(title="📌 Modelos gratuitos disponibles", title_style="bold cyan")
    table.add_column("N°", justify="center", style="bold yellow")
    table.add_column("ID del modelo", style="white")
    table.add_column("Uso", style="italic")
    table.add_column("Calidad", style="green")
    table.add_column("Destacado", style="magenta")

    for clave, datos in modelos.items():
        table.add_row(
            str(clave),
            datos["id"],
            datos["uso"],
            datos["calidad"],
            datos["característica"]
        )

    console.print(table)
