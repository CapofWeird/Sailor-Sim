"""This file handles coordinates, travel, and distance between points"""

from math import atan2, degrees, pow, sqrt


def get_slope(current_pos, dest_pos):
    """Find the slope between the ship's current
       position and the given destination"""
    return (current_pos[1] - dest_pos[1]) / (current_pos[0] - dest_pos[0])


def get_dist_to_dest(current_pos, dest_pos):
    """Find the distance between the ship and the given destination"""
    return sqrt(pow((dest_pos[1] - current_pos[1]), 2)
                + pow((dest_pos[0] - current_pos[0]), 2))


def get_angle_to_dest(current_pos, dest_pos):
    """Find the direction in degrees to point the
       ship towards the given destination"""
    angle = degrees(atan2((dest_pos[1] - current_pos[1]),
                          (dest_pos[0] - current_pos[0])))
    if angle < 0:
        angle += 360
    return angle


def get_time_to_dest(current_pos, dest_pos, ship_speed):
    """Find the time in hours to get to the given destination"""
    return get_dist_to_dest(current_pos, dest_pos) / ship_speed


# Move the ship
# def move_ship():
"""
The idea is to get the distance between the boat and the
destination and then take the speed of the boat to calculate how long
it will take to reach the destination.
Then, we'll take how many minutes to reach the destination and plot
out that many points between the ship and the destination. A loop will
move the ship to the next point each minute, with a chance for events
to happen in the mean time.
"""


def plot_path(current_pos, dest_pos, ship_speed) -> list:
    """Find the path of points to get to the given destination"""

    # The list of the distances each point will be from the boat
    point_distances = []
    # The given distance divided by the whole
    # distance between the ship and the destination
    dist_ratio = []
    # The list that contains all of the
    # coordinates the ship will pass through
    point_path = []

    # Find the distance between the two points and calculate
    # how long (in minutes) it will take to get there
    distance = get_dist_to_dest(current_pos, dest_pos)
    time_to_dest = (distance / ship_speed) * 60

    # Find and list all the distances each point will be at
    for x in range(int(time_to_dest)):
        point_distances.append((distance / (time_to_dest)) * (x + 1))

    # Find and list the distance ratios
    for x in range(int(time_to_dest)):
        dist_ratio.append(point_distances[x] / distance)

    # Find and list the points on the path
    for x in range(int(time_to_dest)):
        point_distance = ((distance / (time_to_dest)) * (x + 1))
        dist_ratio = (point_distance / distance)
        new_x = ((1 - dist_ratio) * current_pos[0]
                 + (dist_ratio * dest_pos[0]))
        new_y = ((1 - dist_ratio) * current_pos[1]
                 + (dist_ratio * dest_pos[1]))
        new_coord = (new_x, new_y)
        point_path.append(new_coord)

    return point_path
