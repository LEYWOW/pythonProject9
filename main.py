import requests
from bs4 import BeautifulSoup

def get_temperature():
    url = 'https://sinoptik.ua/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature_div = soup.find('p', class_='today-temp')
        if temperature_div:
            temperature = temperature_div.text.strip()
            return temperature
    return None

try:
    temperature = get_temperature()
    if temperature:
        print(f"Температура сьогодні: {temperature}")
    else:
        print("Не вдалося отримати дані про температуру")
except requests.exceptions.RequestException:
    print("Помилка підключення до веб-сайту")