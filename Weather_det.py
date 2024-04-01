import requests

#enter your API key which is generated from openweathermap.org
 
key="d8c74fa1e6ab93157875ee3ddc938077"

city=input("enter your city name:")

url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+key

res=requests.get(url).json()
print(f"Here are the {city} Weather details:")
print(res)
