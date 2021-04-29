# Main Playground

# Import all the things!
from class_defs import *            # The various classes being used
from date_time import *             # Handles the flow of time
from location_handler import *      # Handles locations
from random import choice, randint  # Used to get random options from a list, assign stats
from sailor_names import *          # List of names and factions to pick from
from travel_handler import *        # Handles travel and moving of the ship


# Create a new sailor
def GenerateSailor(faction, roleList, allowSpy=True):
    availableRoles = roleList
    oceanMan = sailor()
    # Assign names and faction
    oceanMan.firstName = choice(sailorFirstNames)
    oceanMan.lastName = choice(sailorLastNames)
    oceanMan.faction = faction
    # Assign ship role
    if (availableRoles != []):
        oceanMan.shipRole = availableRoles.pop(0)
    else:
        oceanMan.shipRole = 'Deckhand'
    # Determine stats
    oceanMan.hitPointMax = randint(10, 15)
    oceanMan.hitPoints = oceanMan.hitPointMax
    oceanMan.veils = randint(5, 15)
    oceanMan.mirrors = randint(5, 15)
    # Determine if they're a spy or not
    if (allowSpy is True):
        if (randint(1, 100) >= 95):
            oceanMan.isSpy = True
            oceanMan.veils += 1
            # Reroll their faction if they're a spy
            while (oceanMan.faction == faction):
                oceanMan.faction = choice(allFactions)

    return oceanMan


# Create a boat's worth of sailors
def PopulateBoat(numSailors, faction, roleList):
    # Initialize the available roles
    availableRoles = []
    for x in range(len(roleList)):
        availableRoles.append(roleList[x])
    # Initialize the array of all generated sailors
    allSailors = []
    for x in range(numSailors):
        newSailor = GenerateSailor(faction, availableRoles)
        allSailors.append(newSailor)

    return allSailors


# Count the number of spies on board
def SpyCount(crew):
    spyCount = 0
    for x in range(len(crew)):
        if (crew[x].isSpy is True):
            spyCount += 1
    return spyCount


# Investigate the crew to check for spies
def RunSpyCheck(crew, investRole):
    detectedSpies = []  # Array that holds any detected spies
    for x in range(len(crew)):
        if (crew[x].shipRole == investRole):
            investigator = crew[x]
            break
    for x in range(len(crew)):
        if ((investigator.mirrors > crew[x].veils) and (crew[x] != investigator)):
            if (crew[x].isSpy is True):
                detectedSpies.append(crew[x])

    return detectedSpies


# Initializing time
currentTime = [0, 15, 7, 5, 1836]

# Initialize the player boat
mainBoat = ship(choice(shipNames), 'Merchant', choice(allFactions), 50, 25, ['Bridge', 'Forward'], 10, 12)

# ##For funsies and testing, make an enemy boat
# #badBoat = ship(choice(shipNames), 'Battleship', choice(allFactions), 150, 20, ['Aft', 'Bridge', 'Forward'], 1, 4)


# Populate mainBoat with sailors
mainBoat.crew = PopulateBoat(10, mainBoat.faction, shipPositions)
mainBoat.numSpies = SpyCount(mainBoat.crew)

# ##Populate badBoat with sailors
# #badBoat.crew = PopulateBoat(10, badBoat.faction, shipPositions)


# Test, check the names and positions of the crews
print("Here be the names of our ragtag gang of %s aboard the %s:\n" %
      (mainBoat.crew[0].faction[1],
       mainBoat.name))
for x in range(len(mainBoat.crew)):
    print("%s %s, the %s." % (mainBoat.crew[x].firstName,
                              mainBoat.crew[x].lastName,
                              mainBoat.crew[x].shipRole))

# #print("\nHere be the names of our enemy %s aboard their %s:\n" % (badBoat.crew[0].faction[1], badBoat.name))
# #for x in range(len(badBoat.crew)):
# #    print("%s %s, the %s." % (badBoat.crew[x].firstName, badBoat.crew[x].lastName, badBoat.crew[x].shipRole))

# Test, run spycheck script for verification of faction name functionality
if (mainBoat.numSpies > 0):
    print("\nThere are spies on board! Captain %s is holding an investigation of all crew members." % (mainBoat.crew[0].lastName))
    detectedSpies = RunSpyCheck(mainBoat.crew, shipPositions[0])
    if (detectedSpies == []):
        print("Captain %s could not determine who the spy was..." %
              (mainBoat.crew[0].lastName))
    else:
        for x in range(len(mainBoat.crew)):
            if (mainBoat.crew[x] in detectedSpies):
                print("%s %s was determined to be a spy for the %s!" %
                      (mainBoat.crew[x].firstName,
                       mainBoat.crew[x].lastName,
                       mainBoat.crew[x].faction[2]))
            else:
                print("%s %s was determined to not be a spy..." %
                      (mainBoat.crew[x].firstName,
                       mainBoat.crew[x].lastName))

    print("\nSpies found: %d" % (len(detectedSpies)))
    print("Actual spy count: %d" % (mainBoat.numSpies))

# Test, plot the path from the ship to our destination
mainBoat.coords = [randint(-100, 100), randint(-100, 100)]
destination = MakeLocale([])
tripTime = GetTimeToDest(mainBoat.coords, destination.coords, mainBoat.speed)
tripDistance = GetDistToDest(mainBoat.coords, destination.coords)
destPath = PlotPath(mainBoat.coords, destination.coords, mainBoat.speed)

print("\nThe %s lies at coordinates (%d, %d)." %
      (mainBoat.name, mainBoat.coords[0], mainBoat.coords[1]))
print("Our destination is %s, at (%d, %d), which is %.2lf nautical miles away." %
      (destination.name, destination.coords[0], destination.coords[1], tripDistance))
print("The journey will take about %.2lf hours, and will use about %.2lf units of fuel.\n" %
      (tripTime, tripDistance / mainBoat.fuelRate))
