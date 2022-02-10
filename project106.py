import csv
import plotly.express as pe

import numpy as np

def plotGraph(path):
    with open(path) as f:
        d = csv.DictReader(f)

        graph = pe.scatter(d , x = "Percentage" , y = "Days Present" , title= "Temperature VS Ice-cream")
        graph.show()


def getDataSource(path):
    Percentage = []
    DaysPresent = []

    with open(path) as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            Percentage.append(float(row["Percentage"]))
            DaysPresent.append(float(row["Days Present"]))

    return {"x" : Percentage , "y" : DaysPresent}




def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"] , dataSource["y"])
    print("Correlation between Days Present & Percentage sales is -> " , corelation[0,1])



def setup():

    path = "project106.csv"
    dataSource = getDataSource(path)
    findCorelation(dataSource)
    plotGraph(path)


setup()

