import csv
import plotly.express as px
import numpy as np

def getDataSource(dataPath):
    marks=[]
    attendance=[]

    with open(dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        
        for row in csv_reader:
          marks.append(float(row["Marks In Percentage"]))
          attendance.append(float(row["Days Present"]))

    return {"x":marks,"y":attendance}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation b/w Marks In Percentage v/s Days Present",correlation[0,1])

def setup():
    dataPath="marks.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)  

setup()              