class Station:
    station_id = 0
    def __init__(self,station_name,route=""):
        Station.station_id += 1       
        self.station_id = Station.station_id   
        self.station_name = station_name
  

    @property
    def get_station_name(self):
        return self.station_name
