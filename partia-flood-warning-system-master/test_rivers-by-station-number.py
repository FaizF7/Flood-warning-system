from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    # Creating station 1
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 2
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town"
    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 3
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Z"
    town = "My Town"
    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 4
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Z" #2 stations on Z
    town = "My Town"
    d = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 5
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X" #2 stations on X
    town = "My Town"
    e = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Creating station 6
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River W" #new river
    town = "My Town"
    f = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    

    
    test_stations = [a, b, c, d, e, f]
    assert rivers_by_station_number(test_stations, 1) == [('River X', 2), ('River Z', 2)]
    assert rivers_by_station_number(test_stations, 4) == [('River X', 2), ('River Z', 2), ('River W', 1), ('River Y', 1)]
    assert rivers_by_station_number(test_stations, 4) == rivers_by_station_number(test_stations, 3) # checking that the function continues past N rivers if more than one river has that many stations