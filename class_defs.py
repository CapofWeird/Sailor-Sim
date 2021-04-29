#Class definitions

#Define equipment class
class equipment:
    name = ''     #Equipment name
    equipID  = -1 #Frankly I don't even know if I'll need this property
    value    =  0 #Base equipment price
    position =  0 #Numerical representation of equip position
    traits   = [] #Any additional traits attached to the equipment
    statChanges = {
        'maxHull': 0,
        'cargoSpace': 0,
        'fuelRate': 0,
        'speed': 0,
    }

#Define item class
class item:
    name = '' #Item name
    itemID = -1 #ID used to manage items
    value  =  0 #Base price for the item (Changes depending on if buying/selling, location)
    traits = [] #List of traits the item has

#Define location class
class location(object):

    def __init__(self, name, coords, faction, willBuy, selling):
        self.name    = name    #Location name
        self.coords  = coords  #X and Y coordinates for the location
        self.faction = faction #Location primary faction

        self.willBuy = willBuy #List of itemIDs this location will buy
        self.selling = selling #List of itemIDs this location can sell

#Define Sailor class
class sailor:
    firstName = "" #Sailor's first name
    lastName  = "" #Sailor's last name
    shipRole  = "" #Their job on the ship
    faction   = "" #The faction their allegiance is primarily given to
    isSpy = False  #Whether or not they are a spy
    hitPointMax = 10
    hitPoints = hitPointMax
    veils   = 10
    mirrors = 10

    inventory = []

#Define Ship class
class ship(object):

    def __init__(self, name, shipClass, faction, maxHull, cargoSpace, equipPositions, fuelRate, speed):
        self.name = name
        self.shipClass = shipClass #The class of the ship, e.g. battleship, merchant cruiser
        self.faction = faction #The faction that this ship comes from, and the majority of the crew serve
        self.maxHull = maxHull #Maximum hull points the ship can have
        self.currentHull = maxHull #Current hull points. When this hits zero, the ship is destroyed
        self.cargoSpace = cargoSpace #The number of items that can be stored in the hold
        self.equipPositions = equipPositions #The available slots that weapons or equipment can be used
        self.fuelRate = fuelRate #A fuelRate of 2 means this ship travels 2 squares per fuel
        self.speed = speed #A speed of 1 means this ship travels 1 nautical mile(1 square) per hour (1Nm/Hr)
        #Also, I might end up moving fuelRate and speed to different engine items, ya know, for more
        #variety and to steal even more ideas from Sunless Sea (pls forgive, failbetter)

        self.hold = [] #Ship inventory
        self.crew = [] #Holds the current crew
        self.brig = [] #Holds the current prisoners
        self.numSpies = 0 #The number of spies on board the ship

        self.coords = []

    #Adjust stats based on what's equipped
    def Reequip(self, equipment):
        #Haven't done anything with this yet, so right now
        #it just returns nothing to make the editor stop
        #screaming at me to fix it
        return
