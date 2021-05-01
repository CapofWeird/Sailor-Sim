# Class definitions

# Define equipment class
class Equipment:
    name = ''      # Equipment name
    equip_id = -1  # Frankly I don't even know if I'll need this property
    value = 0      # Base equipment price
    position = 0   # Numerical representation of equip position
    traits = []    # Any additional traits attached to the equipment
    stats = {
        'max_hull': 0,
        'cargo_space': 0,
        'fuel_rate': 0,
        'speed': 0,
    }


# Define item class
class Item:
    name = ''     # Item name
    item_id = -1  # ID used to manage items
    value = 0     # Base price for the item
    traits = []   # List of traits the item has


# Define location class
class Location(object):

    def __init__(self, name, coords, faction, will_buy, selling):
        self.name = name        # Location name
        self.coords = coords    # X and Y coordinates for the location
        self.faction = faction  # Location primary faction

        self.will_buy = will_buy  # List of item IDs this location will buy
        self.selling = selling  # List of item IDs this location can sell


# Define Sailor class
class Sailor:
    first_name = ""  # Sailor's first name
    last_name = ""   # Sailor's last name
    ship_role = ""   # Their job on the ship
    faction = ""     # The faction their allegiance is primarily given to
    is_spy = False   # Whether or not they are a spy
    hit_point_max = 10
    hit_points = hit_point_max
    veils = 10
    mirrors = 10

    inventory = []


# Define Ship class
class Ship(object):

    def __init__(self, name, ship_class, faction, max_hull, cargo_space,
                 equip_positions, fuel_rate, speed):
        self.name = name
        # The class of the ship, e.g. battleship, merchant cruiser
        self.ship_class = ship_class
        # The faction that this ship comes from
        self.faction = faction
        # Maximum hull points the ship can have
        self.max_hull = max_hull
        # Current hull points. When this hits zero, the ship is destroyed
        self.current_hull = max_hull
        # The number of items that can be stored in the hold
        self.cargo_space = cargo_space
        # The available slots that weapons or equipment can be used
        self.equip_positions = equip_positions
        # A fuel_rate of 2 means this ship travels 2 squares per fuel
        self.fuel_rate = fuel_rate
        # A speed of 1 means this ship travels 1Nm/Hr
        self.speed = speed
        # TODO #1 Move speed and fuel_rate from Ship to Engine

        self.hold = []  # Ship inventory
        self.crew = []  # Holds the current crew
        self.brig = []  # Holds the current prisoners
        self.num_spies = 0  # The number of spies on board the ship

        self.coords = []

    # Adjust stats based on what's equipped
    # TODO: #5 Make two functions for equiping and dequiping equipment
    def reequip(self, equipment):
        for stat in equipment.stats:
            print(stat)  # temp, working to get errors to zero
        return
