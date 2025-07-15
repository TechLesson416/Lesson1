# Погода через API
import requests
from PIL import Image
import io

API_KEY =
URL =
CITY =

params = {

    'q': CITY,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(URL, params=params)
result = response.json()

weather = result['weather'][0]['description']
temperature = result['main']['temp']
humidity = result['main']['humidity']
wind = result['wind']['speed']
data = result['coords']
ll = f'{data['lon']},{data['lat']}'
print(ll)


print(f'Сегодня в городе {CITY}: {weather}')
print(f'Температура: {temperature:.1}\xB0'f'C')
print(f'Влажность: {humidity}')
print(f'Скорость ветра: {wind}')
link = https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.0025,0.0025&l=map&pt={ll},pm2dgl
image = requests.get(link).content
if image:
    Image.open(io.BytesIO(image)).show()
