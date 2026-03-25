import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = pd.read_csv('feedback_data.csv')

print("Preview of feedback data:")
print(data.head())

X = data['feedback_text']
y = data['sentiment']

vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

sentiment_counts = data['sentiment'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',
    colors=['green','gray','red']
)
plt.title('Student Feedback Sentiment Distribution')
plt.show()

positive_text = " ".join(data[data['sentiment']=='Positive']['feedback_text'])
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(positive_text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Common Words in Positive Feedback')
plt.show()

print("\n--- Try your own feedback ---")
user_feedback = input("Enter your feedback: ")
user_vector = vectorizer.transform([user_feedback])
prediction = model.predict(user_vector)[0]
print(f"Predicted Sentiment: {prediction}")
