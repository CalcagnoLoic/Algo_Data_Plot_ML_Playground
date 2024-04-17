from sklearn import datasets
from scipy import sparse
import pandas as pd
import numpy as np

"""
1. Write a Python program to load the iris data from a given csv file into a dataframe and print the shape of the data, type of the data and first 3 rows. 
"""
iris = datasets.load_iris()
df = pd.DataFrame(data=iris["data"], columns=iris["feature_names"])
df["species"] = iris["target"]
df["species"] = df["species"].map(dict(enumerate(iris["target_names"])))
df["id"] = df.reset_index().index


def get_info_iris():
    print("1> Shape of dataset: ", df.shape)
    print("2> Type of data: ", type(df))
    print("3> First 3 rows: ", df.head(3))
    print("----------------------------------")


"""
2. Write a Python program using Scikit-learn to print the keys, number of rows-columns, feature names and the description of the Iris data. 
"""


def get_info_iris_sklearn():
    print("1> Key from dataset: ", df.keys())
    print("2> Shape of dataset: ", df.shape)
    print("----------------------------------")


"""
3. Write a Python program to get the number of observations, missing values and nan values. 
"""


def get_observations():
    print("1> Number of observations: ", len(df.index))
    print("2> Number of missing values: ", df.isnull().values.sum())
    print("3> Number of nan values: ", df.isna().values.sum())
    print("----------------------------------")


"""
4. Write a Python program to create a 2-D array with ones on the diagonal and zeros elsewhere. Now convert the NumPy array to a SciPy sparse matrix in CSR format. 
"""


def get_array_matrix_CSR():
    print("1> 2D array: ", "\n", np.eye(4))
    print("2> matrix CSR: ", "\n", sparse.csr_matrix(np.eye(4)))
    print("----------------------------------")


"""
5. Write a Python program to view basic statistical details like percentile, mean, std etc. of iris data. 
"""


def get_statistical():
    print("1> Statistics of dataset: ", "\n", df.describe())
    print("----------------------------------")


"""
6. Write a Python program to get observations of each species (setosa, versicolor, virginica) from iris data. 
"""


def get_observation_by_species():
    print("1> Observation by species: ", df["species"].value_counts())
    print("----------------------------------")


"""
7. Write a Python program to drop Id column from a given Dataframe and print the modified part. Call iris.csv to create the Dataframe. 
"""


def cleanup_dataset():
    df_clean = df.drop("id", axis=1)
    df_clean.to_csv("data/iris.csv")


"""
8. Write a Python program to access first four cells from a given Dataframe using the index and column labels. Call iris.csv to create the Dataframe. 
"""


def get_first_cells():
    df_data = pd.read_csv("data/iris.csv")
    print("1> First data: ", df_data.iloc[:, [1, 2, 3, 4]].values)


if __name__ == "__main__":

    def main():
        get_info_iris()
        get_info_iris_sklearn()
        get_observations()
        get_array_matrix_CSR()
        get_statistical()
        get_observation_by_species()
        cleanup_dataset()
        get_first_cells()

    main()
