from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

"Requirements of Task 2G"

stations = build_station_list()
stations_updated = update_water_levels(stations)
risk_stat = stations_level_over_threshold(stations, 1)





low = []
moderate = []
high = []
extreme = []

for station in risk_stat:
    if station[1] < 1.1:
        low.append(station)

    elif station[1] < 1.25:
        moderate.append(station)

    elif station[1] < 1.4:
        high.append(station)

    elif station[1] >= 1.6:
        extreme.append(station)

print ('Low flood risk')
for station in low:
        print(station[0] + ' ' + str(station[1]))

print(' ')

print ('Moderate flood risk')
for station in moderate:
        print(station[0] + ' ' + str(station[1]))

print(' ')

print ('High flood risk')
for station in high:
        print(station[0] + ' ' + str(station[1]))

print(' ')

print ('Severe flood risk')
for station in extreme:
        print(station[0] + ' ' + str(station[1]))
        