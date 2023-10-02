import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

"Requirements for Task 2F"
stations = build_station_list()
stations_updated = update_water_levels(stations)

stations_10 = stations_highest_rel_level(stations, 10)


dt = 2
count = 0
for station10 in stations_10:
    for station in stations:
        if station10[0] == station.name:
            dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
            count += 1

            if len(levels) == 0:
                count -= 1
                continue
            
            elif count <= 5:
                t = []
                for date, level in zip(dates, levels):
                    t.append(date)

                plot_water_level_with_fit(station, t, levels, 4)