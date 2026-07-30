# AI Virtual Assistant

A Python-based AI Virtual Assistant that supports voice and text interaction. The assistant recognizes user intents, performs predefined actions, retrieves weather information, and responds using speech through an interactive desktop interface.

---

## Features

* Voice and text input
* Speech-to-text conversion
* Text-to-speech responses
* Intent recognition using a machine learning model
* Weather information retrieval
* Interactive desktop GUI built with Tkinter
* Rule-based action handling
* Fallback response using a language model

---

## Project Structure

```text
AI-Virtual-Assistant/
│
├── GUI.py
├── gui2.py
├── action.py
├── intent_matcher.py
├── speechtotext.py
├── text_to_speech.py
├── weather.py
├── intents.yml
├── requirements.txt
├── datasets/
├── IMAGE/
└── REPORT.pdf
```

---

## Technologies Used

* Python
* Tkinter
* SpeechRecognition
* PyAudio
* pyttsx3
* Scikit-learn
* PyYAML
* BeautifulSoup
* Requests
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/arifh201/AI-Virtual-Assistant.git
```

Move to the project directory:

```bash
cd AI-Virtual-Assistant
```

Install the required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable, install the required libraries manually:

```bash
pip install SpeechRecognition pyttsx3 pyaudio scikit-learn pyyaml requests beautifulsoup4 python-dotenv
```

---

## Configuration

Create a `.env` file in the project directory and add the required API key if you are using the language model fallback.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not upload your `.env` file to GitHub.

---

## Running the Application

Launch the main interface:

```bash
python GUI.py
```

or

```bash
python gui2.py
```

Speak or type a command in the application window.

---

## Example Commands

* What is the weather today?
* Tell me a joke.
* Open the calculator.
* Hello.
* What time is it?

---

## Screenshots

Add screenshots of the application inside the `images/` folder and reference them here.

```markdown
## Home Screen

![Home](images/home.png)

## Voice Input

![Voice](images/voice_input.png)

## Assistant Response

![Response](images/response.png)
```

---

## Project Workflow

```text
User Input
     │
     ▼
Speech/Text Processing
     │
     ▼
Intent Recognition
     │
     ▼
Action Execution
     │
     ▼
Response Generation
     │
     ▼
Text-to-Speech Output
```

---

## Future Improvements

* Add more intents and actions
* Improve intent classification accuracy
* Support additional APIs
* Add conversation history
* Improve the user interface
* Package the application as a desktop executable

---

## Authors

* Arif Hussain
* Shayan Ikram Abbasi

---

## License

This project is developed for educational purposes as part of a university project.
