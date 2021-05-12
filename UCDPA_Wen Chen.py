import numpy as np
import pandas as pd

WHR_2015=pd.read_csv("2015.csv")
WHR_2016=pd.read_csv("2016.csv")
WHR_2017=pd.read_csv("2017.csv")
WHR_2018=pd.read_csv("2018.csv")
WHR_2019=pd.read_csv("2019.csv")

#print(WHR_2015.info())
#print(WHR_2016.info())
#print(WHR_2017.info())
#print(WHR_2018.info())
#print(WHR_2019.info())

WHR_2018['Perceptions of corruption'] = WHR_2018['Perceptions of corruption'].fillna(0)
print(WHR_2018.info())

WHR_2015['Year'] = "2015"
WHR_2016['Year'] = "2016"
WHR_2017['Year'] = "2017"
WHR_2018['Year'] = "2018"
WHR_2019['Year'] = "2019"

