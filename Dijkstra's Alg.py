# Initialize class for pickup requests
class Pickup:
    def __init__(self, node, time):
        self.loc, self.time = node, time

# Initialize class for "edges" (representing street segments)
class Edge:
    def __init__(self, node_A, node_B, weight):
        self.a, self.b, self.meters = node_A, node_B, weight

# Set of all street segments on a map
streets = set()

# Throwaway function to output the details of every segment on the map
def test_streets():
    for i, street in enumerate(streets):
        print(f'Street Segment #{i + 1}: Connecting {street.a} and {street.b}. Distance: {street.meters} meters.')

# Define new street segments
Queen_Street_E_1 = Edge("Greenwood Ave", "Coxwell Ave", 850)
streets.add(Queen_Street_E_1)

Queen_Street_E_2 = Edge("Coxwell Ave", "Kingston Rd", 450)
streets.add(Queen_Street_E_2)

Queen_Street_E_3 = Edge("Kingston Rd", "Woodbine Ave", 600)
streets.add(Queen_Street_E_3)

test_streets()