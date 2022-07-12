import requests

city = input("input city: ")
api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp'] - 273.15)

print(f"The weather in {city} is {condition} and the current Temperature there is {temp} ") 