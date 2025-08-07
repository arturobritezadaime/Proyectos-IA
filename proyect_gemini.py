from config import cargar_api_key
from modelos import obtener_modelos, mostrar_modelos
from entrada_usuario import seleccionar_modelo, obtener_prompt
from generador import generar_contenido

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
