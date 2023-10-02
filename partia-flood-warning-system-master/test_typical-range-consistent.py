
"Test for the typical_range_consistent function"

from floodsystem.station import MonitoringStation

def test_typical_range_consistent():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.typical_range_consistent() == True
    
    trange_inconsistent = (3.0, 0.0)
    d = MonitoringStation(s_id, m_id, label, coord, trange_inconsistent, river, town)
    assert d.typical_range_consistent() == False

    trange_none = None
    f = MonitoringStation(s_id, m_id, label, coord, trange_none, river, town)
    assert f.typical_range_consistent() == False
