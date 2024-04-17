import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import mpl_toolkits.mplot3d
from sklearn import decomposition
import numpy as np

iris = pd.read_csv("data/iris.csv")
iris = iris.drop(columns=iris.columns[0], axis=1)
setosa_df = iris[iris["species"] == "setosa"]
versicolor_df = iris[iris["species"] == "versicolor"]
virginica_df = iris[iris["species"] == "virginica"]

"""
1. Write a Python program to create a plot to get a general Statistics of Iris data. 
"""


def get_statistics_plot():
    iris.describe().plot(kind="area")
    plt.xlabel(
        "Statistics",
    )
    plt.ylabel("Value")
    plt.title("General Statistics of Iris Dataset")
    plt.savefig("plots/exo1.png")


"""
2. Write a Python program to create a Bar plot to get the frequency of the three species of the Iris data. 
"""


def get_barplot():
    count = iris["species"].value_counts()
    count.plot(kind="bar")
    plt.title("Frequency of iris species")
    plt.xticks(rotation=45)
    plt.savefig("plots/exo2.png")


"""
3. Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data. 
"""


def get_pieplot():
    count = iris["species"].value_counts()
    plt.pie(count, explode=[0.1, 0.1, 0.1], shadow=True, autopct="%1.1f%%")
    plt.title("Frequency of iris species")
    plt.savefig("plots/exo3.png")


"""
4. Write a Python program to create a graph to find relationship between the sepal length and width. 
"""


def relationship_sl_sw():
    plt.scatter(
        setosa_df["sepal length (cm)"],
        setosa_df["sepal width (cm)"],
        label="Iris setosa",
    )
    plt.scatter(
        versicolor_df["sepal length (cm)"],
        versicolor_df["sepal width (cm)"],
        label="Iris versicolor",
    )
    plt.scatter(
        virginica_df["sepal length (cm)"],
        virginica_df["sepal width (cm)"],
        label="Iris virginica",
    )
    plt.legend()
    plt.title("Relationship between sepal length and sepal width for the three species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.savefig("plots/exo4.png")


"""
5. Write a Python program to create a graph to find relationship between the petal length and width. 
"""


def relationship_pl_pw():
    plt.scatter(
        setosa_df["petal length (cm)"],
        setosa_df["petal width (cm)"],
        label="Iris setosa",
    )
    plt.scatter(
        versicolor_df["petal length (cm)"],
        versicolor_df["petal width (cm)"],
        label="Iris versicolor",
    )
    plt.scatter(
        virginica_df["petal length (cm)"],
        virginica_df["petal width (cm)"],
        label="Iris virginica",
    )
    plt.legend()
    plt.title("Relationship between petal length and petal width for the three species")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.savefig("plots/exo5.png")


"""
6. Write a Python program to create a graph to see how the length and width of SepalLength, SepalWidth, PetalLength, PetalWidth are distributed. 
"""


def subplot_length():
    graph_cols = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
    graph_titles = [
        "Sepal Length (cm)",
        "Sepal Width (cm)",
        "Petal Length (cm)",
        "Petal Width (cm)",
    ]

    _, axes = plt.subplots(2, 2, figsize=(10, 8))

    for i, ax in enumerate(axes.flat):
        ax.hist(iris[graph_cols[i]])
        ax.set_title(graph_titles[i])
        ax.set_ylabel("Count")
        ax.grid(linestyle="--")

    plt.savefig("plots/exo6.png")


"""
7. Write a Python program to create a joinplot to describe individual distributions on the same plot between Sepal length and Sepal width
"""


def jointplot_sepal():
    sns.jointplot(x=iris["sepal length (cm)"], y=iris["sepal width (cm)"])
    plt.savefig("plots/exo7.png")


"""
8. Write a Python program to create a joinplot using "hexbin" to describe individual distributions on the same plot between Sepal length and Sepal width. 
The bivariate analogue of a histogram is known as a "hexbin" plot, because it shows the counts of observations that fall within hexagonal bins. This plot works best with relatively large datasets.
"""


def joint_sepal_hex():
    sns.jointplot(
        x=iris["sepal length (cm)"], y=iris["sepal width (cm)"], kind="hex", color="red"
    )
    plt.savefig("plots/exo8.png")


"""
9. Write a Python program to create a joinplot using "kde" to describe individual distributions on the same plot between Sepal length and Sepal width.
The kernel density estimation (kde) procedure visualize a bivariate distribution. 
"""


def joint_sepal_kde():
    sns.jointplot(
        x=iris["sepal length (cm)"],
        y=iris["sepal width (cm)"],
        kind="kde",
        color="green",
    )
    plt.savefig("plots/exo9.png")


"""
10. Write a Python program to create a joinplot and add regression and kernel density fits using "reg" to describe individual distributions on the same plot between Sepal length and Sepal width. 
"""


def joint_sepal_reg():
    sns.jointplot(
        x=iris["sepal length (cm)"],
        y=iris["sepal width (cm)"],
        kind="reg",
    )
    plt.savefig("plots/exo10.png")


"""
11. Write a Python program to draw a scatterplot, then add a joint density estimate to describe individual distributions on the same plot between Sepal length and Sepal width. 
"""


def scatterplot_kde_sepal():
    sns.jointplot(
        x=iris["sepal length (cm)"],
        y=iris["sepal width (cm)"],
    ).plot_joint(sns.kdeplot, color="r", levels=6)
    plt.savefig("plots/exo11.png")


"""
12. Write a Python program to create a joinplot using "kde" to describe individual distributions on the same plot between Sepal length and Sepal width and use '+' sign as marker. 
"""


def joint_sepal_kde():
    sns.jointplot(
        x=iris["sepal length (cm)"], y=iris["sepal width (cm)"], marker="+"
    ).plot_joint(sns.kdeplot, color="purple", levels=6)
    plt.savefig("plots/exo12.png")


"""
13. Write a Python program to create a pairplot of the iris data set and check which flower species seems to be the most separable. 
"""


def pairplot_iris():
    sns.pairplot(iris)
    plt.savefig("plots/exo13.png")


"""
14. Write a Python program to find the correlation between variables of iris data. Also create a hitmap using Seaborn to present their relations.
"""


def plot_correlation():
    df = iris[
        [
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ]
    ]
    sns.heatmap(df.corr(), cmap="BrBG", annot=True)
    plt.xticks(rotation=10)
    plt.title("Correlation between measurable variables")
    plt.savefig("plots/exo14.png")


"""
15. Write a Python program to create a box plot (or box-and-whisker plot) which shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable of iris dataset.
"""


def boxplot_distribution():
    df = iris[
        [
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ]
    ]
    sns.boxplot(df)
    plt.title("Distribution of quantitative data")
    plt.xlabel("Quantitative data")
    plt.savefig("plots/exo15.png")


"""
16. Write a Python program to create a Principal component analysis (PCA) of iris dataset. 
"""


def get_pca_plot():
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
    Création des différents axes du graphiques en 3D
    """
    fig = plt.figure(1, figsize=(8, 6))
    plt.clf()
    ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
    ax.set_position([0, 0, 0.95, 1])

    """
    Mise en place de l'ACP    
    """
    plt.cla()
    pca = decomposition.PCA(n_components=3)
    pca.fit(X)
    X = pca.transform(X)

    """
    Mise en place du graphique de l'ACP
    """
    species_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
    y_numeric = [species_mapping[species] for species in y]

    for name, label in [("setosa", 0), ("versicolor", 1), ("virginica", 2)]:
        ax.text3D(
            X[y == label, 0].mean(),
            X[y == label, 1].mean() + 1.5,
            X[y == label, 2].mean(),
            name,
            horizontalalignment="center",
            bbox=dict(alpha=0.5, edgecolor="w", facecolor="w"),
        )

    ax.scatter(
        X[:, 0],
        X[:, 1],
        X[:, 2],
        c=y_numeric,
        edgecolors="k",
        cmap=plt.cm.nipy_spectral,
    )

    ax.set_xlabel("Principal component 1")
    ax.set_ylabel("Principal component 2")
    ax.set_zlabel("Principal component 3")

    plt.savefig("plots/exo16.png")

get_pca_plot()