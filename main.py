import requests
import maps_test

base_url='https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey='
API_KEY='1d5ed833-7e1d-4efd-9ad7-9be9083752b4'

def get_train_info () :
  url = f"https://developerservices.itsmarta.com:18096/itsmarta/railrealtimearrivals/developerservices/traindata?apiKey=1d5ed833-7e1d-4efd-9ad7-9be9083752b4"
  response = requests.get(url)

  if response.status_code == 200:
    train_data = response.json()
    return train_data
  else:
    print(f"failed to get train info {response.status_code}")

#print("Enter Station")
#station = input()
#print(station)
print("Welcome to the MARTA Helper!")
print(f"Are you at {maps_test.find_closest_station()}? (Y/N)")
intialStationCorrect = input()

data = get_train_info()
#maps_test.find_closest_station()

current_station = ""
#train["STATION"] == station and
if (intialStationCorrect != "Y"):
  print("Enter your station in all caps, with 'STATION' at the end")
  current_station = input()
else:
  current_station = maps_test.find_closest_station()

print("Enter Direction")
dir = input()
print(f"Checking for train info at {current_station}")

for train in data:
  if train["STATION"] == current_station and train["IS_REALTIME"] == "true" and train["DIRECTION"] == dir:
      direction_short = train["DIRECTION"]
      wait_time = train["WAITING_TIME"]
      direction = ""
      match direction_short:
        case "S":
          direction = "southbound"
        case "N":
          direction = "northbound"
        case "W":
          direction = "westbound"
        case "E":
          direction = "eastbound"
      line = train["LINE"]
      station_at = train["STATION"]
      print(f"A {direction} {line} line train is {wait_time} away from {station_at}")

