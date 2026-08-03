import pandas as pd
def load_data():
    df = pd.read_csv("C:/Users/Dattu/PycharmProjects/PythonProject2/PlacementPredictionSystem/data/placement_data.csv")
    return df
def get_summary(df):
    return{
        "rows": df.shape[0],
        "columns": df.shape[1],
        "target": "Placement Status"
    }
if __name__ == "__main__":
    df=load_data()
    print(get_summary(df))
    # print(df.head())
    #print(df.info())
    #print(df.describe())
    #print(df.isnull().sum())
    