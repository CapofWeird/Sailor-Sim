from random import choice, randint

from class_defs import Location
from sailor_names import locationNames, allFactions


def coord_flavor(coords: list) -> str:
    """Take a coordinate and return it as a string.

       Ex. (-15, 22) returns '15°S, 22°E'
    """
    if coords[0] < 0:
        latitude = 'S'
        coords[0] *= -1
    else:
        latitude = 'N'

    if coords[1] < 0:
        longitude = 'W'
        coords[1] *= -1
    else:
        longitude = 'E'

    return ("%d°%c, %d°%c" % (coords[0], latitude, coords[1], longitude))


def make_locale(current_locales: list) -> Location:
    """Randomly create a new location
    """
    # Generate the location's name
    locale_name = choice(locationNames)
    # Make sure the new location isn't already in use
    while (locale_name in current_locales):
        locale_name = choice(locationNames)
    # Generate location coordinates
    locale_coords = [randint(-100, 100), randint(-100, 100)]
    # Make sure the coordinates aren't already taken
    while (locale_coords in current_locales):
        locale_coords = [randint(-100, 100), randint(-100, 100)]
    # Generate location faction
    locale_faction = choice(allFactions)
    # Generate location buy and sell items
    locale_buy = []
    locale_sell = []
    locale = Location(locale_name, locale_coords, locale_faction, locale_buy,
                      locale_sell)
    return locale
