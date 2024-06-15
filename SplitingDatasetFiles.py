import pandas as pd
from datetime import datetime


def SplitingMainDataFile():
    csvfile = pd.read_csv("files/Automated_Traffic_Volume_Counts.csv", header=11, )

    csvfile = csvfile.sort_values(by=['street'])

    for i in range(26):
        if i == 0:
            x = csvfile.iloc[0:1000000, :]
        else:
            x = csvfile.iloc[i * 1000000: ((i + 1) * 1000000), :]
        x.to_csv(f"files/file{i}.csv")


def SeperatingFiles():
    dataframe = pd.read_csv("files/KellyTravis.csv", sep=",")

    dataframe = dataframe.sort_values(by="Street")
    east = dataframe.iloc[0:766, :]
    north = dataframe.iloc[767:1531, :]
    south = dataframe.iloc[1532:2279, :]
    west = dataframe.iloc[2280:, :]

    east.to_csv("files/east")
    west.to_csv("files/west")
    north.to_csv("files/north")
    south.to_csv("files/south")


def SortingByData():
    east = pd.read_csv("files/east")
    west = pd.read_csv("files/west")
    south = pd.read_csv("files/south")
    north = pd.read_csv("files/north")

    eastDict = {}
    westDict = {}
    northDict = {}
    southDict = {}

    eastDictAveraging = {}
    westDictAveraging = {}
    northDictAveraging = {}
    southDictAveraging = {}
    # Loops around the hour

    # Loops around the hours
    for i in range(len(east.index)):
        vehCount = east.loc[i, "VehCount"]
        time = east.loc[i, "Hour"].astype(str) + ":" + east.loc[i, "Minute"].astype(str)
        if time in eastDict.keys():
            eastDict[time].append(vehCount)
        else:
            eastDict[time] = [vehCount]

    for i in range(len(west.index)):
        vehCount = west.loc[i, "VehCount"]
        time = west.loc[i, "Hour"].astype(str) + ":" + west.loc[i, "Minute"].astype(str)
        if time in westDict.keys():
            westDict[time].append(vehCount)
        else:
            westDict[time] = [vehCount]

    for i in range(len(south.index)):
        vehCount = south.loc[i, "VehCount"]
        time = south.loc[i, "Hour"].astype(str) + ":" + south.loc[i, "Minute"].astype(str)
        if time in southDict.keys():
            southDict[time].append(vehCount)
        else:
            southDict[time] = [vehCount]

    for i in range(len(north.index)):
        vehCount = north.loc[i, "VehCount"]
        time = north.loc[i, "Hour"].astype(str) + ":" + north.loc[i, "Minute"].astype(str)
        if time in northDict.keys():
            northDict[time].append(vehCount)
        else:
            northDict[time] = [vehCount]

    for x in eastDict.keys():
        sum = 0
        count = 0
        for vehCountForAveraging in eastDict[x]:
            sum = sum + vehCountForAveraging
            count = count + 1
        eastDictAveraging[x] = sum / count
        print(eastDictAveraging)

    for x in southDict.keys():
        sum = 0
        count = 0
        for vehCountForAveraging in southDict[x]:
            sum = sum + vehCountForAveraging
            count = count + 1
        southDictAveraging[x] = sum / count
        print(southDictAveraging)

    for x in northDict.keys():
        sum = 0
        count = 0
        for vehCountForAveraging in northDict[x]:
            sum = sum + vehCountForAveraging
            count = count + 1
        northDictAveraging[x] = sum / count
        print(northDictAveraging)

    for x in westDict.keys():
        sum = 0
        count = 0
        for vehCountForAveraging in westDict[x]:
            sum = sum + vehCountForAveraging
            count = count + 1
        westDictAveraging[x] = sum / count
        print(westDictAveraging)

    dataEast = {"Hour&Minute": eastDictAveraging.keys(), "VehCount": eastDictAveraging.values()}
    eastDataset = pd.DataFrame(dataEast)
    eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    dataWest = {"Hour&Minute": westDictAveraging.keys(), "VehCount": westDictAveraging.values()}
    westDataset = pd.DataFrame(dataWest)
    westDataset["Hour&Minute"] = westDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    westDataset["Hour&Minute"] = westDataset["Hour&Minute"] = westDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    dataSouth = {"Hour&Minute": southDictAveraging.keys(), "VehCount": southDictAveraging.values()}
    southDataset = pd.DataFrame(dataSouth)
    southDataset["Hour&Minute"] = southDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    southDataset["Hour&Minute"] = southDataset["Hour&Minute"] = southDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    dataNorth = {"Hour&Minute": northDictAveraging.keys(), "VehCount": northDictAveraging.values()}
    northDataset = pd.DataFrame(dataNorth)
    northDataset["Hour&Minute"] = northDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    northDataset["Hour&Minute"] = northDataset["Hour&Minute"] = northDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    eastDataset = eastDataset.sort_values(by="Hour&Minute")
    westDataset = westDataset.sort_values(by="Hour&Minute")
    southDataset = southDataset.sort_values(by="Hour&Minute")
    northDataset = northDataset.sort_values(by="Hour&Minute")
    eastDataset.to_csv("files/averages/eastAverage.csv")
    westDataset.to_csv("files/averages/westAverage.csv")
    southDataset.to_csv("files/averages/southAverage.csv")
    northDataset.to_csv("files/averages/northAverage.csv")


def DaySplit(day):
    east = pd.read_csv("files/east")
    west = pd.read_csv("files/west")
    south = pd.read_csv("files/south")
    north = pd.read_csv("files/north")

    eastDataset = east.query(f"Day == {day}").reset_index(drop=True)
    westDataset = west.query(f"Day == {day}").reset_index(drop=True)
    southDataset = south.query(f"Day == {day}").reset_index(drop=True)
    northDataset = north.query(f"Day == {day}").reset_index(drop=True)
    eastDataset = eastDataset.drop(["Unnamed: 0"], axis=1)

    print(eastDataset.head(5))
    eastDict = {}
    westDict = {}
    southDict = {}
    northDict = {}

    for i in range(len(eastDataset.index)):
        vehCount = eastDataset.loc[i, "VehCount"]
        time = eastDataset.loc[i, "Hour"].astype(str) + ":" + eastDataset.loc[i, "Minute"].astype(str)
        eastDict[time] = vehCount
    for i in range(len(westDataset.index)):
        vehCount = westDataset.loc[i, "VehCount"]
        time = westDataset.loc[i, "Hour"].astype(str) + ":" + westDataset.loc[i, "Minute"].astype(str)
        westDict[time] = vehCount
    for i in range(len(southDataset.index)):
        vehCount = southDataset.loc[i, "VehCount"]
        time = southDataset.loc[i, "Hour"].astype(str) + ":" + southDataset.loc[i, "Minute"].astype(str)
        southDict[time] = vehCount
    for i in range(len(northDataset.index)):
        vehCount = northDataset.loc[i, "VehCount"]
        time = northDataset.loc[i, "Hour"].astype(str) + ":" + northDataset.loc[i, "Minute"].astype(str)
        northDict[time] = vehCount

    eastDataset = pd.DataFrame({"Hour&Minute": eastDict.keys(), "VehCount": eastDict.values()})
    eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"] = eastDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    westDataset = pd.DataFrame({"Hour&Minute": eastDict.keys(), "VehCount": eastDict.values()})
    westDataset["Hour&Minute"] = westDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    westDataset["Hour&Minute"] = westDataset["Hour&Minute"] = westDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))
    southDataset = pd.DataFrame({"Hour&Minute": eastDict.keys(), "VehCount": eastDict.values()})
    southDataset["Hour&Minute"] = southDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    southDataset["Hour&Minute"] = southDataset["Hour&Minute"] = southDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))
    northDataset = pd.DataFrame({"Hour&Minute": eastDict.keys(), "VehCount": eastDict.values()})
    northDataset["Hour&Minute"] = northDataset["Hour&Minute"].apply(lambda x: datetime.strptime(x, "%H:%M"))
    northDataset["Hour&Minute"] = northDataset["Hour&Minute"] = northDataset["Hour&Minute"].apply(
        lambda x: datetime.strftime(x, "%H:%M"))

    eastDataset = eastDataset.sort_values(by="Hour&Minute")
    westDataset = westDataset.sort_values(by="Hour&Minute")
    southDataset = southDataset.sort_values(by="Hour&Minute")
    northDataset = northDataset.sort_values(by="Hour&Minute")

    eastDataset.to_csv(f"files/days/eastDay{day}.csv")
    westDataset.to_csv(f"files/days/westDay{day}.csv")
    northDataset.to_csv(f"files/days/northDay{day}.csv")
    southDataset.to_csv(f"files/days/southDay{day}.csv")


DaySplit(4)
