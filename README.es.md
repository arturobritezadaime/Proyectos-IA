# 🧠 Cliente Terminal para Google Gemini API

Este proyecto permite interactuar con la API de Google Gemini desde tu terminal de forma sencilla, ideal para pruebas, aprendizaje y desarrollo de soluciones con IA generativa.

## 🚀 Funcionalidades

- Modo Conversacional: Interactúa de forma continua con el modelo, manteniendo el historial de la conversación.
- Selección de Modelos: Elige entre una lista de modelos gratuitos disponibles.
- Visualización mejorada: Consulta los modelos en un formato de tabla claro con la librería rich.
- Barra de Progreso: Muestra un spinner mientras el modelo genera la respuesta.
- Guardar Conversación: Al finalizar, tienes la opción de guardar el historial completo de la conversación en formato .txt, .docx o .csv.
- Manejo de errores: El programa gestiona errores, como una API key faltante o una selección de modelo inválida.

## 📁 Estructura del proyecto

```
proyecto_gemini_terminal/
├── .env
├── config.py
├── entrada_usuario.py
├── generador.py
├── modelos.py
├── proyect_gemini.py
├── requirements.txt
├── README.md
├── README.es.md
└── README.en.md
```

## 🛠️ Requisitos

- Python 3.10 o superior
- Cuenta y API Key de Google Gemini: https://makersuite.google.com/app

## 🔧 Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/arturobritezadaime/Proyectos-IA.git
cd Proyectos-IA

# 2. Crea y activa el entorno virtual
python -m venv .venv
.venv\Scripts\activate       # En Windows
source .venv/bin/activate     # En macOS/Linux

# 3. Instala dependencias
pip install -r requirements.txt
```

## 🔐 Configuración

Crea un archivo `.env` con el siguiente contenido:

```
API_KEY=tu_api_key_de_google
```

## ▶️ Ejecución

```bash
python proyect_gemini.py
```

El programa te guiará para seleccionar un modelo y empezar la conversación. Escribe "salir" o "exit" o "quit" para terminar el chat. Al finalizar, te preguntará si deseas guardar el historial.

## 📷 Captura de consola

```
📌 Modelos gratuitos disponibles
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ N° ┃ ID del modelo                ┃ Uso                                    ┃ Calidad       ┃ Destacado                        ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ models/gemini-2.5-pro        │ Generación de contenido más largo      │ Alta calidad  │ Ideal para escritura y análisis  │
│ 2  │ models/gemini-2.5-flash      │ Respuestas rápidas y eficientes        │ Buen costo    │ Pensamiento adaptativo           │
│ ...│ ...                          │ ...                                    │ ...           │ ...                              │
└────┴──────────────────────────────┴────────────────────────────────────────┴───────────────┴───────────────────────────────────┘
```

## 🤖 Tecnologías utilizadas

- Python 3.10+
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [rich](https://pypi.org/project/rich/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- python-docx: Para guardar el historial en formato .docx.

## 🧠 Autor

César Arturo Britez Adaime  
[@Git](https://github.com/arturobritezadaime)
