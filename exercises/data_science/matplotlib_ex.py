import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/company_sales_data.csv")


"""
Exercise 1: Read Total profit of all months and show it using a line plot
    X label name = Month Number
    Y label name = Total profit
"""

x = df["month_number"]
y = df["total_profit"]

plt.plot(x, y)
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company profit per month")
plt.savefig("plots/exo1.png")

"""
Exercise 2: Get total profit of all months and show line plot 
Generated line plot must include following Style properties: 
    Line Style dotted and Line-color should be red
    Show legend at the lower right location.
    X label name = Month Number
    Y label name = Sold units number
    Add a circle marker.
    Line marker color as read
    Line width should be 3
"""
x = df["month_number"]
y = df["total_profit"]

plt.plot(
    x, y, "--or", markerfacecolor="k", linewidth=3, label="Profit data of last year"
)
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.title("Company Sales data of past year")
plt.legend(loc="lower right")
plt.savefig("plots/exo2.png")

"""
Exercise 3: Read all product sales data and show it  using a multiline plot

Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).
"""
x = df["month_number"]

plt.plot(x, df["facecream"], linewidth=3, marker="o", label="Facecream Sales Data")
plt.plot(
    x,
    df["facewash"],
    linewidth=3,
    marker="o",
    color="tab:orange",
    label="Facewash Sales Data",
)
plt.plot(
    x,
    df["toothpaste"],
    linewidth=3,
    marker="o",
    color="g",
    label="Toothpaste Sales Data",
)
plt.plot(
    x,
    df["bathingsoap"],
    linewidth=3,
    marker="o",
    color="r",
    label="Bathingsoap Sales Data",
)
plt.plot(
    x,
    df["shampoo"],
    linewidth=3,
    marker="o",
    color="tab:purple",
    label="Shampoo Sales Data",
)
plt.plot(
    x,
    df["moisturizer"],
    linewidth=3,
    marker="o",
    color="tab:brown",
    label="Moisturizer Sales Data",
)
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Sales data")
plt.legend(loc="upper left")
plt.savefig("plots/exo3.png")

"""
Exercise 4: Read toothpaste sales data of each month and show it using a scatter plot

Also, add a grid in the plot. gridline style should “–“.
"""
x = df["month_number"]
y = df["toothpaste"]

plt.scatter(x, y, label="Toothpaste sales data")
plt.ylabel("Number of units sold")
plt.xlabel("Month number")
plt.title("Toothpaste sales data")
plt.grid(linestyle="--")
plt.legend()
plt.savefig("plots/exo4.png")

"""
Exercise 5: Read face cream and facewash product sales data and show it using the bar chart

The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
"""
x = df["month_number"]

plt.bar(x, df["facecream"], width=0.3, label="Facecream Sales data")
plt.bar(
    x + 0.3, df["facewash"], color="tab:orange", width=0.3, label="Facewash Sales data"
)
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Facecream and facewash sales data")
plt.legend(loc="upper left")
plt.grid(linestyle="--")
plt.savefig("plots/exo5.png")


"""
Exercise 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
"""
x = df["month_number"]
y = df["bathingsoap"]

plt.bar(x, y)
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("Bathing soap sales data")
plt.grid(linestyle="--")
plt.savefig("plots/exo6.png")


"""
Exercise 7: Read the total profit of each month and show it using the histogram to see the most common profit ranges
"""

plt.hist(df["total_profit"], label="Profit data")
plt.xlabel("Profit range in dollar $")
plt.ylabel("Actual profil in dollar $")
plt.title("Profit data")
plt.legend()
plt.savefig("plots/exo7.png")


"""
Exercise 8: Calculate total sale data for last year for each product and show it using a Pie chart

Note: In Pie chart display Number of units sold per year for each product in percentage.
"""

my_data = np.array(
    [
        df["facecream"].sum(),
        df["facewash"].sum(),
        df["toothpaste"].sum(),
        df["bathingsoap"].sum(),
        df["shampoo"].sum(),
        df["moisturizer"].sum(),
    ]
)
my_labels = [
    "facecream",
    "facewash",
    "toothpaste",
    "bathingsoap",
    "shampoo",
    "moisturizer",
]

plt.axis("equal")
plt.pie(my_data, labels=my_labels, autopct="%1.1f%%", shadow=True)
plt.title("Sales data")
plt.legend(loc="upper left")
plt.savefig("plots/exo8.png")

"""
Exercise 9: Read Bathing soap facewash of all months and display it using the Subplot
"""
x = df["month_number"]
y1 = df["bathingsoap"]
y2 = df["facewash"]

plt.subplot(2, 1, 1)
plt.plot(x, y1, color="black", marker="o", linewidth=3)
plt.ylabel("Sales Units")
plt.title("Sales data of bathing soap")

plt.subplot(2, 1, 2)
plt.plot(x, y2, color="red", marker="o", linewidth=3)
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.title("Sales data of facewash")

plt.savefig("plots/exo9.png")


"""
Exercise Question 10: Read all product sales data and show it using the stack plot
"""

x = df["month_number"]
my_data = np.array(
    [
        df["facecream"],
        df["facewash"],
        df["toothpaste"],
        df["bathingsoap"],
        df["shampoo"],
        df["moisturizer"],
    ]
)
my_labels = [
    "facecream",
    "facewash",
    "toothpaste",
    "bathingsoap",
    "shampoo",
    "moisturizer",
]

plt.stackplot(x, my_data, labels=my_labels)
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.title("All product sales data")
plt.legend(loc="upper left")
plt.savefig("plots/exo10.png")
