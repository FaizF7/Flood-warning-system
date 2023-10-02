import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

def test_plot_water_level_with_fit ():
    stations = build_station_list()    
    stations_updated = update_water_levels(stations)

    dt = 5
    for station in stations:
        if station.name == 'Cam':
            dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))

            
            t = []
            for date, level in zip(dates, levels):
                t.append(date)

            plot_water_level_with_fit(station, t, levels, 6)