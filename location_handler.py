from random import choice, randint
from class_defs import location
from sailor_names import locationNames, allFactions

#Randomly create a new location
def MakeLocale(currentLocales):
    #Generate the location's name
    localeName = choice(locationNames)
    #Make sure the new location isn't already in use
    while (localeName in currentLocales):
        localeName = choice(locationNames)
    #Generate location coordinates
    localeCoords = [randint(-100, 100), randint(-100, 100)]
    #Make sure the coordinates aren't already taken
    while (localeCoords in currentLocales):
        localeCoords = [randint(-100, 100), randint(-100, 100)]
    #Generate location faction
    localeFaction = choice(allFactions)
    #Generate location buy and sell items
    localeBuy = []
    localeSell = []
    locale = location(localeName, localeCoords, localeFaction, localeBuy, localeSell)
    return locale
