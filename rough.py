import matplotlib as plt
import pandas as pd

data=pd.read_csv("weather_data.csv")

print(data.temp.describe())
print(data["temp"])
print(data["temp"].mean())
print(data[data["day"]=="Monday"])
print(data[data["temp"]==data["temp"].max()])

