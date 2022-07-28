from operator import le
import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

fur=data["Primary Fur Color"].unique()[1:]



cinnamon_fur_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
gray_fur=len(data[data["Primary Fur Color"]=="Gray"])
black_fur=len(data[data["Primary Fur Color"]=="Black"])




fur_color_data={
    "color":["Grey","Cinnamon","Black"],
    "count":[gray_fur,cinnamon_fur_count,black_fur]
}

df_fur_data=pd.DataFrame(fur_color_data)
df_fur_data.to_csv("squirell_count.csv")