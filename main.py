import train_data
import maps_test
data = train_data.get_train_info()

curr = train_data.startup()

print("Enter Direction")
dir = input()
print(f"Checking for train info at {curr}")

for train in data:
  if train["STATION"] == curr and train["IS_REALTIME"] == "true" and train["DIRECTION"] == dir:
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

