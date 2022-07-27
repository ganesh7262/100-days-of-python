import pandas as pd

data=pd.read_csv("weather_data.csv")
print(data["day"])


print(data.describe())