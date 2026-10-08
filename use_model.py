import pandas as pd
import pickle

# Import the model
def retrive_model(path = "models/best_model.pkl"):
    with open(path, "rb") as f_r:
        return pickle.load(f_r)

model_pipeline = retrive_model()

while True:
    # We give it a title
    sentance = input("Enter the title  ").lower()
    if sentance == "exit":
        break
    # Convert it into a DataFrame
    df = pd.DataFrame({"product_title" : [sentance]})
    # Print the category (list)
    print(model_pipeline.predict(df[["product_title"]]))