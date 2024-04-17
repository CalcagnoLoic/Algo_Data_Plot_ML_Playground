from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


iris = pd.read_csv("data/iris.csv")
iris = iris.drop(columns=iris.columns[0], axis=1)
setosa_df = iris[iris["species"] == "setosa"]
versicolor_df = iris[iris["species"] == "versicolor"]
virginica_df = iris[iris["species"] == "virginica"]

X = iris[
    [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
]
y = iris["species"]


"""
1. Write a Python program to view some basic statistical details like percentile, mean, std etc. of the species of 'Iris-setosa', 'Iris-versicolor' and 'Iris-virginica'. 
"""


def basic_statistics_by_species():
    print(setosa_df.describe())
    print(versicolor_df.describe())
    print(virginica_df.describe())


"""
2. Write a Python program to create a scatter plot using sepal length and petal_width to separate the Species classes.
"""


def plot_sepal_petal():
    process = preprocessing.LabelEncoder()
    iris.species = process.fit_transform(iris.species)

    X = X.values
    y = y.values

    plt.scatter(X[:, 0], X[:, 3], c=y, cmap="flag")
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Petal length (cm)")
    plt.legend()
    plt.savefig("plots/logistic2.png")


"""
3. Write a Python program to get the accuracy of the Logistic Regression.
"""


def get_logistic_regression():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    model = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)

    print(
        "The accuracy of logistic regression is: ",
        metrics.accuracy_score(prediction, y_test),
    )
