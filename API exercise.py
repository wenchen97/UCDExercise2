import requests
#request=requests.get('http://api.open-notify.org/iss-now.json')
#print(request.status_code)
#print(request.text)

request2=requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=Default')
print(request2.status_code)
print(request2.text)