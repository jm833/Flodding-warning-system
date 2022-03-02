from floodsystem.warning_system import *
from floodsystem.stationdata import build_station_list

def run():
    data = build_station_list()
    calculate_kvalue(data)
   
    
        

   


if __name__ == "__main__":
    run()

