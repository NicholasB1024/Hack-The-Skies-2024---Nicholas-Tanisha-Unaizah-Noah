# Initialize classes and functions
class City:
    def __init__(self, city: str, province: str, country: str):
        self.city, self.province, self.country = city, province, country

def address_validation(msg: str, city, locator): # determine pickup and dropoff spots
    while True:
        location = None
        while not location:
            address = input(f'Enter a valid {msg} in {city.city}: ').strip()
            location = locator.geocode(f'{address}, {city.city}, {city.province}, {city.country}')
        confirmation = None
        while confirmation not in ('y', 'n'):
            print('Selected address:', location.address)
            confirmation = input('Confirm address (y/n): ').lower()
        if confirmation == 'y':
            break
    return location

def shortest_path(locStart, locStop, graph, ox):
    # Find corresponding graph nodes for each location
    node1 = ox.distance.nearest_nodes(graph, float(locStart.longitude), float(locStart.latitude))
    node2 = ox.distance.nearest_nodes(graph, float(locStop.longitude), float(locStop.latitude))

    # Find shortest path
    print(graph[node1], '\n', graph[node2])
    path = ox.shortest_path(G=graph, orig=node1, dest=node2, weight='travel_time', cpus=None)
    pathDist = sum([graph[path[i]][path[i + 1]][0].get('length') for i in range(len(path) - 1)])
    print(f'Shortest Path Length: {pathDist / 1000:.1f} km')

    # Print directions
    print('\nDirections:')
    directions = {}
    prevStreetName = None
    for i in range(len(path) - 1):
        streetName = graph[path[i]][path[i + 1]][0].get('name')
        if not (streetName == prevStreetName or type(streetName) != str):
            directions[streetName] = 0
        prevStreetName = streetName
    for i in range(len(path) - 1):
        streetName = graph[path[i]][path[i + 1]][0].get('name')
        streetLen = graph[path[i]][path[i + 1]][0].get('length')
        if type(streetName) == str and streetLen:
            directions[streetName] += streetLen
    for key in directions:
        print(f'{key}: {directions[key]/ 1000:.1f} km')
    print('Arrived!\n')