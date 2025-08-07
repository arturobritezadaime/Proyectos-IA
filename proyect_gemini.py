from config import cargar_api_key
from modelos import obtener_modelos, mostrar_modelos
from entrada_usuario import seleccionar_modelo, obtener_prompt
from generador import generar_contenido
from rich.console import Console

# ================================
# 🔹 Función principal
# ================================

console = Console()

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

        console.print("\n📄 [bold green]Respuesta del modelo:[/bold green]\n")
        console.print(respuesta, style="white")

    except Exception as e:
        console.print(f"\n⚠️ [bold red]Error:[/bold red] {e}", style="red")


# ================================
# 🔹 Ejecutar
# ================================

if __name__ == "__main__":
    main()
