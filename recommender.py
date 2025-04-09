# recommender.py
import pandas as pd

# Load your CSV data
data = pd.read_csv("shl_data.csv")

def recommend_assessments(query):
    keywords = query.lower().split()
    
    # Match if ALL keywords are in the Name field (case-insensitive)
    matched = data[data["Name"].apply(lambda x: all(kw in x.lower() for kw in keywords))]

    # Return the result as a list of dicts
    return matched.to_dict(orient="records")
