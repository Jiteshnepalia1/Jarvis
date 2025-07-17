
# 🧠 Jarvis – AI Voice Assistant

**Jarvis** is a Python-based voice assistant inspired by virtual assistants like **Alexa** and **Google Assistant**. It uses voice recognition and AI models to execute commands, play YouTube videos, fetch weather/news, launch/close apps, and interact through natural language using the **Groq API** with LLaMA and Compound models.

---

## 🚀 Features

- 🎙️ Wake-word detection ("Jarvis")
- 🧠 Natural language understanding via Groq (LLaMA 3.3 & Compound Beta)
- 📺 Play YouTube videos using `pywhatkit`
- 🌐 Open and close websites
- 🖥️ Launch and close desktop apps
- ☁️ Fetch live weather updates
- 📰 Read top news headlines using NewsAPI
- 🔊 Text-to-speech output with `pyttsx3`
- 🔉 Beep alert before command recognition
- 🔒 API key protection via `.env` file

---

## 🛠️ Requirements

Install all dependencies using pip:

```bash
pip install -r requirements.txt
```

**`requirements.txt`** should contain:

```text
python-dotenv
speechrecognition
pyttsx3
pywhatkit
requests
groq
```

Also install PyAudio (if not already):

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 📁 Project Structure

```
Jarvis/
│
├── apps.py                # Custom dictionary for app paths
├── browser.py             # Custom dictionary for websites
├── main.py                # Main assistant script
├── .env                   # Environment variables (API keys)
├── beep2.wav              # Beep sound to activate listener
└── README.md              # Documentation (you are here)
```

---

## 🔐 .env Configuration

Create a `.env` file in the project root with the following:

```env
ai=your_groq_ai_api_key
weather=your_groq_weather_api_key
newsapi=your_newsapi_org_key
```

> ✅ Do NOT share or commit your API keys publicly. Add `.env` to `.gitignore`.

---

## 🧠 Voice Commands (Examples)

| Command                | Action                                  |
|------------------------|-----------------------------------------|
| `Jarvis`               | Wake up the assistant                   |
| `Open YouTube`         | Opens YouTube in browser                |
| `Start notepad`        | Launches Notepad from app list          |
| `Play Imagine Dragons` | Plays YouTube video                     |
| `What's the weather`   | Gives current weather info              |
| `News`                 | Reads top headlines                     |
| `Close notepad`        | Terminates app                          |
| `Close YouTube`        | Kills browser instance                  |
| `Who are you?`         | AI-generated response                   |

---

## 🔊 Voice Engine Settings

- **TTS Engine**: `pyttsx3`
- **Rate**: 170 words per minute
- **Voice**: Default system voice (customizable)

---

## ⚙️ Custom Modules

### `apps.py`
```python
aap_paths = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe"
}
```

### `browser.py`
```python
wep_page = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com"
}
```

> ✅ Expand these files for more sites and apps.

---

## ✅ To Run

Run the assistant from the terminal:

```bash
python main.py
```

Ensure your mic and audio output are configured correctly.

---

## 📢 Notes

- Internet connection is required for all API interactions.
- Use noise-canceling microphones for better recognition.
- Tune `timeout` and `phrase_time_limit` values in the recognizer for best results.

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Jitesh Nepalia**  
_Developer of Jarvis Voice Assistant_  
Feel free to contribute or suggest improvements!
