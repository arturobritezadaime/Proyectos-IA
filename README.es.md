# 🧠 Cliente Terminal para Google Gemini API

Este proyecto permite interactuar con la API de Google Gemini desde tu terminal de forma sencilla, ideal para pruebas, aprendizaje y desarrollo de soluciones con IA generativa.

## 🚀 Funcionalidades

- ✅ Consultar modelos disponibles (formato tabla con Rich).
- 📝 Enviar prompts simples desde la consola.
- ⏳ Ver barra de progreso mientras se genera contenido.
- 📄 Resultados con formato elegante y colores.
- 📦 Estructura modular con buenas prácticas.

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
└── README.md
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

Y seguí las instrucciones en pantalla para elegir el modelo, escribir tu prompt y ver la respuesta.

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

## 🧠 Autor

César Arturo Britez Adaime  
[@TuGitHub](https://github.com/arturobritezadaime)
