from src.data.load_data import load_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def basic_eda(df):
    print("First five rows")
    print(df.head())
    print("-----------------------------------------------------------------------------------------")
    print("Last five rows")
    print(df.tail())
    print("-----------------------------------------------------------------------------------------")
    print("from row 25 to 35")
    print(df.iloc[25:36])
    print("-----------------------------------------------------------------------------------------")
    print("random rows")
    print(df.sample(10))
    print("-----------------------------------------------------------------------------------------")
    print("Column Names")
    print(df.columns)
    print("-----------------------------------------------------------------------------------------")
    print("datatypes:")
    print(df.dtypes)
    print("-----------------------------------------------------------------------------------------")
    print("Complete Information")
    df.info()
    print("-----------------------------------------------------------------------------------------")
    print("Data Summary")
    print(df.describe())
    print("-----------------------------------------------------------------------------------------")
    print("Columns with null values")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    print("-----------------------------------------------------------------------------------------")
    print("Target variable status")
    print(df["PlacementStatus"].value_counts())

    count = df["PlacementStatus"].value_counts()
    plt.figure(figsize=(6,5))
    plt.title("Distribution of Placement Status")
    plt.bar(count.index, count.values)
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\placement_status.png")
    plt.show()


def univariate(df):
    plt.figure(figsize=(6,5))
    plt.hist(df["CGPA"], bins=10, edgecolor="black")
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\CGPA_hist.png")
    plt.show()

    gendercount = df["Gender"].value_counts()
    plt.figure(figsize=(6,5))
    plt.pie(gendercount, labels=gendercount.index, autopct="%1.1f%%", startangle=90)
    plt.title("Gender Distribution Piechart")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\gender_distribution.png")
    plt.show()


def bivariate(df):
    # Scatter plot
    plt.figure(figsize=(6,5))
    plt.scatter(df["CGPA"], df["AptitudeTestScore"])
    plt.title("CGPA vs Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\cgpa_aptitudescore_scatter.png")
    plt.show()
    plt.close()

    # Boxplot
    plt.figure(figsize=(6,5))
    placed = df[df["PlacementStatus"] == 1]["CGPA"]
    not_placed = df[df["PlacementStatus"] == 0]["CGPA"]
    plt.boxplot([placed, not_placed], label=["Placed","Not Placed"])
    plt.title("CGPA vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("CGPA")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\boxplot.png")
    plt.show()
    plt.close()



def multivariate(df):
    data = df[["CGPA", "AptitudeTestScore", "PlacementStatus"]]
    correlation = data.corr()
    plt.figure(figsize=(6,5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(r"C:\Users\Dattu\PycharmProjects\PythonProject2\PlacementPredictionSystem\app\static\charts\heatmap.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    df = load_data()
    basic_eda(df)
    univariate(df)
    bivariate(df)
    multivariate(df)
