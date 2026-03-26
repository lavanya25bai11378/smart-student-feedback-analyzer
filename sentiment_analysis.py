data = [
    ("The course was very interesting and helpful", "Positive"),
    ("Some topics were confusing and hard to follow", "Negative"),
    ("I liked the practical exercises they helped a lot", "Positive"),
    ("Assignments were too challenging for the time given", "Negative"),
    ("Overall a good learning experience", "Positive")
]

positive_words = ["good", "interesting", "helpful", "liked", "useful", "great"]
negative_words = ["confusing", "hard", "challenging", "difficult", "boring"]

def predict_sentiment(text):
    text = text.lower()
    pos_count = 0
    neg_count = 0

    for word in positive_words:
        if word in text:
            pos_count += 1

    for word in negative_words:
        if word in text:
            neg_count += 1

    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

print("Predictions:\n")

for feedback, actual in data:
    predicted = predict_sentiment(feedback)
    print("Feedback:", feedback)
    print("Actual:", actual)
    print("Predicted:", predicted)
    print()
