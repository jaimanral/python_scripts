import pandas as pd

def clean_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna()
    df.to_csv(output_file, index=False)
    print("Data cleaned and saved")

if __name__ == "__main__":
    clean_csv("data.csv", "clean_data.csv")
