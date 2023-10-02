
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    "Displays list of stations with relative water levels over specified threshold"

    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("stations must form a list")
    elif type(tol) != float and type(tol) != int:
        raise RuntimeError("tolerance must be a numerical value")

    over_threshold_list = []
    for station in stations:
        if station.typical_range_consistent() == True:
            if station.latest_level != None:
                if station.relative_water_level() > tol:
                    over_threshold_list.append((station.name, station.relative_water_level()))
    over_threshold_list_sorted = sorted_by_key(over_threshold_list, 1, reverse=True)
    return over_threshold_list_sorted

def stations_highest_rel_level(stations, N):
    "Displays top N stations according to relative water levels"

    # Checking if the inputs are of the correct type
    if type(stations) != list:
        raise RuntimeError("stations must form a list")
    elif type(N) != int:
        raise RuntimeError("N must be an integer")

    over_threshold_list_sorted = stations_level_over_threshold(stations, 0)
    highest_rel_level = over_threshold_list_sorted[:N]
    return highest_rel_level