
"Test for the relative_water_level function"

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def test_relative_water_level():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s.latest_level = 3.4445
    assert round(s.relative_water_level(),5) == 1

    s.latest_level = -2.3
    assert round(s.relative_water_level(),5) == 0

    s.latest_level = (3.4445+(-2.3))/2
    assert round(s.relative_water_level(),5) == 0.5