from floodsystem.analysis import polyfit

def test_analysis():
    times1 = [0,2,4,6]
    times2 = [50,52,54,56]
    times3 = [10000,10002,10004,10006]
    levels = [10,15,20,25]
    p = 3
    poly1 = polyfit(times1, levels, p)
    poly2 = polyfit(times2, levels, p)
    poly3 = polyfit(times3, levels, p)

    assert poly1 == poly2 == poly3
