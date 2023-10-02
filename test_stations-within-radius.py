from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

stations = build_station_list()
cambridge_centre = (52.2053, 0.1218)



def test_stations_within_radius(r=200):

        # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label_a = "a"
    coord_a = (52.2053, 0.5)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    a = MonitoringStation(s_id, m_id, label_a, coord_a, trange, river, town)
    label_b = "b"
    coord_b = (52.2053, 1.0)
    b = MonitoringStation(s_id, m_id, label_b, coord_b, trange, river, town)
    label_c = "c"
    coord_c = (52.2053, 10.0)
    c = MonitoringStation(s_id, m_id, label_c, coord_c, trange, river, town)


    stations = [a, c, b]
    cambridge_centre = (52.2053, 0.1218)
    
    station_in_r = stations_within_radius(stations, cambridge_centre, r)
    dist = stations_by_distance(stations, cambridge_centre)
    
    within_r = []
    for station in dist:
        if station[2] < r:
            within_r.append(station[0])
        else:
            pass

    assert station_in_r[0] == label_a
    assert station_in_r[1] == label_b
   