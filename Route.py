from Station import Station

class Route:
    def __init__(self,route_name,stations_list,distance_list):
        self.__route_name = route_name
        self.__stations_list = stations_list
        self.__distance_list = distance_list
        

    @property
    def get_route_name(self):
        return self.__route_name
    @property
    def get_station_route_list(self):
        return self.__station_route_list
    @property
    def get_stations_name(self):
        return [station.get_station_name for station in self.__stations_list]
    @property
    def get_distances(self):
        return self.__distance_list
    @property
    def get_name(self):
        name =  []
        for i in self.__stations_list:
            name.append(i.get_station_name)
        return name
    
    def add_station_to_route(self,*stations):
        for  station in stations:
            self.__station_route_list.append(station)

    #**********************
    def calculate_distance(self, start_station, end_station):
        # หา index ของสถานีต้นทางและปลายทาง
        start_idx = self.get_name.index(start_station)
        end_idx = self.get_name.index(end_station)

        # ตรวจสอบว่าตำแหน่งถูกต้อง
        if start_idx >= end_idx:
            # print(self.get_distances)
            # print(self.get_distances[::-1])
            reverse = self.get_distances[::-1]
            return sum(reverse[end_idx:start_idx])

        # คำนวณระยะทางโดยรวมค่าระยะห่างระหว่างสถานีที่อยู่ระหว่างนั้น
        return sum(self.get_distances[start_idx:end_idx])

    
