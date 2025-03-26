"""
Flask-Webanwendung: "Almighty Oracle"

Diese App zeigt eine einfache Website, auf der Nutzer eine Frage eingeben können.
Je nach gewähltem Modell (z. B. GPT, Mistral usw. via OpenRouter) wird die Frage an eine KI-API gesendet,
und die Antwort wird auf der Website angezeigt.
"""

# ========== Benötigte Bibliotheken importieren ==========
import os
import json
import requests  # Für HTTP-Requests an die OpenRouter API
from dotenv import load_dotenv  # Für das Einlesen der .env-Datei mit API-Schlüssel
from flask import Flask, render_template, request  # Flask-Komponenten

# ========== API-Key aus .env laden ==========
load_dotenv()

# ========== Flask-App initialisieren ==========
app = Flask(__name__)

# ========== Funktion zur Anfrage an OpenRouter ==========
def ask_openrouter(prompt, model, short_answer=False):
    """
    Stellt eine Anfrage an die OpenRouter API mit dem gegebenen Prompt und Modell.

    :param prompt: Die Nutzerfrage als Text
    :param model: Der Modellname (z. B. "openai/gpt-3.5-turbo")
    :param short_answer: Wenn True, wird das Modell gebeten, sich kurz zu fassen
    :return: Die textuelle Antwort des Modells
    """

    # Wenn im Vergleichsmodus → Prompt anpassen
    if short_answer:
        prompt += " Antworte in kürzester Form."

    # Header vorbereiten
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",  # API-Schlüssel aus .env
        "HTTP-Referer": "http://localhost",  # Kann später mit echter URL ersetzt werden
        "X-Title": "Almighty Oracle",  # Projekttitel
        "Content-Type": "application/json"
    }

    # Daten (Payload) vorbereiten
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Anfrage senden
    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers,
                             data=json.dumps(data))

    # Antwort verarbeiten
    try:
        response_json = response.json()
        result = response_json['choices'][0]['message']['content']
    except (KeyError, IndexError, json.JSONDecodeError):
        result = "Fehler beim Verarbeiten der Antwort."
    return result

# ========== Route für die Hauptseite ==========
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Startseite der Web-App.
    GET zeigt das Formular, POST verarbeitet die Frage und zeigt Antworten der KI-Modelle.
    """
    answer = None

    # Liste verfügbarer Modelle (frei & spannend)
    available_models = [
        ("openai/gpt-3.5-turbo", "GPT-3.5 Turbo"),
        ("mistralai/mistral-small-3.1-24b-instruct:free", "Mistral Small 3.1"),
        ("deepseek/deepseek-chat-v3-0324:free", "DeepSeek V3")
    ]

    if request.method == 'POST':
        # Frage und ausgewählte Modelle aus dem Formular auslesen
        question = request.form.get('question')
        selected_models = request.form.getlist('model')

        print("Formulardaten:", request.form)

        # Mehrere Modelle → Kurzmodus aktivieren
        short_mode = len(selected_models) > 1

        # Antworten abrufen
        answers = {}
        for model in selected_models:
            response = ask_openrouter(question, model, short_answer=short_mode)
            answers[model] = response

        # Antworten + Frage + Modellnamen ans Template weitergeben
        return render_template('index.html',
                               answer=answers,
                               question=question,
                               models=available_models,
                               selected_models=selected_models)

    # Bei GET: nur Seite + Modelle anzeigen
    return render_template('index.html',
                           models=available_models,
                           selected_models=[])

# ========== App starten ==========
if __name__ == "__main__":
    app.run(debug=True)
