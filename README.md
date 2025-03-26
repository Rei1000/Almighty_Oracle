# 🔮 Almighty Oracle

**Ein unterhaltsames Flask-Webprojekt, das Antworten von verschiedenen KI-Modellen sammelt – gleichzeitig und kostenlos!**  
_A fun and mystical Flask web app that gathers answers from different AI models – simultaneously and for free!_

---

## 🧙‍♂️ Funktionen / Features

- ✍️ Stelle eine beliebige Frage – Ask any question
- 🔀 Wähle mehrere Modelle aus (Vergleichsmodus) – Compare multiple models at once
- ⏱️ Kurzmodus erzwingt kurze Antworten (ideal für Vergleich)  
  _Short mode forces brief replies (ideal for comparison)_
- 🧠 Nutzt OpenRouter.ai (kostenfrei mit API Key) – Uses OpenRouter.ai (free with API key)
- 🧾 Modelle: GPT-3.5 Turbo, Mistral Small 3.1, DeepSeek V3  
  _Models used: GPT-3.5 Turbo, Mistral Small 3.1, DeepSeek V3_

> 💡 **Fun Fact**  
> DeepSeek ist das einzige Modell, das im Langmodus auch chinesische Automarken wie **BYD** oder **Geely** nennt.  
> _DeepSeek is the only model that mentions Chinese car brands like **BYD** or **Geely** in full-answer mode._

---

## 🎮 Bedienungsanleitung / How to Use

🟢 **Vergleichsmodus aktivieren:**  
Wähle mehrere Modelle aus und stelle deine Frage.  
Im Vergleichsmodus werden die Antworten automatisch kurz gehalten.

🔵 **Einzelmodus:**  
Wähle nur ein Modell aus. Die Antwort ist dann ausführlich und in natürlicher Länge.

---

## 🛠️ Installation & Setup

1. **Repo klonen / Clone the repo**
   ```bash
   git clone https://github.com/deinname/almighty-oracle.git
   cd almighty-oracle
   ```

2. **Virtuelle Umgebung aktivieren / Activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Abhängigkeiten installieren / Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **API Key einfügen / Add your API key**  
   Erstelle eine `.env` Datei mit folgendem Inhalt:  
   _Create a `.env` file with:_
   ```
   OPENROUTER_API_KEY=sk-...
   ```

5. **App starten / Start the app**
   ```bash
   python app.py
   ```

---

## 📸 Vorschau / Preview

![App Screenshot](screenshots/orakel_live.jpg)

---

## 🧪 Test-Frage für den Vergleich / Sample test question

> Frage: `Was ist 2 + 2?`  
> Ergebnis: Alle Modelle antworten korrekt. ✅  
> _Question: `What is 2 + 2?` → All models reply correctly._

> Frage: `Welches ist die beste Automarke?`  
> Ergebnis: **DeepSeek** nennt auch **BYD** und **Geely** – andere nicht.  
> _DeepSeek uniquely includes Chinese car brands like **BYD** and **Geely**._

---

## 💬 To Do / Weiteres

- Ergebnisse filtern oder bewerten  
- Mehr Modelle hinzufügen  
- Sprachumschaltung (DE / EN)

---

Viel Spaß beim Orakeln! 😄  
_Have fun querying the Oracle!_
