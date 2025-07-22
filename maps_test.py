import geocoder
from geopy.distance import great_circle

g = geocoder.ip('me')
#print(g.latlng)

stations_dictionary = {
  'Stations': ['AIRPORT STATION','COLLEGE PARK STATION','EAST POINT STATION','LAKEWOOD/FORT MCPHERSON STATION',
               'OAKLAND CITY STATION','WEST END STATION','GARNETT STATION','FIVE POINTS STATION',
               'PEACHTREE CENTER STATION','CIVIC CENTER STATION','NORTH AVENUE STATION','MIDTOWN STATION',
               'ARTS CENTER STATION','LINDBERGH CENTER STATION','LENOX STATION','BUCKHEAD STATION',
               'MEDICAL CENTER STATION','SANDY SPRINGS STATION','DUNWOODY STATION','NORTH SPRINGS STATION',
               'BROOKHAVEN/OGLETHORPE STATION','CHAMBLEE STATION','DORAVILLE STATION','HAMILTON E. HOLMES STATION',
               'WEST LAKE STATION','ASHBY STATION','BANKHEAD STATION','VINE CITY STATION',
               'GWCC/CNN CENTER STATION','GEORGIA STATE STATION','KING MEMORIAL STATION','EDGEWOOD/CANDLER PARK STATION',
               'EAST LAKE STATION','DECATUR STATION','AVONDALE STATION','KENSINGTON STATION',
               'INDIAN CREEK STATION','INMAN PARK/REYNOLDSTOWN STATION'],
  'lat': [33.6407,33.6792,33.7058,33.7145,33.7225,
          33.7371,33.7483,33.7538,33.7597,33.7667,
          33.7788,33.7845,33.7897,33.8188,33.8451,
          33.8471,33.9048,33.9298,33.9318,33.9575,
          33.8821,33.9038,33.9213,33.7583,33.7531,
          33.7561,33.7712,33.7568,33.7568,33.7516,
          33.7483,33.7667,33.7656,33.7735,33.7731,
          33.7709,33.7709,33.7628],
  'long': [-84.4449,-84.4485,-84.4419,-84.4262,-84.4173,
           -84.4144,-84.3965,-84.3916,-84.3872,-84.3876,
           -84.3868,-84.3873,-84.3878,-84.3695,-84.3577,
           -84.3644,-84.3547,-84.3468,-84.3411,-84.3524,
           -84.3409,-84.3168,-84.2863,-84.4578,-84.4466,
           -84.4172,-84.4326,-84.4079,-84.3971,-84.3852,
           -84.3758,-84.3461,-84.3283,-84.2989,-84.2774,
           -84.2407,-84.2183,-84.3597],
  'line': ['red/yellow','red/yellow','red/yellow','red/yellow',
           'red/yellow','red/yellow','red/yellow','red/yellow',
           'red/yellow','red/yellow','red/yellow','red/yellow',
           'red/yellow','red/yellow','yellow','red',
           'red','red','red','red',
           'yellow','yellow','yellow','HAMILTON E. HOLMES STATION',
           'WEST LAKE STATION','ASHBY STATION','BANKHEAD STATION','VINE CITY STATION',
           'GWCC/CNN CENTER STATION','GEORGIA STATE STATION','KING MEMORIAL STATION','EDGEWOOD/CANDLER PARK STATION',
           'EAST LAKE STATION','DECATUR STATION','AVONDALE STATION','KENSINGTON STATION',
           'INDIAN CREEK STATION','INMAN PARK/REYNOLDSTOWN STATION']
}
#print(f"[{stations_dictionary['lat'][22]}, {stations_dictionary['long'][22]}]")

def find_closest_station():
  closest_location = None
  min_distance = float('inf')


  for i in range(len(stations_dictionary['Stations'])):
    location_name = stations_dictionary['Stations'][i]
    location_coords = (stations_dictionary['lat'][i], stations_dictionary['long'][i])
    #find distance between index station and current location
    curr_distance = great_circle(g.latlng, location_coords)
    #update min
    if curr_distance < min_distance:
      min_distance = curr_distance
      closest_location = location_name

  return closest_location



