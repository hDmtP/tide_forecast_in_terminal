#!/usr/bin/python3
import requests
import fontstyle
from bs4 import BeautifulSoup


def main():
    URL = "https://tide-forecast.com/locations/Calcutta-Garden-Reach-India/tides/latest"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    tide_forecast = soup.find(class_="tide-day-tides")

    count = 0
    arr = [None]*25

    for elem1 in tide_forecast.stripped_strings:
        arr[count] = elem1
        count += 1
        if(count >= 4 and count % 4 == 0):
            pass

    data = fontstyle.apply(
        f"|| {arr[4]} = {arr[5]} ||\n|| {arr[9]} = {arr[10]}  ||\n|| {arr[14]} = {arr[15]} ||\n|| {arr[19]} = {arr[20]}  ||", "bold/white/BLACK_BG")

    print(fontstyle.apply("========================", "bold/red/YELLOW_BG"))
    print(f"{data}")
    print(fontstyle.apply("========================", "bold/red/YELLOW_BG"))


if __name__ == "__main__":
    main()
