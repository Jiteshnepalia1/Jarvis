# ------------------------------------------------------------------------------------------------------
# Load Environment Variables
# ------------------------------------------------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file into the environment


# ------------------------------------------------------------------------------------------------------
# Standard Library Imports
# ------------------------------------------------------------------------------------------------------
import os                                                 # Operating system interaction
import asyncio                                            # Asynchronous I/O
import webbrowser                                         # Open web pages in a browser
import winsound                                           # Play simple sounds on Windows


# -------------------------------------------------------------------------------------------------------
# Third-Party Library Imports
# -------------------------------------------------------------------------------------------------------
import speech_recognition as sr                           # Speech-to-text conversion
import pyttsx3                                            # Text-to-speech synthesis
import requests                                           # HTTP requests
import pywhatkit                                          # WhatsApp, YouTube, and other automation tools


# -------------------------------------------------------------------------------------------------------
# External/Custom Module Imports
# -------------------------------------------------------------------------------------------------------
from groq import Groq                                     # Access Groq language models via API
import apps                                               # Custom module for managing local applications
import browser                                            # Custom module for browser automation/control

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speech rate (words per minute) for the text-to-speech engine; default is usually ~200
engine.setProperty("rate",170)

# Initialize News API client (example using requests or a specific wrapper)

# Speaks the given text aloud using the text-to-speech engine
def speak(text):
    engine.say(text)     # Queue the text for speech
    engine.runAndWait()  # Process and speak the queued text

# Function to play a YouTube video based on the user's query
def play_youtube_video(query):
    speak(f"{query} on YouTube")   # Announce the video being played
    pywhatkit.playonyt(query)              # Use pywhatkit to open and play the video on YouTube

# Function to process user commands using the Groq AI model
def aiProcess(command):
    # Initialize the Groq client with your API key
    client = Groq(
    api_key=os.getenv('ai')
    )

    # Create a chat completion request with system and user messages
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"system",  # System prompt to set assistant behavior (can be customized)
            "content": "You are a virtual assistent named jarvis skilled in general task like Alexa and Google Cloud. Give short responses please",
            # Instruction for the AI to behave like a virtual assistant named Jarvis, offering concise replies
        },
        {
            "role":"user",   # User prompt from voice or text input
         "content":command   # Dynamic user input captured through voice recognition
        }
    ],
    model="llama-3.3-70b-versatile",   # Specify the LLaMA model to use
    )

    # Return the AI-generated response text
    return chat_completion.choices[0].message.content

# Function to fetch weather or similar info using a Groq language model
def weather(command):
                try:
                    # Initialize Groq client with API key (consider using env vars in real projects)
                    client = Groq(
                    api_key=os.getenv('weather')
                    )

                    user_query = command   # Voice command passed as input


                    # Request response from the Groq Compound Beta model
                    chat_completion = client.chat.completions.create(
                    messages=[
                        {

                            "role": "system",  # Defines the role of the message for the language model (system message sets behavior)
                            "content": "Summarize weather reports in 4-5 lines with key data only.",  # Instruction to the AI for concise weather summarization
                        },
                        {
                            "role": "user",   # Indicates this message is from the user (i.e., the actual query or input to the AI)
                            "content": user_query,  # The user's voice command or input passed to the AI model
                        }
                    ],

                    model="compound-beta",   # Model used for conversational AI
                    )

                    # Extract and print the response from the AI
                    print(f"Query: {user_query}")
                    print(f"Compound Beta Response:\n{chat_completion.choices[0].message.content}")
                    
                    # Speak the response aloud
                    speak(f"Compound Beta Response:\n{chat_completion.choices[0].message.content}")
                except Exception as e:
                    # Handle potential errors (e.g., network, API failure)
                    print(f"An error occurred: {e}")
                    speak("Sorry, I couldn't fetch the weather information.")

# Function to process voice commands related to opening websites           
def processCommand(c):
    # Handle commands that start with 'open' to open a website
    if c.lower().startswith("open"):
        web = c.lower().split(" ")[1]   # Extract website keyword
        link = browser.wep_page[web]    # Fetch the URL from custom dictionary
        speak(f"opening {web}")         # Announce the action
        webbrowser.open(link)           # Open the link in default browser

    # Handle commands that start with 'start' to launch an application    
    elif c.lower().startswith("start"):
        app = c.lower().split(" ")[1]   # Extract app keyword
        path = apps.aap_paths[app]      # Get the path from custom dictionary
        speak(f"opening {app}")         # Announce the action
        os.system(path)                 # Launch the app using system command
    
    # Handle a specific command to launch Microsoft Edge browser
    elif "launch edge" in c.lower():
        speak("Launch Edge")    # Announce launching Edge
        os.system(r'"C:\Users\Public\Desktop\Microsoft Edge.lnk"')   # Run Edge shortcut
    
    # Handle 'play' command to play a YouTube video
    elif c.lower().startswith("play"):
        asyncio.run(play_youtube_video(c.lower()))   # Play video using async YouTube function
    
    # Handle commands that mention 'news' to fetch top headlines
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('newsapi')}")   # Fetch news
        data = r.json()                                # Parse JSON response
        if r.status_code == 200 and data["status"] == "ok":
            articles = data["articles"]                 # Extract articles list
            print("Top Headlines:\n")
            for i, article in enumerate(articles):    # Iterate through each article
                print(f"{i+1}. {article['title']}")   # Print headline
                speak(f"{i+1}. {article['title']}")   # Read aloud headline
        else:
            print("Failed to fetch news:", data.get("message", "Unknown error"))   # Error handling
    
    # Handle weather-related queries
    elif c.lower().startswith("what's the weather"):
        output = weather(c)                          # Call weather function
        print(output)                                # Print the response
    
    # Handle commands that start with 'close' to terminate applications
    elif c.lower().startswith("close"):
        app = c.lower().split(" ")[1]                  # Extract app name
        if "close youtube" in c.lower():
            os.system("taskkill /f /im chrome.exe")    # Kill Chrome
            os.system("taskkill /f /im msedge.exe")    # Kill Edge
            speak("Closed YouTube tab.")               # Confirm action

        elif f"{app}" in c.lower():
            os.system(f"taskkill /f /im {app}.exe")   # Kill specified app
            os.system("taskkill /f /im msedge.exe")   # Kill Edge
            speak(f"{c.lower()} tab.")                # Confirm action
        
        else:
            # os.system("taskkill /f /im chrome.exe")  # Default: close Chrome
            os.system("taskkill /f /im msedge.exe")    # Default: close Edge
            speak(f"{c.lower()} tab.")                 # Confirm fallback action
    
    # Handle all other commands using AI model
    else:
        output = aiProcess(c)                         # Send input to AI model
        print(output)                                 # Print AI response
        speak(output)                                 # Speak the response

def main():
    # Speak the initial greeting when the assistant starts
    speak("Hello, I am Jarvis. How can I assist you today?")

    while True:
        # Initialize speech recognizer
        r = sr.Recognizer()
        r.energy_threshold = 200             # Lower threshold for more sensitivity
        r.pause_threshold = 0.5              # Time to wait before considering speech complete
            
        try:
            # Capture input from the microphone
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)   # Adjust for background noise
                print("Listning...")
                audio = r.listen(source,timeout=5,phrase_time_limit=5)   # Listen for wake word

            word = r.recognize_google(audio)   # Recognize spoken wake word

            if(word.lower() == "jarvis"):   # Check for wake word
                # Listen for actual user command
                with sr.Microphone() as source:
                    winsound.PlaySound("beep2.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)   # Play activation sound
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout=4,phrase_time_limit=7)   # Listen for full command
                    command = r.recognize_google(audio)   # Recognize spoken command
                    
                    # Execute command using assistant logic
                    # asyncio.run(processCommand(command))  # Optional: use if processCommand is async
                    processCommand(command)  # Call the main processing function

        except Exception as e:
            # Handle any exceptions that occur during voice recognition or processing
            print("Error; {0}".format(e))

if __name__ == "__main__":
    # Entry point of the script when run directly
    # asyncio.run(main())        # Optional: Use this if main() contains async code
    main()                       # Call the main function to start the assistant
