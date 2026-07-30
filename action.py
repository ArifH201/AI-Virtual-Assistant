#defines the backend logic

import os
from dotenv import load_dotenv
import text_to_speech
import datetime
import weather
import webbrowser
from intent_matcher import get_response  # NEW

# Load Gemini API
import google.generativeai as genai
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
model = None

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    except Exception as e:
        print(f"Error initializing Gemini model: {e}")
else:
    print("Error: GEMINI_API_KEY not found.")

def call_gemini(prompt):
    if model is None:
        return "Sorry, I can't answer that."
    try:
        response = model.generate_content(
            f"You are an AI assistant. User said: {prompt}. Respond briefly.in one line"
        )
        reply = response.text.strip()
        if not reply or "sorry" in reply.lower():
            return "Sorry, I don’t know."
        return reply
    except Exception as e:
        print("Gemini error:", e)
        return "Sorry, I don’t know."

def action(data):
    user_input = data.lower()

    try:
        reply = get_response(user_input)
        if reply:
            text_to_speech.text_to_speech(reply)
            return reply
        fallback = call_gemini(user_input)
        text_to_speech.text_to_speech(fallback)
        return fallback
    except Exception as e:
        print("Error in action():", e)
        error_reply = "Sorry, something went wrong."
        text_to_speech.text_to_speech(error_reply)
        return error_reply
