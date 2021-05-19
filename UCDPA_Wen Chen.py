import pandas as pd
import numpy as np

WHR_2015 = pd.read_csv("2015.csv")
WHR_2016 = pd.read_csv("2016.csv")
WHR_2017 = pd.read_csv("2017.csv")
WHR_2018 = pd.read_csv("2018.csv")
WHR_2019 = pd.read_csv("2019.csv")

for n in [WHR_2015, WHR_2016, WHR_2017, WHR_2018, WHR_2019]:
    print(n.info())


WHR_2018['Perceptions of corruption'] = WHR_2018['Perceptions of corruption'].fillna(0)
print(WHR_2018.info())

WHR_2015['Year'] = 2015
WHR_2016['Year'] = 2016
WHR_2017['Year'] = 2017
WHR_2018['Year'] = 2018
WHR_2019['Year'] = 2019

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
    print(n.info())

#Now the above data has the same columns needed for analysis so can cantenate them now.

WHR_Final = pd.concat([WHR_2015_new, WHR_2016_new, WHR_2017_new, WHR_2018_new, WHR_2019_new], axis =0)
print(WHR_Final.info())

#Now we have a data set containing 5 year world happiness data of each country and each region and for each year.

import matplotlib.pyplot as plt
import seaborn as sns

Region_list={'Western Europe': 'WE', 'North America': 'NA', 'Australia and New Zealand': 'ANZ', 'Middle East and Northern Africa': 'MENA',
             'Latin America and Caribbean':'LAC', 'Southeastern Asia':'SEA', 'Central and Eastern Europe':'CEE',
             'Eastern Asia':'EA', 'Sub-Saharan Africa':'SSA', 'Southern Asia': 'SA'}

WHR_Final['Region'].replace(Region_list, inplace=True)

_ = sns.stripplot(x='Region', y='Happiness Score', data=WHR_Final)
_ = plt.xlabel('Region')
_ = plt.ylabel('Happiness Score')
plt.show()


plt.figure(figsize=(10,10))
corr_mat = sns.heatmap(WHR_Final.corr(), vmin=-1, vmax=1, annot=True)
corr_mat.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12)
plt.show()

#To perform machine learning on factors determing the happiness score, keep only the feature with a type "float"

WHR_2 = WHR_Final.select_dtypes(["float64"])
print(WHR_2.info())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.linear_model import Lasso
X = WHR_2.drop("Happiness Score", axis=1)
y = WHR_2["Happiness Score"]
names = X.columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X,y).coef_
_ = plt.plot(range(len(names)), lasso_coef)
_ = plt.xticks(range(len(names)), names, rotation=60)
_ = plt.ylabel('Coefficients')
plt.show()

X = WHR_2[["Economy (GDP per Capita)"]]
y = WHR_2[['Happiness Score']]
reg = LinearRegression()
model = reg.fit(X,y)
print("intercept: ", model.intercept_)
print("coef: ", model.coef_)
print("rcore. ", model.score(X,y))
gdp_list = [[0.25],[0.50],[0.75],[1.00],[1.25],[1.50]]
model.predict(gdp_list)
for g in gdp_list:
    print("The happiness value of the country with a gdp value of ",g,": ",model.predict([g]))
reg = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(reg.score(X_test, y_test))
rmse_test = np.sqrt(MSE(y_test, y_pred))
print('Test set RMSE: {:.2f}'.format(rmse_test))

X = WHR_2.drop("Happiness Score", axis=1)
y = WHR_2["Happiness Score"]
reg = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 2)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print(reg.score(X_test, y_test))
rmse_test = np.sqrt(MSE(y_test, y_pred))
print('Test set RMSE: {:.2f}'.format(rmse_test))


from sklearn.ensemble import GradientBoostingRegressor
gbt = GradientBoostingRegressor(n_estimators=300, max_depth=1, random_state=2)
gbt.fit(X_train, y_train)
y_pred_gbt = gbt.predict(X_test)
print(gbt.score(X_test, y_test))
rmse_test_gbt = np.sqrt(MSE(y_test, y_pred_gbt))
print('Test set RMSE_GBT: {:.2f}'.format(rmse_test_gbt))





