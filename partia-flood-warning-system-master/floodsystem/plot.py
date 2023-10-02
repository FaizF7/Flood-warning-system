import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib


def plot_water_levels(station, dates, levels):
    if type(dates) != list:
        raise RuntimeError("dates must form a list")
    if type(levels) != list:
        raise RuntimeError("levels must form a list")
    l_list = []
    h_list = []

    for date in dates:
        l = station.typical_range[0]
        h = station.typical_range[1]

        l_list.append(l)
        h_list.append(h)

    dates = matplotlib.dates.date2num(dates)

    plt.plot(dates, levels, label="levels")
    plt.plot(dates, h_list, label="typical high")
    plt.plot(dates, l_list, label="typical low")
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    if type(dates) != list:
        raise RuntimeError("dates must form a list")
    if type(levels) != list:
        raise RuntimeError("levels must form a list")
    if type(p) != int:
        raise RuntimeError("p must be an integer")

    l_list = []
    h_list = []

    for date in dates:
        l = station.typical_range[0]
        h = station.typical_range[1]

        l_list.append(l)
        h_list.append(h)


    poly, d0 = polyfit(dates, levels, p)

    # Plot polynomial fit at 100 points along interval (note that polynomial
    # is evaluated using the shift x)

    x = np.linspace(0, d0, 100)
    
    x_dec = matplotlib.dates.date2num(dates)
    x_decs = sorted(x_dec)
    plt.plot(x_dec - x_decs[0], levels, label="levels")
    plt.plot(x, poly(x), label="polynomial")
    plt.plot(x_dec - x_decs[0], h_list, label="typical high")
    plt.plot(x_dec - x_decs[0], l_list, label="typical low")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()