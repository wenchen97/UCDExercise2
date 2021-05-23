import requests
request2=requests.get('https://world-population.p.rapidapi.com/population')


def gdp_per_capita (x,y):
    return x/y

print(gdp_per_capita(200,500))
