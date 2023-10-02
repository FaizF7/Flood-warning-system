# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from floodsystem.utils import sorted_by_key # noqa


def stations_by_distance(stations, p):
    "Sorting monitoring station by distance from coordinate point p"
    
    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("stations must form a list")
    elif type(p) != tuple:
        raise RuntimeError("coordinates must be a tuple")
    
    station_list = []
    for station in stations:
        distance = haversine(p, station.coord)
        
        station_list.append((station.name, station.town, distance))
    station_list = sorted_by_key(station_list, 2)
    return station_list
    

def stations_within_radius(stations, centre, r):
    dist = stations_by_distance(stations, centre)
    #returns list of (station, distance) tuples
    
    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("stations must form a list")
    elif type(centre) != tuple:
        raise RuntimeError("coordinates must be a tuple")
    elif type(r) != float and type(r) != int:
        raise RuntimeError("distance must be a float or an integer")

    stations_in_r = []
    for station in dist:

        if station[2] < r:
            stations_in_r.append(station[0])
            
        else:
            return stations_in_r


def rivers_with_station(stations):
    "Displaying rivers with at least one monitoring station in alphabetical order"

    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("Stations must form a list")

    river_set = set()
    for station in stations:
        if type(station.river) != str:
            raise RuntimeError("River name must be a string")
        else:
            river_set.add(station.river)
    
    river_set = sorted(river_set)
    return river_set

def stations_by_river(stations):
    "Creating a dictionary that maps river names to a list of monitoring stations on the river"

    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("Stations must form a list")

    river_dict = {}
    for river in rivers_with_station(stations):
        station_list = []
        for station in stations:
            if station.river == river:
                station_list.append(station.name)
        station_list = sorted(station_list)
        river_dict[river] = station_list
    
    return river_dict



def rivers_by_station_number(stations, N):
    r_list =  []
    rivers = stations_by_river(stations)

    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("stations must form a list")
    
    elif type(N) != int:
        raise RuntimeError("N must be an integer")


    for  river in rivers:
        station = rivers[river]

        number = len(station)
            
        r_number = (river, number)

        r_list.append(r_number)    
                    
    sorted = sorted_by_key(r_list, 1, reverse = True)

    n = sorted[:N]
    print(n)

    for river in sorted:
        if river[1] == sorted[N-1][1]:
            print(sorted[N-1])
            n.append(river) if river not in n else None

    return (n)