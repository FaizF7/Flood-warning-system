
"Test for the function stations_highest_rel_level"

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_highest_rel_level():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label_a = "a"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label_a, coord, trange, river, town)
    a.latest_level = 3.0
    label_b = "b"
    b = MonitoringStation(s_id, m_id, label_b, coord, trange, river, town)
    b.latest_level = 3.2
    label_c = "c"
    c = MonitoringStation(s_id, m_id, label_c, coord, trange, river, town)
    c.latest_level = 3.4
    label_d = "d"
    d = MonitoringStation(s_id, m_id, label_d, coord, trange, river, town)
    d.latest_level = 3.6
    label_e = "e"
    e = MonitoringStation(s_id, m_id, label_e, coord, trange, river, town)
    e.latest_level = 3.8

    stations = [a, b, c, d, e]
    highest_rel_list = stations_highest_rel_level(stations, 3)

    assert len(highest_rel_list) == 3
    assert highest_rel_list[0][0] == label_e
    assert highest_rel_list[1][0] == label_d
    assert highest_rel_list[2][0] == label_c

    