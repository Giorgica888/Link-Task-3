import pandas as pd
import joblib

def retrive_model(path = "models/best_model.joblib"):
    return joblib.load(path)

model_pipeline = retrive_model()

while True:

    sentance = input("Enter the title  ")
    if sentance == "exit":
        break

    df = pd.DataFrame({"product_title" : [sentance]})
    print(model_pipeline.predict(df[["product_title"]]))