"Test for the inconsistent_typical_range_stations"

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_inconsistent_typical_range_stations():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "stat a"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    
    trange_inconsistent_1 = (3.0, 0.0)
    label="stat b"
    b = MonitoringStation(s_id, m_id, label, coord, trange_inconsistent_1, river, town)
  
    trange_inconsistent_2 = (0.1, 0.0)
    label= "stat c"
    c = MonitoringStation(s_id, m_id, label, coord, trange_inconsistent_2, river, town)

    trange_none = None
    label4="stat d"
    d = MonitoringStation(s_id, m_id, label4, coord, trange_none, river, town)

    stations = [a,c,b,d]

    assert inconsistent_typical_range_stations(stations) == [c, b, d]
