import google.generativeai as genai
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()

# ================================
# 🔹 Generar contenido con modelo
# ================================

def generar_contenido(modelo_id, prompt):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("🧠 Generando contenido...", total=None)
        time.sleep(1.5)  # Simula carga

        modelo = genai.GenerativeModel(modelo_id)
        respuesta = modelo.generate_content(prompt)

        progress.update(task, description="✅ Contenido generado")
        time.sleep(0.3)

    return respuesta.text