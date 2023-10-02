
"Test for the station_by_distance function"

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_station_by_distance():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label_a = "a"
    coord_a = (52.2053, 1.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label_a, coord_a, trange, river, town)
    label_b = "b"
    coord_b = (52.2053, 10.0)
    b = MonitoringStation(s_id, m_id, label_b, coord_b, trange, river, town)
    label_c = "c"
    coord_c = (52.2053, 100.0)
    c = MonitoringStation(s_id, m_id, label_c, coord_c, trange, river, town)


    stations = [c, b, a]
    cambridge_city_centre = (52.2053, 0.1218)
    stations_list = stations_by_distance(stations, cambridge_city_centre)
    
    assert stations_list[0][0] == label_a
    assert stations_list[1][0] == label_b
    assert stations_list[2][0] == label_c
