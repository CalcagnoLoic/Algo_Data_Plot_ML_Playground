import pandas as pd
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np


iris = pd.read_csv("data/iris.csv")
iris = iris.drop(columns=iris.columns[0], axis=1)

"""
1. Write a Python program to split the iris dataset into its attributes (X) and labels (y). The X variable contains the first four columns (i.e. attributes) and y contains the labels of the dataset. 
"""

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
2. Write a Python program using Scikit-learn to split the iris dataset into 70% train data and 30% test data. Out of total 150 records, the training set will contain 105 records and the test set contains 45 of those records.
"""


def split_train_test_70():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
    print("1> Size of train dataset ", len(X_train))
    print("2> Size of test dataset ", len(X_test))


"""
3. Write a Python program using Scikit-learn to convert Species columns in a numerical column of the iris dataframe. To encode this data map convert each value to a number. e.g. Iris-setosa:0, Iris-versicolor:1, and Iris-virginica:2. Now print the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. 
"""


def split_train_test_80():
    y = iris["species"].map({"setosa": 0, "versicolor": 1, "virginica": 2})
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    print("1> Size of train dataset ", len(X_train))
    print("2> Size of test dataset ", len(X_test))


"""
4. Write a Python program using Scikit-learn to split the iris dataset into 70% train data and 30% test data. Out of total 150 records, the training set will contain 105 records and the test set contains 45 of those records. Predict the response for test dataset (SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) using the K Nearest Neighbor Algorithm. Use 5 as number of neighbors.
"""


def predict_variable_70():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)  # entrainement du modèle
    y_pred = knn.predict(X_test)  # on prédit les étiquettes via le modèle de test

    comparison = pd.DataFrame({"True labels": y_test, "Predicted labels": y_pred})
    print(comparison)


"""
5. Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and calculate the accuracy of the model using the K Nearest Neighbor Algorithm. 
"""


def estimate_accuracy_model():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(X_train, y_train)

    print("Accuracy of model: ", knn.score(X_test, y_test))


"""
6. Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm calculate the performance for different values of k.
"""


def estimate_accuracy_various_params():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    for i in range(1, 10):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        score = knn.score(X_test, y_test)

        print(f"The accuracy for {i} neighbors is {score}")


"""
7. Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm and create a plot to present the performance for different values of k. 
"""


def plot_estimate_accuracy_various_params():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    for i in range(1, 10):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        score = knn.score(X_test, y_test)

        plt.bar(i, score)
        plt.text(i, score, str(round(score, 2)), ha="center", va="bottom")

    plt.xticks(range(1, 10))
    plt.xlabel("Hyperparameter K")
    plt.ylabel("Accuracy (%)")
    plt.title("Performance of model by different value of hyperparameter K")
    plt.show()


"""
8. Write a Python program using Scikit-learn to split the iris dataset into 80% train data and 20% test data. Out of total 150 records, the training set will contain 120 records and the test set contains 30 of those records. Train or fit the data into the model and using the K Nearest Neighbor Algorithm and create a plot of k values vs accuracy. 
"""


def plot_estimate_accuracy_dataset():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    train_accuracy = np.empty(9)
    test_accuracy = np.empty(9)

    for i in range(1, 10):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)

        train_accuracy[i - 1] = knn.score(X_train, y_train)
        test_accuracy[i - 1] = knn.score(X_test, y_test)

    plt.plot(range(1, 10), train_accuracy, label="Training set")
    plt.plot(range(1, 10), test_accuracy, label="Testing set")
    plt.title("k-NN dataset performance on hyperparameter K")
    plt.xlabel("Number of neighbors")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()
