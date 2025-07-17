#identify red/gold stops and blue/green stops
#identify transfer points: lindbergh, Ashby, five points and edgewood/candler park
#divide in north south east and west sectors, any switch from north/south to east/west or vice versa
#requires trasfer at five points

red_and_yellow_line: ['AIRPORT STATION','COLLEGE PARK STATION','EAST POINT STATION','LAKEWOOD/FORT MCPHERSON STATION',
'OAKLAND CITY STATION','WEST END STATION','GARNETT STATION','FIVE POINTS STATION',
'PEACHTREE CENTER STATION','CIVIC CENTER STATION','NORTH AVENUE STATION','MIDTOWN STATION',
'ARTS CENTER STATION','LINDBERGH CENTER STATION']
red_line: ['BUCKHEAD STATION','MEDICAL CENTER STATION','SANDY SPRINGS STATION','DUNWOODY STATION','NORTH SPRINGS STATION']
yellow_line: ['LENOX STATION', 'BROOKHAVEN/OGLETHROPE STATION', 'CHAMBLEE STATION', 'DORAVILLE STATION']

def plan_route(start, finish):
  #if route doesnt involve transfer, find both locs, minus for amount of stops

  #if route invovles transfer, identify zones, find transfer location,
