# 🧠 Terminal Client for Google Gemini API

This project allows you to interact with the Google Gemini API directly from your terminal in a simple way—ideal for testing, learning, and developing solutions with generative AI.

## 🚀 Features

- **Conversational Mode:** Continuously interact with the model while keeping the full conversation history.  
- **Model Selection:** Choose from a list of available free models.  
- **Enhanced Visualization:** View models in a clean table format using the `rich` library.  
- **Progress Indicator:** Displays a spinner while the model generates a response.  
- **Save Conversation:** At the end, you can save the full conversation history in `.txt`, `.docx`, or `.csv` format.  
- **Error Handling:** The program handles errors such as missing API keys or invalid model selections.  

## 📁 Project Structure

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

## 🛠️ Requirements

- Python 3.10 or higher  
- Google Gemini account and API Key: https://makersuite.google.com/app  

## 🔧 Installation

```bash
# 1. Clone the repository
git clone https://github.com/arturobritezadaime/Proyectos-IA.git
cd Proyectos-IA

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate       # On Windows
source .venv/bin/activate    # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

## 🔐 Configuration

Create a `.env` file with the following content:

```
API_KEY=your_google_api_key
```

## ▶️ Usage

```bash
python proyect_gemini.py
```

The program will guide you to select a model and start chatting.  
Type `"exit"`, `"quit"`, or `"salir"` to end the session.  
At the end, you will be asked if you want to save the conversation history.

## 📷 Terminal Screenshot

```
📌 Available Free Models
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ #  ┃ Model ID                      ┃ Usage                                  ┃ Quality       ┃ Highlight                         ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1  │ models/gemini-2.5-pro         │ Longer content generation              │ High quality  │ Ideal for writing and analysis    │
│ 2  │ models/gemini-2.5-flash       │ Fast and efficient responses           │ Cost-effective│ Adaptive reasoning                │
│ ...│ ...                           │ ...                                    │ ...           │ ...                               │
└────┴──────────────────────────────┴────────────────────────────────────────┴───────────────┴───────────────────────────────────┘
```

## 🤖 Technologies Used

- Python 3.10+  
- [google-generativeai](https://pypi.org/project/google-generativeai/)  
- [rich](https://pypi.org/project/rich/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  
- python-docx: For saving conversation history in `.docx` format.  

## 🧠 Author

César Arturo Britez Adaime  
[@Git](https://github.com/arturobritezadaime)  
