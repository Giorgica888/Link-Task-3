import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.naive_bayes import  MultinomialNB, BernoulliNB, ComplementNB
import pickle

df = pd.read_csv("data/finished_products.csv")
df.category_label = df.category_label.astype("category")

X = df[["product_title"]]
y = df["category_label"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y, shuffle=True
)

def train_model(model):
    preprocessor = ColumnTransformer(
        transformers= [
            ("title", TfidfVectorizer(), "product_title"),
        ]
    )

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("classifier", model)
    ])
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    c_report = classification_report(y_test, y_pred, output_dict=True)

    metrics = {
    "model": str(model)[:-2],
    "model_weights" : pipeline,
    "average_score": round(c_report["accuracy"], 3),
    "precision": round(c_report["macro avg"]["precision"], 3),
    "f1-score": round(c_report["macro avg"]["f1-score"], 3),
    "recall": round(c_report["macro avg"]["recall"], 3),
    }
    return metrics


results = []
for i in [RandomForestClassifier(), LinearSVC(), SVC(), MultinomialNB(), BernoulliNB(), ComplementNB()]:
    print(i)
    in_rez= train_model(i)
    print(in_rez)
    results.append(in_rez)

model = max(results, key=lambda d: d["f1-score"])["model_weights"]

with open("models/best_model.pkl", "wb") as f_w:
    pickle.dump(model, f_w)