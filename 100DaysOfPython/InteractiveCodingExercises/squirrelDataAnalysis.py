import pandas as pd

squirrel_data = pd.read_csv("2018_Central_park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray","Cinnamon","Black"]
color_dict = {"Fur Color": [],
              "Count": []}

for color in colors:
    squirrel_color_len = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
    
    color_dict["Fur Color"].append(color)
    color_dict["Count"].append(squirrel_color_len)

color_df = pd.DataFrame(color_dict)
#color_df.to_csv("Squirrel_Color_amounts")
print(color_df)