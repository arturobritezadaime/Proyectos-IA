
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