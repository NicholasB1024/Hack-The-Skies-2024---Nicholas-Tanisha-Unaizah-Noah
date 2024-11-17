print('Loading osmnx...')
import osmnx as ox
print('Making HTTP requests to Nominatim API...')
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent='xX_TTV_MLG_PXTHZFVNDR_69420_Xx') # establish locator object

# Initialize classes and functions
class City:
    def __init__(self, city: str, province: str, country: str):
        self.city, self.province, self.country = city, province, country

locConstant = City('Toronto', 'Ontario', 'Canada') # constant information for locations

def address_validation(msg: str): # determine pickup and dropoff spots
    while True:
        location = None
        while not location:
            address = input(f'Enter a valid {msg} in {locConstant.city}: ').strip()
            location = locator.geocode(f'{address}, {locConstant.city}, {locConstant.province}, {locConstant.country}')
        print(location.address)
        confirmation = None
        while confirmation not in ('y', 'n'):
            confirmation = input('Confirm address:\n(y/n): ').lower()
        if confirmation == 'y':
            break
    return location

# Pickup and dropoff
locStart = address_validation('pickup address')
locStop = address_validation('dropoff address')

# Find shortest path
print(f'Accessing graph of {locConstant.city} (takes a little too long as of now)...')
# graph of toronto below, takes a while, so radial from locStart is used instead temporarily
# graph = ox.graph_from_place(f'{locConstant.city, locConstant.province, locConstant.country}', network_type='drive')
graph = ox.graph_from_point((locStart.latitude, locStart.longitude), dist=2000, network_type='drive')
node1 = ox.distance.nearest_nodes(graph, float(locStart.longitude), float(locStart.latitude))
node2 = ox.distance.nearest_nodes(graph, float(locStop.longitude), float(locStop.latitude))

print('Finding shortest path...')
path = ox.shortest_path(G=graph, orig=node1, dest=node2, cpus=None)
print('\nShortest Path Length:', len(path))

# Print directions
print('\nDirections:')
prevStreetName = None
for i in range(len(path) - 1):
    streetName = graph[path[i]][path[i + 1]][0].get('name')
    if not (streetName == None or streetName == prevStreetName):
        print(streetName)
    prevStreetName = streetName
print('Arrived!\n')