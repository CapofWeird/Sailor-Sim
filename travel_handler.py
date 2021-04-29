#This file currently handles travel and distance between points
import math

#Find the slope between the ship's current position and the given destination
def GetSlope(currentPos, destPos):
    return (currentPos[1] - destPos[1]) / (currentPos[0] - destPos[0])

#Find the distance between the ship and the given destination
def GetDistToDest(currentPos, destPos):
    return math.sqrt(math.pow((destPos[1] - currentPos[1]), 2) + math.pow((destPos[0] - currentPos[0]), 2))

#Find the direction in degrees to point the ship towards the given destination
def GetAngleToDest(currentPos, destPos):
    degrees = math.degrees(math.atan2((destPos[1] - currentPos[1]), (destPos[0] - currentPos[0])))
    if degrees < 0:
        degrees += 360
    return degrees

#Find the time in hours to get to the given destination
def GetTimeToDest(currentPos, destPos, shipSpeed):
    return GetDistToDest(currentPos, destPos) / shipSpeed

#Move the ship
#def MoveShip():
    
#Alright so like I'm not braining rn so I'ma just write out the general idea here
#So the idea is to get the distance between the boat and the destination and then
#take the speed of the boat to calculate how long it will take to reach the destination.
#Then, we'll take how many minutes to reach the destination and plot out that many points
#between the ship and the destination. A loop will move the ship to the next point each
#minute, with a chance for events to happen in the mean time.

#Find the path of points to get to the given destination
def PlotPath(currentPos, destPos, shipSpeed):
    pointDistances = [] #The list of the distances each point will be from the boat
    distRatio = [] #The given distance divided by the whole distance between the ship and the destination
    pointPath = [] #The list that contains all of the coordinates the ship will pass through

    #Find the distance between the two points and calculate how long (in minutes) it will take to get there
    distance = GetDistToDest(currentPos, destPos)
    timeToDest = (distance / shipSpeed) * 60

##    #Find and list all the distances each point will be at
##    for x in range(int(timeToDest)):
##	pointDistances.append((distance / (timeToDest)) * (x + 1))

##    #Find and list the distance ratios
##    for x in range(int(timeToDest)):
##        distRatio.append(pointDistances[x] / distance)

    #Find and list the points on the path
    for x in range(int(timeToDest)):
        pointDistance = ((distance / (timeToDest)) * (x + 1))
        distRatio = (pointDistance / distance)
        newX = ((1 - distRatio) * currentPos[0] + (distRatio * destPos[0]))
        newY = ((1 - distRatio) * currentPos[1] + (distRatio * destPos[1]))
        newCoord = (newX, newY)
        pointPath.append(newCoord)
    
    return pointPath
