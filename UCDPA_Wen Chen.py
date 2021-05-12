import numpy as np
import pandas as pd

WHR_2015 = pd.read_csv("2015.csv")
WHR_2016 = pd.read_csv("2016.csv")
WHR_2017 = pd.read_csv("2017.csv")
WHR_2018 = pd.read_csv("2018.csv")
WHR_2019 = pd.read_csv("2019.csv")

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

WHR_2015_new = WHR_2015.filter(['Happiness Rank', 'Country', 'Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year'])
WHR_2016_new = WHR_2016.filter(['Happiness Rank', 'Country', 'Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year'])


WHR_2017.rename(columns = {'Happiness.Rank':'Happiness Rank',
                          'Happiness.Score':'Happiness Score',
                          'Economy..GDP.per.Capita.' : 'Economy (GDP per Capita)',
                          'Health..Life.Expectancy.' : 'Health (Life Expectancy)',
                          'Trust..Government.Corruption.' : 'Trust (Government Corruption)',
                           }, inplace = True)
WHR_2017_new = WHR_2017.filter(['Happiness Rank', 'Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year'])

WHR_2018.rename(columns = {'Overall rank' : 'Happiness Rank',
                          'Country or region' : 'Country',
                          'Score' : 'Happiness Score',
                          'Social support' : 'Family',
                          'GDP per capita' : 'Economy (GDP per Capita)',
                          'Healthy life expectancy' : 'Health (Life Expectancy)',
                          'Freedom to make life choices' :'Freedom',
                          'Perceptions of corruption' : 'Trust (Government Corruption)'
                          }, inplace = True)
WHR_2018_new = WHR_2018.filter(['Happiness Rank', 'Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year'])

WHR_2019.rename(columns = {'Overall rank' : 'Happiness Rank',
                          'Country or region' : 'Country',
                          'Score' : 'Happiness Score',
                          'Social support' : 'Family',
                          'GDP per capita' : 'Economy (GDP per Capita)',
                          'Healthy life expectancy' : 'Health (Life Expectancy)',
                          'Freedom to make life choices' :'Freedom',
                          'Perceptions of corruption' : 'Trust (Government Corruption)'
                          }, inplace = True)
WHR_2019_new = WHR_2019.filter(['Happiness Rank', 'Country','Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year'])

Ref_data = WHR_2016.filter(['Country', 'Region'])
print(Ref_data.info())

WHR_2017_new = WHR_2017_new.merge(Ref_data, left_on = 'Country', right_on = 'Country', how = 'inner')
WHR_2018_new = WHR_2018_new.merge(Ref_data, left_on = 'Country', right_on = 'Country', how = 'inner')
WHR_2019_new = WHR_2019_new.merge(Ref_data, left_on = 'Country', right_on = 'Country', how = 'inner')

list=['Happiness Rank', 'Country', 'Region', 'Economy (GDP per Capita)','Family',
                        'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity',
                        'Happiness Score' , 'Year']

WHR_2017_new=WHR_2017_new.filter(list)
WHR_2018_new=WHR_2018_new.filter(list)
WHR_2019_new=WHR_2019_new.filter(list)

for n in [WHR_2015_new, WHR_2016_new, WHR_2017_new, WHR_2018_new, WHR_2019_new]:
    print(n.head())

