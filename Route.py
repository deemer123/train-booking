from Station import Station

class Route:
    def __init__(self,route_name):
        self.__route_name = route_name
        self.__station_route_list = []

    @property
    def get_route_name(self):
        return self.__route_name
    @property
    def get_station_route_list(self):
        return self.__station_route_list
    @property
    def get_stations_name(self):
        return [station.get_station_name for station in self.__station_route_list]
    
    def add_station_to_route(self,*stations):
        for  station in stations:
            self.__station_route_list.append(station)

    
