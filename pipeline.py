import pandas as pd

def load_dataset(path="dataset.csv"):
    df = pd.read_csv(path)

    print(f"Loaded {len(df)} examples")
    print(df.head())

    return df

if __name__ == "__main__":
    load_dataset()
