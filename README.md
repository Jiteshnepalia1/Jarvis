
# 🧠 Jarvis – AI Voice Assistant

Jarvis is a Python-based voice assistant inspired by popular virtual assistants like Alexa and Google Assistant. It supports voice commands to launch apps, browse websites, fetch news/weather, and interact with LLMs for intelligent responses.

---

## 📌 Features

- 🎙️ Wake word detection (`"Jarvis"`)
- 🗣️ Speech-to-text & text-to-speech (Google + pyttsx3)
- 🌐 Open apps and websites via voice
- 🧠 Smart response via Groq AI (LLaMA & Compound Beta models)
- 📺 Play YouTube videos
- ☁️ Get real-time weather updates
- 📰 Fetch top news headlines
- ❌ Close apps/webpages with voice

---

## 🛠️ Tech Stack

| Purpose             | Library/Tool           |
|---------------------|------------------------|
| Voice Input         | `speech_recognition`   |
| Voice Output        | `pyttsx3`              |
| LLM Interaction     | `Groq`                 |
| Web Operations      | `webbrowser`, `requests`, `pywhatkit` |
| Custom Logic        | `apps.py`, `browser.py` |
| OS Interactions     | `os`, `winsound`       |

---

## 📁 Project Structure

```
Jarvis/
│
├── main.py                # Entry point for Jarvis
├── apps.py                # App path dictionary for launching apps
├── browser.py             # Website link dictionary
├── requirements.txt       # List of dependencies
└── beep2.wav              # Activation sound
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/jarvis-assistant.git
cd jarvis-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set API Keys
Edit the following:
- `newsapi = "<YOUR_NEWS_API_KEY>"`
- `api_key` in `Groq(...)`

### 4. Run Jarvis
```bash
python main.py
```

---

## 🧪 Example Commands

| Command Example           | Behavior                                 |
|---------------------------|------------------------------------------|
| `"Jarvis"`                | Activates the assistant                  |
| `"Open YouTube"`          | Opens YouTube in default browser         |
| `"Start Notepad"`         | Launches Notepad                         |
| `"Play Despacito"`        | Plays the video on YouTube               |
| `"What's the weather"`    | Fetches weather info using LLM           |
| `"News"`                  | Reads top headlines                      |
| `"Close WhatsApp"`        | Terminates the app using taskkill        |

---

## ⚙️ Customization

- **Apps/Browser Links:** Update `apps.py` and `browser.py` with your own application paths and URLs.
- **Text-to-Speech Rate:** Adjust via `engine.setProperty("rate", 170)` in `main.py`.

---

## 🧩 Dependencies

Add to `requirements.txt`:
```txt
pyttsx3
speechrecognition
requests
pywhatkit
groq
```

---

## 🚧 Known Issues

- Only works on Windows (`os.system`, `winsound`)
- Internet required for voice recognition and LLM calls
- No fallback if wake word is not heard correctly
- Needs `beep2.wav` in root directory

---

## 👨‍💻 Author

**Jitesh Nepalia**  
**Developed using Python and cutting-edge AI technologies to enhance productivity and automation.**
