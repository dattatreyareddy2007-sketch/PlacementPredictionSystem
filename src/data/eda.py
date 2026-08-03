from src.data.load_data import load_data
def basic_eda(df):
    print("First five rows")
    print(df.head())
    print("Last five rows:")
    print(df.tail())
    print("25 to 35 rows:")
    print(df.iloc[25:36])
    print("Sample of 10 records:")
    print(df.sample(10))
    print("Sample of 25 records:")
    print(df.sample(25))

if __name__ == "__main__":
    df = load_data()
    basic_eda(df)

