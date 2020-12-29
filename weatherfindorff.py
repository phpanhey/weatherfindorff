from urllib.request import urlopen
from bs4 import BeautifulSoup


def getTemperature(url):
    contents = urlopen(weather_url).read()
    soup = BeautifulSoup(contents, "lxml")
    data = soup.find_all("title")[1].get_text()
    return float(
        data.split("………")[1]
        .split("\n")[1]
        .replace(" ", "")
        .replace("°C", "")
        .replace(",", ".")
    )


weather_url = "http://www.ach-du-schan.de/wetterdaten/rss.xml"
temperature = getTemperature(weather_url)
emoji = "😅"
if temperature <= 7:
    emoji = "🥶"

print(f"{emoji}{temperature}°C")
