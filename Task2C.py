
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def demo2C():
    "Requirements of Task 2C"

    stations = build_station_list()
    stations_updated = update_water_levels(stations)
    return stations_highest_rel_level(stations, 10)

for station in demo2C():
        print(station[0] + ' ' + str(station[1]))
