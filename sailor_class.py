from sailor_names import * #List of names and factions to pick from
from class_defs import ship
from random import choice, randint #Used to get random options from a list, assign stats

#Define Sailor class
class sailor:
    firstName = "" #Sailor's first name
    lastName = ""  #Sailor's last name
    shipRole = ""  #Their job on the ship
    faction = ""   #The faction their allegiance is primarily given to
    isSpy = False  #Whether or not they are a spy
    hitPointMax = 10
    hitPoints = hitPointMax
    veils = 10
    mirrors = 10

    inventory = []

    def SailorDeath(self):
        print("%s %s has died." % (self.firstName, self.lastName))


#This isn't being used right now, but it's kind of a neat function anyway
def NextListItem(listName):
	nextItem = listName[0]
	listName.append(listName[0])
	listName.remove(listName[0])

	return nextItem

#Create a new sailor
def GenerateSailor(faction, allowSpy = True):
    availableRoles = shipPositions #Frankly I don't know how or why this works
    oceanMan = sailor()
    #Assign names and faction
    oceanMan.firstName = choice(sailorFirstNames)
    oceanMan.lastName = choice(sailorLastNames)
    oceanMan.faction = faction
    #Assign ship role
    #The ship roles are just not working right now
    #and need to be rebuilt
    if (availableRoles != []):
        oceanMan.shipRole = availableRoles[0]
        availableRoles.remove(availableRoles[0])
    else:
        oceanMan.shipRole = 'Deckhand'
    #Determine stats
    oceanMan.hitPointMax = randint(10, 15)
    oceanMan.hitPoints = oceanMan.hitPointMax
    oceanMan.veils = randint(5, 15)
    oceanMan.mirrors = randint(5, 15)
    #Determine if they're a spy or not
    if (allowSpy == True):
        if (randint(1, 100) >= 95):
            oceanMan.isSpy = True
            oceanMan.veils += 1
            #Reroll their faction if they're a spy
            while (oceanMan.faction == faction):
                oceanMan.faction = choice(allFactions)
    
    return oceanMan

#Create a boat's worth of sailors
def PopulateBoat(numSailors, faction, roleList):
    #Initialize the available roles
    availableRoles = []
    for x in range(len(roleList)):
        availableRoles.append(roleList[x])
    #Initialize the array of all generated sailors
    allSailors = []
    for x in range(numSailors):
        newSailor = GenerateSailor(faction, availableRoles)
        allSailors.append(newSailor)

    return allSailors

#Investigate the crew to check for spies
def RunSpyCheck(crew):
    detectedSpies = [] #Array that holds any detected spies
    #The captain is in charge of investigating the crew
    for x in range(len(crew)):
        if (crew[x].shipRole == 'Captain'):
            investigator = crew[x]
    for x in range(len(crew)):
        if (investigator.mirrors > crew[x].veils):
            if (crew[x].isSpy == True):
                detectedSpies.append(crew[x])

    return detectedSpies
    

#Main
faction = choice(allFactions)
spyCount = 0
boatContents = PopulateBoat(10, faction)

print("Here be the names of our ragtag gang of %s:\n" % (faction))
for x in range(len(boatContents)):
    print("%s %s, the %s." % (boatContents[x].firstName, boatContents[x].lastName, boatContents[x].shipRole))
print("\n") #Blank line

for x in range(len(boatContents)):
    if (boatContents[x].isSpy == True):
        spyCount += 1

if (spyCount > 0):
    print("There are spies on board! Captain %s is holding an investigation of all crew members." % (boatContents[0].lastName))
    detectedSpies = RunSpyCheck(boatContents)
    if (detectedSpies == []):
        print("Captain %s could not determine who the spy was..." % (boatContents[0].lastName))
    else:
        for x in range(len(boatContents)):
            if (boatContents[x].isSpy == True):
                print("%s %s was determined to be a spy for the %s!" % (boatContents[x].firstName, boatContents[x].lastName, boatContents[x].faction))
            else:
                print("%s %s was determined to not be a spy..." % (boatContents[x].firstName, boatContents[x].lastName))

    print("\nSpies found: %d" % (len(detectedSpies)))
    print("Actual spy count: %d" % (spyCount))

