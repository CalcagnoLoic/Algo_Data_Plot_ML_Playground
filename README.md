# Python Algo_Data_Plot_ML_Playground

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,vscode" />
  </a>
</p>

A multitude of exercises related to different aspects of Python. The purpose of these exercises is to test my current skills as well as to learn new techniques/methods. These exercises come from [pynative](https://pynative.com/) and [w3ressource](https://www.w3resource.com/machine-learning/scikit-learn/iris/index.php).

Among these exercises, the following themes have been tackled:
- Algorithms on native language elements and storage objects. Aspects such as writing to files and object-oriented were also covered.
- Data manipulation via the well-known [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html) packages.
- Data visualization via the [MatplotLib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/index.html) packages.
- Putting machine learning into practice with the famous `iris` dataset. The various classical aspects of analysis were covered: data exploration, data visualization, principal component analysis and training of two simple models: k-NN and logistic regression.

<details><summary><h2>Content of the folder exercises</h2></summary>

- [ ] `Basic's topic` : Variables, Operators, Loops, String, Numbers, List
- [ ] `Input/Output's topic` : `print()` and `input()`, File I/O
- [ ] `Loop's topic` : If-else statements, loop, and while loop.
- [ ] `Function's topic`: Functions arguments, built-in functions.
- [ ] `String's topic`: String operations and manipulations.
- [ ] `Data structure's topic`: List, Set, Dictionary, and Tuple operations
- [ ] `List's topic`: List operations and manipulations, list functions, list slicing and list comprehension
- [ ] `Dictionary's topic`: Dictionary operations and manipulations, dictionary functions and dictionary comprehension
- [ ] `Tuple's topic`: Tuple creation, operations, unpacking of a tuple
- [ ] `Set's topic`: Set operations, manipulations, and set functions
- [ ] `OOP's topic`: Object, Classes, Inheritance
- [ ] `Date and Time's topic`: Date, time, DateTime, Calendar.
- [ ] `JSON's topic`: JSON creation, manipulation, Encoding, Decoding, and parsing
- [ ] `Numpy's topic`: Array manipulations, numeric ranges, Slicing, indexing, Searching, Sorting, and splitting
- [ ] `Pandas' topic`:  Data-frame, Data selection, group-by, Series, sorting, searching, and statistics
- [ ] `Matplotlib's topic`: Line plot, Style properties, multi-line plot, scatter plot, bar chart, histogram, Pie chart, Subplot, stack plot
- [ ] `Random data generation's topic`: random module, secrets module, UUID module

</details>

<details><summary><h2>Content of the folder machine_learning</h2></summary>

- [ ] `Exploration's topic` : Data manipulation to understand the dataset
- [ ] `Visualization's topic` : Data manipulation to generate trend graphs and a PCA
- [ ] `kNN's topic` : Various manipulations of test and training datasets to work with the kNN model
- [ ] `Logistic regression's topic`: Data manipulation for logistic regression

</details>

## Launch virtual env and packages

From the root of the project : 

```cmd
$ python -m venv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
```

Don't forget to select the good interpreter inside VSCode

## Launch all the tests

From the root of the project : 

```cmd
$ python -m unittest discover
```
