"""Main Playground"""

# Imports
# Used to get random options from a list, assign stats
from random import choice, randint

# TODO: #3 Remove wildcard imports
# The various classes being used
from class_defs import Sailor, Ship
# Handles locations
import location_handler as loc
# List of names and factions to pick from
from sailor_names import *
# Handles travel and moving of the ship
import travel_handler as travel


def generate_sailor(faction: tuple, role_list: list, allow_spy=True) -> Sailor:
    """Creates a new sailor"""
    available_roles = role_list

    # Assign names and faction
    first_name = choice(sailorFirstNames)
    last_name = choice(sailorLastNames)
    faction = faction

    # Assign ship role
    if (available_roles != []):
        ship_role = available_roles.pop(0)
    else:
        ship_role = 'Deckhand'

    # Determine stats
    hit_point_max = randint(10, 15)
    veils = randint(5, 15)
    mirrors = randint(5, 15)

    # Determine if they're a spy or not
    if (allow_spy is True):
        if (randint(1, 100) >= 95):
            is_spy = True
            veils += 1  # Increase their veils a little bc they're sneaky!
            # Reroll their faction if they're a spy
            old_faction = faction
            while (faction == old_faction):
                faction = choice(allFactions)
        else:
            is_spy = False

    ocean_man = Sailor(first_name, last_name, ship_role, faction,
                       is_spy, hit_point_max, veils, mirrors)

    return ocean_man


def populate_boat(num_sailors: int, faction: tuple, role_list: list) -> list:
    """Create a boat's worth of sailors"""
    # Initialize the available roles
    available_roles = []
    for x in range(len(role_list)):
        available_roles.append(role_list[x])
    # Initialize the array of all generated sailors
    all_sailors = []
    for x in range(num_sailors):
        new_sailor = generate_sailor(faction, available_roles)
        all_sailors.append(new_sailor)

    return all_sailors


def spy_count(crew: list) -> int:
    """Counts the number of spies in a given crew"""
    num_spies = 0  # Number of spies in the crew
    for x in range(len(crew)):
        if (crew[x].is_spy is True):
            num_spies += 1
    return num_spies


def run_spy_check(crew: list, investigator_role: str) -> list:
    """Investigate the crew to check for spies"""
    detected_spies = []  # List that holds any detected spies
    for x in range(len(crew)):
        if (crew[x].ship_role == investigator_role):
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
                 ['Bridge', 'Forward'], 100, 10, 12)


# Populate main_boat with sailors
main_boat.crew = populate_boat(10, main_boat.faction, shipPositions)
main_boat.num_spies = spy_count(main_boat.crew)


# Test, check the names and positions of the crews
print("Here be the names of our ragtag gang of %s aboard the %s:\n" %
      (main_boat.crew[0].faction[1],
       main_boat.name))
for x in range(len(main_boat.crew)):
    print("%s %s, the %s." % (main_boat.crew[x].first_name,
                              main_boat.crew[x].last_name,
                              main_boat.crew[x].ship_role))


# Test, run spycheck script for verification of faction name functionality
if (main_boat.num_spies > 0):
    print("\nThere are spies on board! "
          + "Captain %s is holding an investigation of all crew members."
          % (main_boat.crew[0].last_name))

    detected_spies = run_spy_check(main_boat.crew, shipPositions[0])
    if (detected_spies == []):
        print("Captain %s could not determine who the spy was..." %
              (main_boat.crew[0].last_name))
    else:
        for x in range(len(main_boat.crew)):
            if (main_boat.crew[x] in detected_spies):
                print("%s %s was determined to be a spy for the %s!" %
                      (main_boat.crew[x].first_name,
                       main_boat.crew[x].last_name,
                       main_boat.crew[x].faction[2]))
            else:
                print("%s %s was determined to not be a spy..." %
                      (main_boat.crew[x].first_name,
                       main_boat.crew[x].last_name))

    # Temp prints
    print("\nSpies found: %d" % (len(detected_spies)))
    print("Actual spy count: %d" % (main_boat.num_spies))

# Test, plot the path from the ship to our destination
main_boat.coords = [randint(-100, 100), randint(-100, 100)]
destination = loc.make_locale([])
trip_time = travel.get_time_to_dest(main_boat.coords,
                                    destination.coords,
                                    main_boat.speed)
trip_distance = travel.get_dist_to_dest(main_boat.coords, destination.coords)
dest_path = travel.plot_path(main_boat.coords,
                             destination.coords,
                             main_boat.speed)

print("\nThe %s lies at %s." %
      (main_boat.name, loc.coord_flavor(main_boat.coords)))
print("Our destination is %s, at %s, which is %.2lf nautical miles away."
      % (destination.name,
         loc.coord_flavor(destination.coords),
         trip_distance))
print("The journey will take about %.2lf hours, " % (trip_time)
      + "and will use %.2lf units of fuel.\n"
      % (trip_distance / main_boat.fuel_rate))
