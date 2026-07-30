import yaml
import random
import webbrowser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from action import Action
from sklearn.pipeline import make_pipeline
import weather  # your weather.py file
from sklearn.metrics import accuracy_score, classification_report


# Load YAML
def load_intents(yaml_path):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['intents']

intents = load_intents('intents.yml')

X, y = [], []
responses = {}
actions = {}

for intent in intents:
    tag = intent['tag']
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(tag)
    responses[tag] = intent['responses']
    if 'action' in intent:
        actions[tag] = intent['action']

# Train model
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(X, y)

# Respond and execute
def get_response(user_input):
    predicted_tag = model.predict([user_input])[0]
    response = random.choice(responses[predicted_tag])

    # Perform action if defined
    if predicted_tag in actions:
        action = actions[predicted_tag]
        if action == "get_weather":
            weather_info = weather.get_weather()
            return f"{response} {weather_info}"
        elif action == "play_music":
            webbrowser.open("https://open.spotify.com/")
        elif action == "open_google":
            webbrowser.open("https://google.com/")
        elif action == "shutdown":
            return "Shutting down assistant."
        
    if predicted_tag == "unknown":
        return "call_gemini"
    
    
    return response

# ✅ Step 1: Test data: (input sentence, expected intent tag)

test_data = [
    ("hi there!", "greetings"),
    ("can you play some music?", "music"),
    ("check if it's raining", "weather"),
    ("i want to watch some videos", "youtube"),
    ("open google search", "google"),
    ("what time is it now?", "time"),
    ("close this assistant", "shutdown"),
    ("make me laugh with a joke", "joke"),
    ("remind me about my appointment", "reminder"),
    ("do you know any interesting fact?", "facts"),
    ("tell me how the universe works", "unknown"),
    ("start youtube", "youtube"),
    ("can you google this?", "google"),
    ("set a reminder for my homework", "reminder"),
    ("what's up?", "greetings"),
    ("tell me something funny", "joke"),
    ("do i need a jacket today?", "weather"),
    ("play a song please", "music"),
    ("what time should i leave?", "time"),
    ("exit this program", "shutdown")
]


# ✅ Step 2: Separate inputs and true labels
X_test = [text for text, _ in test_data]
y_true = [label for _, label in test_data]

# ✅ Step 3: Predict with your trained model
y_pred = model.predict(X_test)

# ✅ Step 4: Compare predictions
print("\n--- Predictions ---")
for i in range(len(X_test)):
    print(f"Input: {X_test[i]} | Expected: {y_true[i]} | Predicted: {y_pred[i]}")

# ✅ Step 5: Evaluate accuracy
accuracy = accuracy_score(y_true, y_pred)
print(f"\n✅ Accuracy: {accuracy * 100:.2f}%")

# ✅ Step 6: Detailed report
print("\n📊 Classification Report:")
print(classification_report(y_true, y_pred))
