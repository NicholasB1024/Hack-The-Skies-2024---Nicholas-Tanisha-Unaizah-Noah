# Initialize classes
class Edge: # edge object represents a street segment (edge) between two intersections (nodes)
    def __init__(self, street: str, street_start: str, street_end: str, weight: int):
        self.a, self.b, self.dist = {street, street_start}, {street, street_end}, weight

segments = {} # dict of all street segments (edges) on a map

class Street: # street object includes its intersections
    def __init__(self, name: str, intersections: list, weights: list): # parallel lists for intersections and weights
        self.name, self.inters, self.dists = name, intersections, weights
        global segments
        for i in range(len(self.dists)):
            new_edges = {Edge(self.name, self.inters[i], self.inters[i + 1], self.dists[i])}
            segments[sorted(list())]
        segments |= new_edges # add new street segments based on new information

def test_segments(): # throwaway function to output the details of every segment on the map
    print(f'\nStreet Segments ({len(segments)}):')
    for segment in segments:
        print(f'{" and ".join(segment.a)} to {" and ".join(segment.b)}. Distance: {segment.dist} meters.')

# Define new street segments
Danforth = Street('Danforth',
                  ['Broadview', 'Chester', 'Pape', 'Donlands', 'Greenwood', 'Coxwell',
                   'Woodbine', 'Main', 'Victoria Park', 'Warden', 'Kennedy'],
                   [100] * 10)

Queen = Street('Queen', ['Greenwood', 'Coxwell', 'Kingston', 'Woodbine'], [850, 450, 600])

test_segments()