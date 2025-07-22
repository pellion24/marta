from nicegui import ui
import maps_test
import train_data

direction = 'None'
station = maps_test.find_closest_station()
info = train_data.get_train_info()

#UI Elements
output_label = None
train_info_output = None
station_select_card = None
direction_card = None
station_select_dropdown = None

def update_direction(event):
  global direction
  direction = event.value
  if output_label:
    output_label.set_text(f"Current Direction: {direction}")
  ui.notify(f"Direction updated to: {direction}", timeout=1000)
  if train_info:
    train_info.visible = True
    find_trains(station, direction)

def get_full_direction(short_code):
  match short_code:
    case "S": return "southbound"
    case "N": return "northbound"
    case "W": return "westbound"
    case "E": return "eastbound"
    case _: return "unknown direction" # Handle unexpected codes

def update_station(event):
  global station
  station = event.value
  ui.notify(f"Station updated to {station}", timeout=1000)
  if station_select_card:
    station_select_card.visible=False
  show_direction_card()

def show_direction_card():
  ui.notify(f"At: {station}")
  if direction_card: # Ensure the card exists before trying to show it
    direction_card.visible = True


def change_station():
  if station_select_card:
    station_select_card.visible = True

def find_trains(curr_station, curr_direction):
  found_trains = []
  global info
  for train in info:
    print(f"Checking for {curr_direction} trains from {curr_station}")
    if (train["STATION"] == curr_station and
        train["IS_REALTIME"] == "true" and
        train["DIRECTION"] == curr_direction):

      direction_short = train["DIRECTION"]
      wait_time = train["WAITING_TIME"]
      dir = get_full_direction(direction_short)
      line = train["LINE"]
      found_trains.append(f"A {dir} {line} line train is departing from {curr_station} in {wait_time}")
      print(f"A {dir} {line} line train is departing from {curr_station} in {wait_time}")
  if found_trains:
    # Use HTML to format multiple lines, or ui.run_javascript for more complex formatting
    content = "<br>".join(found_trains)
    train_info_output.set_content(f"<div class='font-bold text-green-700 mb-2'>Trains Found:</div>{content}")
  else:
    print("what the helly")
    train_info_output.set_content(f"No real-time trains found for {curr_station} at this moment.")
    ui.notify("No trains found.", color="warning")


ui.label("Welcome to the MARTA Helper!")
ui.label(f"Are you at {station}?")
with ui.button_group():
  ui.button('Yes', on_click= lambda: show_direction_card())
  ui.button('No', on_click= lambda: change_station())

with ui.card() as station_select_card:
  station_select_card.visible = False
  ui.label("Selection new station")
  ui.select(
    options=maps_test.stations_dictionary['Stations'],
    value=station,
    on_change=update_station
  )

with ui.card() as direction_card:
  direction_card.visible = False
  ui.label("Select your direction")
  ui.select(
    options=['None', 'N', 'S', 'E', 'W'],
    value=direction,
    label="select",
    on_change=update_direction
  )
  output_label = ui.label(f"Current Direction: {direction}")

with ui.card() as train_info:
  train_info.visible = False
  train_info_output = ui.html('<div>"Info Here"</div>')

ui.run()
