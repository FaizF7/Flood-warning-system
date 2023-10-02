
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def demo2B():
    "Requirements of Task 2B"

    stations = build_station_list()
    stations_updated = update_water_levels(stations)
    return stations_level_over_threshold(stations, 0.8)

for station in demo2B():
        print(station[0] + ' ' + str(station[1]))



