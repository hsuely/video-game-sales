import pullData
from pullData import videoGames
import matplotlib.pyplot as plt

globalSales = []
xmin = 0
xmax = 0

for videogame in videoGames:
    globalSales.append(videogame.global_sales)
    if videogame.global_sales < xmin:
        xmin = videogame.global_sales
    elif videogame.global_sales > xmax:
        xmax = videogame.global_sales

plt.boxplot(globalSales, vert = False)
plt.title("Video Game Global Sales")
plt.xlabel("Sales")

plt.show()
