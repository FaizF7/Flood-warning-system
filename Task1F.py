from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


stations = build_station_list()

def demo_1F():
    "Requirements for Task1F"
    inconsistent = inconsistent_typical_range_stations(stations)
    
    Name = []
    for station in inconsistent:
        name = station.name
        Name.append(name)

    return sorted(Name)

print(demo_1F())
