import requests
from bs4 import BeautifulSoup

def get_weather(city="islamabad"):
    # Weather.com search URLs are not stable, but you can get location codes manually
    url = "https://weather.com/weather/today/l/33.69,73.05"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    temp = soup.find("span", {"data-testid": "TemperatureValue"})
    desc = soup.find("div", {"data-testid": "wxPhrase"})
    if not (temp and desc):
        print(soup.prettify())
        return "Could not fetch weather from weather.com."
    return f"{temp.text}, {desc.text}"

print(get_weather())