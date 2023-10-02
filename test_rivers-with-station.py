
"Test for the rivers_with_station function"

from floodsystem.geo import rivers_with_station
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
    # all three stations have different river names

    test_stations = [b, a, c]
    assert rivers_with_station(test_stations) == ["River X", "River Y", "River Z"]

    test_stations = [c, b, a]
    assert rivers_with_station(test_stations) == ["River X", "River Y", "River Z"]
