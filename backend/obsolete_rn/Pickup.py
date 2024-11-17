import datetime, GraphSetup # GraphSetup currently unused

# Initialize classes
pickup_queue = []

class Pickup: # pickup request class
    def __init__(self, node: set):
        self.loc, self.time = node, datetime.datetime.now()
        pickup_queue.append(self)
        pickup_queue.sort(key=lambda x: x.time)

Pickup({"Danforth", "Coxwell"})
Pickup({"Danforth", "Pape"})
Pickup({"Danforth", "Chester"})
Pickup({"Danforth", "Greenwood"})

for pickup in pickup_queue:
    print(pickup.loc, pickup.time)