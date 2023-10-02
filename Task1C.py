from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def demo1C():
    "Requirements for Task 1C"
    stations = build_station_list()
    cambridge_centre = (52.2053, 0.1218)

    station_in_r = stations_within_radius(stations, cambridge_centre, 10)
    
    return sorted(station_in_r)

print("Stations within 10km of Cambridge city centre: {}".format(demo1C()))


