import pandas as pd


df = pd.read_csv("data/Automobile_data.csv", na_values="-")
print(df.info())

"""
Exercise 1: From the given dataset print the first and last five rows
"""
print(df.head())
print(df.tail())
print("----------------------------------")


"""
Exercise 2: Clean the dataset and update the CSV file
"""

"""
Exercise 3: Find the most expensive car company name
"""
print(df[["company", "price"]][df.price == df["price"].max()])
print("----------------------------------")


"""
Exercise 4: Print All Toyota Cars details
"""
all_cars = df.groupby("company")
print(all_cars.get_group("toyota"))
print("----------------------------------")


"""
Exercise 5: Count total cars per company
"""
print(df["company"].value_counts())
print("----------------------------------")


"""
Exercise 6: Find each company’s Higesht price car
"""
all_company_cars = df.groupby("company")
print(all_company_cars[["company", "price"]].max())
print("----------------------------------")


"""
Exercise 7: Find the average mileage of each car making company
"""
all_company_cars = df.groupby("company")
print(all_company_cars[["average-mileage"]].mean())
print("----------------------------------")


"""
Exercise 8: Sort all cars by Price column
"""
print(df.sort_values(by=["price"]))
print("----------------------------------")


"""
Exercise 9: Concatenate two data frames using the following conditions
"""
GermanCars = {
    "Company": ["Ford", "Mercedes", "BMV", "Audi"],
    "Price": [23845, 171995, 135925, 71400],
}
japaneseCars = {
    "Company": ["Toyota", "Honda", "Nissan", "Mitsubishi "],
    "Price": [29995, 23600, 61500, 58900],
}

df_japaneseCars = pd.DataFrame.from_dict(japaneseCars)
df_germanCars = pd.DataFrame.from_dict(GermanCars)
new_df = pd.concat([df_germanCars, df_japaneseCars], keys=["German", "Japanese"])
new_df.to_csv("data/new_df.csv")


"""
Exercise 10: Merge two data frames using the following condition
Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
"""
Car_Price = {
    "Company": ["Toyota", "Honda", "BMV", "Audi"],
    "Price": [23845, 17995, 135925, 71400],
}
car_Horsepower = {
    "Company": ["Toyota", "Honda", "BMV", "Audi"],
    "horsepower": [141, 80, 182, 160],
}

df_price = pd.DataFrame.from_dict(Car_Price)
df_horsepower = pd.DataFrame.from_dict(car_Horsepower)
new_df = pd.merge(df_price, df_horsepower, on="Company")
new_df.to_csv("data/new_merged_df.csv")