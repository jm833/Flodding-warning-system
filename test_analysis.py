from floodsystem.analysis import polyfit
from matplotlib.dates import num2date
import numpy as np
"""
def test_analysis():
    times1 = num2date([0,2,4,6])
    times2 = num2date([50,52,54,56])
    times3 = num2date([10000,10002,10004,10006])
    levels = [10,15,20,25]
    p = 3
    poly1 = polyfit(times1, levels, p)
    poly2 = polyfit(times2, levels, p)
    poly3 = polyfit(times3, levels, p)

    return poly1

test_analysis()
"""
def test_stations_polyfit():
    """test_analysis"""
    #(x-1)^2 
    dates = num2date([7,6,5,4,3,2,1])
    levels = [36,25,16,9,4,1,0]

    p, d0 = polyfit(dates,levels,2)
    assert round(p[2]) == 1
    assert d0 == 1
    
    #(2x-1)^3
    dates = num2date([6,4,3,2])
    levels = [1331,343,125,27]

    p, d0 = polyfit(dates,levels,3)
    assert round(p[3]) == 8
    assert d0 == 2

   