import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "message": [
        "Congratulations! You won a free prize",
        "Claim your free cash reward now",
        "Win a free iPhone today",
        "You have won a lottery prize",
        "Click this link to get free money",
        "Limited offer! Claim your reward",
        "Get free coupons now",
        "You are selected for a cash prize",
        "Free gift waiting for you",
        "Congratulations, you won a reward",

        "Hello, how are you?",
        "Can we meet tomorrow?",
        "Please send me the notes",
        "Your class starts at 10 AM",
        "Don't forget the meeting",
        "I will call you later",
        "Can you help me with this work?",
        "See you tomorrow",
        "Please submit the assignment",
        "Good morning, have a nice day"
    ],
    "label": [
        "spam", "spam", "spam", "spam", "spam",
        "spam", "spam", "spam", "spam", "spam",
        "not spam", "not spam", "not spam", "not spam", "not spam",
        "not spam", "not spam", "not spam", "not spam", "not spam"
    ]
}

df = pd.DataFrame(data)

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Spam Message Detection")
print("----------------------")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Test new messages
while True:
    message = input("\nEnter a message (or type 'exit'): ")

    if message.lower() == "exit":
        print("Program ended.")
        break

    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)

    print("Prediction:", prediction[0])