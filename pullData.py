import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\conta\Documents\video-game-sales\vgsales.csv')

#print(df)

class VideoGame:
    def __init__(self, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_sales = na_sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales

videoGames = []
for count in range(df.shape[0]):
    videoGames.append(VideoGame(df.iloc[count,1],df.iloc[count,2],df.iloc[count,3],df.iloc[count,4],df.iloc[count,5],df.iloc[count,6],df.iloc[count,7],df.iloc[count,8],df.iloc[count,9],df.iloc[count,10]))

print(videoGames[1].name)
