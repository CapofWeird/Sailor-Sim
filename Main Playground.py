# Main Playground

# Imports
# Used to get random options from a list, assign stats
from random import choice, randint

# TODO: #3 Remove wildcard imports
from class_defs import *            # The various classes being used
from date_time import *             # Handles the flow of time
from location_handler import *      # Handles locations
from sailor_names import *          # List of names and factions to pick from
from travel_handler import *        # Handles travel and moving of the ship


# Create a new sailor
def generate_sailor(faction, role_list, allow_spy=True):
    available_roles = role_list
    ocean_man = Sailor()
    # Assign names and faction
    ocean_man.firstName = choice(sailorFirstNames)
    ocean_man.lastName = choice(sailorLastNames)
    ocean_man.faction = faction
    # Assign ship role
    if (available_roles != []):
        ocean_man.ship_role = available_roles.pop(0)
    else:
        ocean_man.ship_role = 'Deckhand'
    # Determine stats
    ocean_man.hitPointMax = randint(10, 15)
    ocean_man.hitPoints = ocean_man.hitPointMax
    ocean_man.veils = randint(5, 15)
    ocean_man.mirrors = randint(5, 15)
    # Determine if they're a spy or not
    if (allow_spy is True):
        if (randint(1, 100) >= 95):
            ocean_man.is_spy = True
            ocean_man.veils += 1
            # Reroll their faction if they're a spy
            while (ocean_man.faction == faction):
                ocean_man.faction = choice(allFactions)

    return ocean_man


# Create a boat's worth of sailors
def PopulateBoat(numSailors, faction, role_list):
    # Initialize the available roles
    available_roles = []
    for x in range(len(role_list)):
        available_roles.append(role_list[x])
    # Initialize the array of all generated sailors
    allSailors = []
    for x in range(numSailors):
        newSailor = generate_sailor(faction, available_roles)
        allSailors.append(newSailor)

    return allSailors


# Count the number of spies on board
def spy_count(crew):
    num_spies = 0  # Number of spies in the crew
    for x in range(len(crew)):
        if (crew[x].is_spy is True):
            num_spies += 1
    return num_spies


# Investigate the crew to check for spies
def run_spy_check(crew, invest_role):
    detected_spies = []  # List that holds any detected spies
    for x in range(len(crew)):
        if (crew[x].ship_role == invest_role):
            investigator = crew[x]
            break
    for x in range(len(crew)):
        if ((investigator.mirrors > crew[x].veils) and
           (crew[x] != investigator)):
            if (crew[x].is_spy is True):
                detected_spies.append(crew[x])

    return detected_spies


# Initializing time
current_time = [0, 15, 7, 5, 1836]

# Initialize the player boat
main_boat = Ship(choice(shipNames), 'Merchant', choice(allFactions), 50, 25,
                 ['Bridge', 'Forward'], 10, 12)

# For funsies and testing, make an enemy boat
# badBoat = ship(choice(shipNames), 'Battleship', choice(allFactions), 150,
#                20, ['Aft', 'Bridge', 'Forward'], 1, 4)


# Populate main_boat with sailors
main_boat.crew = PopulateBoat(10, main_boat.faction, shipPositions)
main_boat.num_spies = spy_count(main_boat.crew)

# ##Populate badBoat with sailors
# #badBoat.crew = PopulateBoat(10, badBoat.faction, shipPositions)


# Test, check the names and positions of the crews
print("Here be the names of our ragtag gang of %s aboard the %s:\n" %
      (main_boat.crew[0].faction[1],
       main_boat.name))
for x in range(len(main_boat.crew)):
    print("%s %s, the %s." % (main_boat.crew[x].firstName,
                              main_boat.crew[x].lastName,
                              main_boat.crew[x].ship_role))

# #print("\nHere be the names of our enemy %s aboard their %s:\n"
#        % (badBoat.crew[0].faction[1], badBoat.name))
# #for x in range(len(badBoat.crew)):
# #    print("%s %s, the %s." % (badBoat.crew[x].firstName,
#                                badBoat.crew[x].lastName,
#                                badBoat.crew[x].ship_role))

# Test, run spycheck script for verification of faction name functionality
if (main_boat.num_spies > 0):
    print("\nThere are spies on board! "
          + "Captain %s is holding an investigation of all crew members."
          % (main_boat.crew[0].lastName))

    detected_spies = run_spy_check(main_boat.crew, shipPositions[0])
    if (detected_spies == []):
        print("Captain %s could not determine who the spy was..." %
              (main_boat.crew[0].lastName))
    else:
        for x in range(len(main_boat.crew)):
            if (main_boat.crew[x] in detected_spies):
                print("%s %s was determined to be a spy for the %s!" %
                      (main_boat.crew[x].firstName,
                       main_boat.crew[x].lastName,
                       main_boat.crew[x].faction[2]))
            else:
                print("%s %s was determined to not be a spy..." %
                      (main_boat.crew[x].firstName,
                       main_boat.crew[x].lastName))

    print("\nSpies found: %d" % (len(detected_spies)))
    print("Actual spy count: %d" % (main_boat.num_spies))

# Test, plot the path from the ship to our destination
main_boat.coords = [randint(-100, 100), randint(-100, 100)]
destination = make_locale([])
trip_time = get_time_to_dest(main_boat.coords,
                             destination.coords,
                             main_boat.speed)
trip_distance = get_dist_to_dest(main_boat.coords, destination.coords)
dest_path = plot_path(main_boat.coords, destination.coords, main_boat.speed)

print("\nThe %s lies at coordinates (%d, %d)." %
      (main_boat.name, main_boat.coords[0], main_boat.coords[1]))
print("Our destination is %s, at (%d, %d), which is %.2lf nautical miles away."
      % (destination.name, destination.coords[0],
         destination.coords[1], trip_distance))
print("The journey will take about %.2lf hours, " % (trip_time)
      + "and will use about %.2lf units of fuel.\n"
      % (trip_distance / main_boat.fuel_rate))
