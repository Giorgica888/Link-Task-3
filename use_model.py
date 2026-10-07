import pandas as pd
import pickle

def retrive_model(path = "models/best_model.pkl"):
    with open(path, "rb") as f_r:
        return pickle.load(f_r)

model_pipeline = retrive_model()

while True:

    sentance = input("Enter the title  ")
    if sentance == "exit":
        break

    df = pd.DataFrame({"product_title" : [sentance]})
    print(model_pipeline.predict(df[["product_title"]]))