
"Test for the stations_by_river function"

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation

def test_stations_by_river():
    # Creating station 1
    s_id = "test-s-id-1"
    m_id = "test-m-id"
    label = "station 1"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 2
    s_id = "test-s-id-2"
    m_id = "test-m-id"
    label = "station 2"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X" # same river as station 1
    town = "My Town"
    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 3
    s_id = "test-s-id-3"
    m_id = "test-m-id"
    label = "station 3"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Z"
    town = "My Town"
    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    # all stations have different names

    test_stations = [c, b, a]
    assert type(stations_by_river(test_stations)) == dict
    assert stations_by_river(test_stations)['River Z'] == ['station 3']
    assert stations_by_river(test_stations)['River X'] == ['station 1', 'station 2']