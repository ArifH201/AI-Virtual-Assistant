
AI Virtual Assistant - README

-------------------------------------
Project Description:
-------------------------------------
This is a Python-based AI Virtual Assistant that can process both voice and text input. It uses 
machine learning to classify intents and execute various actions such as retrieving weather 
information, speaking responses, and handling unknown queries using a fallback language model.

-------------------------------------
Project Structure:
-------------------------------------
- GUI.py / gui2.py         -> Main interface (Tkinter-based GUI)
- intent_matcher.py        -> Intent classification logic
- intents.yml              -> Sample dataset for training intent classifier
- speechtotext.py          -> Converts voice input to text
- text_to_speech.py        -> Converts text responses to speech
- action.py                -> Action routing for recognized intents
- weather.py               -> Scrapes weather data using BeautifulSoup
- .env                     -> Environment variables (e.g., Gemini API key)
- IMAGE/                   -> Icons and screenshots used in the GUI

-------------------------------------
Setup Instructions:
-------------------------------------
1. Clone or unzip the project files.
2. Ensure Python 3 is installed on your system.
3. Install required libraries using pip:
   pip install -r requirements.txt

   If requirements.txt is not available, install manually:
   pip install SpeechRecognition pyttsx3 pyaudio scikit-learn pyyaml requests beautifulsoup4 python-dotenv

4. Make sure your system microphone is accessible (for voice input).

-------------------------------------
How to Run:
-------------------------------------
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the GUI:
   python GUI.py
   (or)
   python gui2.py

4. Speak or type a query in the interface.

-------------------------------------
Notes:
-------------------------------------
- Ensure your internet connection is active for Gemini fallback to function.
- For speech recognition to work, pyaudio must be correctly installed.
- Keep your .env file secure and DO NOT share your API keys publicly.

-------------------------------------
Created by:
Shayan Ikram Abbasi (01-134222-140)
Arif Hussain (01-134222-029)
