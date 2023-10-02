
"Test for the stations_level_over_threshold function"

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"

    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    a.latest_level = 3.4445

    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    b.latest_level = -2.3

    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    c.latest_level = 4.5

    d = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    d.latest_level = 3.1

    stations = [a, b, c, d]
    over_threshold_list = stations_level_over_threshold(stations, 0.8)

    assert len(over_threshold_list) == 3
    for i in range(len(over_threshold_list)-1):
        assert over_threshold_list[i][1] > 0.8
        assert over_threshold_list[i][1] > over_threshold_list[i+1][1]
