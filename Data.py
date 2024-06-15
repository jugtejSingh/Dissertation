import pandas as pd
import matplotlib.pyplot as plt

eastBound = pd.read_csv("files/averages/eastAverage.csv")
northBound = pd.read_csv("files/averages/northAverage.csv")
southBound = pd.read_csv("files/averages/southAverage.csv")
westBound = pd.read_csv("files/averages/westAverage.csv")

print(max(eastBound["VehCount"]))
print(max(southBound["VehCount"]))
print(max(northBound["VehCount"]))
print(max(westBound["VehCount"]))

print(min(eastBound["VehCount"]))
print(min(southBound["VehCount"]))
print(min(northBound["VehCount"]))
print(min(westBound["VehCount"]))


print(sum(eastBound["VehCount"])/eastBound["VehCount"].count())
print(sum(southBound["VehCount"])/southBound["VehCount"].count())
print(sum(northBound["VehCount"])/northBound["VehCount"].count())
print(sum(westBound["VehCount"])/westBound["VehCount"].count())

def plotting(direction, directionForChart):
    timeVehicle = direction.loc[:, "Hour&Minute"]
    vehCount = direction.loc[:, "VehCount"]

    timeVehicle = timeVehicle.values.tolist()
    print(timeVehicle)
    vehCount = vehCount.values.tolist()
    print(vehCount)

    plt.figure(figsize=(30, 8))
    plt.scatter(timeVehicle, vehCount)
    plt.xlabel("Time")
    plt.ylabel("Volume Of Vehicles")
    plt.title(f"{directionForChart} Charts")
    # plt.show()
    return timeVehicle, vehCount


easttime, eastCount = plotting(eastBound, "EastBound")
westTime, westCount = plotting(westBound, "WestBound")
southTime, southCount = plotting(southBound, "SouthBound")
northTime, northCount = plotting(northBound, "NorthBound")
