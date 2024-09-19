import algebra 
import rest_api_server
import math

def test_area_circle():
    area = algebra.area_circle(10)
    assert math.isclose(area, 314.15926535897932)

