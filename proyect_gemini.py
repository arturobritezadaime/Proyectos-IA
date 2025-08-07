from config import cargar_api_key
from modelos import obtener_modelos, mostrar_modelos
from entrada_usuario import seleccionar_modelo
from generador import generar_contenido
from rich.console import Console

console = Console()

# ================================
# 🔹 Función principal (modo conversacional)
# ================================

def main():
    try:
        cargar_api_key()
        modelos = obtener_modelos()
        mostrar_modelos(modelos)

        modelo_info = seleccionar_modelo(modelos)
        if not modelo_info:
            raise ValueError("❌ Número de modelo no válido.")

        modelo_id = modelo_info["id"]
        historial_conversacion = []

        console.print("\n💬 [bold cyan]Modo conversacional activado.[/bold cyan] Escribí 'salir' para terminar.\n")

        while True:
            prompt = input("Tú: ").strip()
            if prompt.lower() in ["salir", "exit", "quit"]:
                console.print("👋 [bold yellow]Fin de la conversación.[/bold yellow]")
                break

            # Agregar mensaje del usuario al historial
            historial_conversacion.append({"role": "user", "parts": [prompt]})

            # Obtener respuesta del modelo
            respuesta = generar_contenido(modelo_id, historial_conversacion)

            # Mostrar respuesta
            console.print(f"\n🤖 [bold green]Modelo:[/bold green] {respuesta}\n")

            # Agregar respuesta del modelo al historial
            historial_conversacion.append({"role": "model", "parts": [respuesta]})

    except Exception as e:
        console.print(f"\n⚠️ [bold red]Error:[/bold red] {e}", style="red")


# ================================
# 🔹 Ejecutar
# ================================

if __name__ == "__main__":
    main()
