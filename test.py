from sklearn.metrics import accuracy_score, classification_report

# ✅ Step 1: Test data: (input sentence, expected intent tag)
test_data = [
    ("play music please", "music"),
    ("what’s the weather like today?", "weather"),
    ("hi", "greetings"),
    ("open youtube", "youtube"),
    ("shutdown the assistant", "shutdown"),
    ("tell me the time", "time"),
    ("search something", "google"),
    ("can you play a video", "youtube"),
    ("tell me a joke", "joke"),
    ("tell me something interesting", "facts"),
    ("remind me to take medicine", "reminder"),
    ("how do black holes work", "unknown")
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
