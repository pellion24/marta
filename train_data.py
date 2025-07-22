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

def startup ():
  print(f"Are you at {maps_test.find_closest_station()}? (Y/N)")
  intialStationCorrect = input()
  current_station = ""

  if (intialStationCorrect != "Y"):
    print("Enter your station in all caps, with 'STATION' at the end")
    current_station = input()
  else:
    current_station = maps_test.find_closest_station()
  return current_station


