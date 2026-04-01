# train.py
# importing libraries 



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib
from sklearn.naive_bayes import MultinomialNB


# loading dataset

df = pd.read_csv("data/spam.csv", encoding="latin-1")

# keeping rggod columns and which is relevant 

df = df[['v1', 'v2']]
df.columns = ['label', 'text']

# naming the labels 
df['label'] = df['label'].map({'ham': 0, 'spam': 1})


# splitting them

X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# vectorizing the code

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# training the  model

model = MultinomialNB(class_prior=[0.3, 0.7])
model.fit(X_train_vec, y_train)

# evaluating the code 

y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# saved model + vectorizer

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")


#printing the result 
print("\nSaved: model.pkl, vectorizer.pkl")

#end of training
