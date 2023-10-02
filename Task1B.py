
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def demo1B():
    "Requirements for Task 1B"
    stations = build_station_list()
    cambridge_city_centre = (52.2053, 0.1218)
    return stations_by_distance(stations, cambridge_city_centre)

print("Closest 10 stations: {}".format(demo1B()[:10]))
print("Furthest 10 stations: {}".format(demo1B()[-10:]))
