# Initialize classes
class Pickup: # initialize class for pickup requests
    def __init__(self, node, time):
        self.loc, self.time = node, time

class Edge: # edge object represents a street segment (edge) between two intersections (nodes)
    def __init__(self, street, street_start, street_end, weight):
        self.a, self.b, self.dist = {street, street_start}, {street, street_end}, weight

segments = set() # set of all street segments (edges) on a map

class Street: # street object includes its intersections
    def __init__(self, name, intersections: list, weights: list):
        self.name, self.inters, self.dists = name, intersections, weights
        global segments
        new_edges = {Edge(self.name, self.inters[i], self.inters[i + 1], self.dists[i]) for i in range(len(self.dists))}
        segments |= new_edges # add new street segments based on new information

def test_segments(): # throwaway function to output the details of every segment on the map
    for segment in segments:
        print(f'Street Segment: Connecting {segment.a} and {segment.b}. Distance: {segment.dist} meters.')

# Define new street segments
Danforth = Street('Danforth', ['Broadview', 'Chester', 'Pape', 'Donlands', 'Greenwood', 'Coxwell',
                   'Woodbine', 'Main', 'Victoria Park', 'Warden', 'Kennedy'], [100] * 10)

test_segments()



'''
Queen_Street_E_1 = Edge("Greenwood Ave", "Coxwell Ave", 850)
streets.add(Queen_Street_E_1)

Queen_Street_E_2 = Edge("Coxwell Ave", "Kingston Rd", 450)
streets.add(Queen_Street_E_2)

Queen_Street_E_3 = Edge("Kingston Rd", "Woodbine Ave", 600)
streets.add(Queen_Street_E_3)
'''