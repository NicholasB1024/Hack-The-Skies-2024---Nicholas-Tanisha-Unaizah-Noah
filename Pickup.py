#Note: this is imported but not used, find a way to use it later
import GraphSetup
import datetime

# Initialize classes
class Pickup: # initialize class for pickup requests
    def __init__(self, node, time):
        self.loc, self.time = node, time
        
pickupRequests = []
        
def createPickup(location: tuple):
    p = Pickup(location, datetime.datetime.now())
    pickupRequests.append(p)
    
createPickup(["Danforth", "Coxwell"])
createPickup(["Danforth", "Pape"])
createPickup(["Danforth", "Chester"])
createPickup(["Danforth", "Greenwood"])

for i in range(len(pickupRequests)):
    print(pickupRequests[i].loc, pickupRequests[i].time)