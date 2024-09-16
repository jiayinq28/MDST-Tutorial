# %% [markdown]
# # Checkpoint 0


# %% [markdown]
# These exercises are a mix of Python and Pandas practice. Most should be no more than a few lines of code!


# %%
# here is a Python list:


a = [1, 2, 3, 4, 5, 6]




# %%
# get a list containing the last 3 elements of a
# Yes, you can just type out [4, 5, 6] but we really want to see you demonstrate you know how to use list slicing in Python
a = [1, 2, 3, 4, 5, 6]
a[3:]


# %%
# create a list of numbers from 1 to 20
a = list(range (1,21))
print (a)


# %%
# now get a list with only the even numbers between 1 and 100
# you may or may not make use of the list you made in the last cell
a = list(range(2,100,2))
print (a)


# %%
# write a function that takes two numbers as arguments
# and returns the first number divided by the second
def num(a,b):
    div = a/b
    return (div)
num(6, 3)


# %%
# fizzbuzz
# you will need to use both iteration and control flow
# go through all numbers from 1 to 30 in order
# if the number is a multiple of 3, print fizz
# if the number is a multiple of 5, print buzz
# if the number is a multiple of 3 and 5, print fizzbuzz and NOTHING ELSE
# if the number is neither a multiple of 3 nor a multiple of 5, print the number
for i in list(range(1,31)):
    if (i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")
    elif (i % 5 == 0):
        print("buzz")
    elif (i % 3 == 0):
        print("fizz")
    else:
        print(i)


# %%
# create a dictionary that reflects the following menu pricing (taken from Ahmo's)
# Gyro: $9
# Burger: $9
# Greek Salad: $8
# Philly Steak: $10


ahmo = { "Gyro": 9, "Burger": 9, "Greek Salad": 8, "Philly Steak": 10}
print (ahmo)


# %%
# load in the "starbucks.csv" dataset
# refer to how we read the cereal.csv dataset in the tutorial
import pandas as pd
df = pd.read_csv("../data/starbucks.csv")
print(df)


# %%
# select all rows with more than and including 400 calories
df[df["calories"]>400]


# %%
# select all rows whose vitamin c content is higher than the iron content
df[df ["vitamin c"]>df["iron"]]


# %%
# create a new column containing the caffeine per calories of each drink
df["caffeine_per_calories"] = df["caffeine"] / df["calories"]
df


# %%
# what is the average calorie across all items?
df["calories"].mean()


# %%
# how many different categories of beverages are there?
print(df["beverage_category"].nunique())


# %%
# what is the average # calories for each beverage category?
#print(df["beverage_category"].unique())
#df["avg_calories"] = df["caffeine"] / df["calories"]
mfrs = df.groupby("beverage_category")
mfrs["calories"].mean()
