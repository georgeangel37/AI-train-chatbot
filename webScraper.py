import requests
from bs4 import BeautifulSoup
from datetime import datetime


# start - journey start, represented as either the city name or station postcode
# end - journey end, represented as either the city name or station postcode
# day - the date of the journey, represented either as today, tommorow, or a string in the yymmdd format
# time - the desired departure or arrival time, represented in the hhmm format
# DepartureOrArrive - represents whether the time and date represent the time of departure or arrival, arr for arrival and dep for departure

def get_price(start, end, day, time, DepartureOrArrive):
    if not valid_date(day, time):
        print("Error! The day and time must be in the future!")
        return ("", "")
    url = f"https://ojp.nationalrail.co.uk/service/timesandfares/{start}/{end}/{day}/{time}/{DepartureOrArrive}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", id="oft")
    cell = table.find("td", {"class": "fare has-cheapest"})
    fare = cell.find("label", {"class": "opsingle"})
    return (fare.text.strip(), url)

def valid_date(day, time):
    if day == "today" or day == "tomorrow":
        return True
    now = datetime.now()
    date = datetime.strptime(day+time, "%d%m%y%H%M")
    return date >= now

fare, url = get_price("London", "CAM", "tomorrow", "1730", "arr")
print(fare)
print(url)

valid_date("150623", "1730")