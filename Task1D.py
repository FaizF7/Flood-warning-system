
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()
def demo1D_1():
    stations = build_station_list()
    return rivers_with_station(stations)

print("Number of rivers: {}".format(len(rivers_with_station(stations))))
print(demo1D_1()[:10])

def demo1D_2():
    stations = build_station_list()
    return stations_by_river(stations)

print(demo1D_2()["River Aire"])
print(demo1D_2()["River Cam"])
print(demo1D_2()["River Thames"])