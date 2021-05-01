# Class definitions

# Define equipment class
class Equipment:

    def __init__(self, name: str, equip_id: int, value: int,
                 position: int, traits: list, stats: dict):
        self.name = name  # Equipment name
        self.equip_id = equip_id  # ID used to manage equipment
        self.value = value  # Base equipment price
        self.position = position  # Numerical representation of equip position
        self.traits = traits  # Any additional traits attached to the equipment
        self.stats = stats  # Stats changed by the equipment and by how much


# Define item class
class Item:

    def __init__(self, name: str, item_id: int, value: int, traits: list):
        self.name = name  # Item name
        self.item_id = item_id  # ID used to manage items
        self.value = value  # Base price for the item
        self.traits = traits  # List of traits the item has


# Define location class
class Location:

    def __init__(self, name: str, coords: list, faction: tuple,
                 will_buy: list, selling: list):
        self.name = name  # Location name
        self.coords = coords  # X and Y coordinates for the location
        self.faction = faction  # Location primary faction

        self.will_buy = will_buy  # List of item IDs this location will buy
        self.selling = selling  # List of item IDs this location can sell


# Define Sailor class
class Sailor:

    def __init__(self, first_name: str, last_name: str, ship_role: str,
                 faction: tuple, is_spy: bool, hit_point_max: int,
                 veils: int, mirrors: int):
        # Sailor's first name
        self.first_name = first_name
        # Sailor's last name
        self.last_name = last_name
        # Their job on the ship
        self.ship_role = ship_role
        # The faction their allegiance is primarily given to
        self.faction = faction
        # Whether or not they are a spy
        self.is_spy = is_spy
        # Hit points indicate whether or not the sailor is dead
        self.hit_point_max = hit_point_max
        self.hit_points = self.hit_point_max
        # Veils are used for deception and cunning
        self.veils = veils
        # Mirrors are used for navigation and perception
        self.mirrors = mirrors

        self.inventory = []


# Define Ship class
class Ship:

    def __init__(self, name: str, ship_class: str, faction: tuple,
                 max_hull: int, cargo_space: int, equip_positions: list,
                 weight: int, fuel_rate, speed):
        # The name of the ship
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
        # A ship's weight affects its speed
        self.weight = weight
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
