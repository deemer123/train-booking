from Station import Station
from Schedule import Schedule

class Departure:
    def  __init__(self, departure_id, route, schedule, train):
        self.__departure_id = departure_id
        self.__route = route
        self.__schedule = schedule
        self.__train = train
        self.__origin_station = None
        self.__destination_station = None
        
    @property
    def get_departure_id(self):
        return self.__departure_id
    @property
    def get_date(self):
        return self.__schedule.get_date
    @property
    def get_time(self):
        return self.__schedule.get_time
    @property
    def get_train(self):
        return self.__train
    
    @property
    def get_train_number(self):
        return self.__train.get_train_number
    @property
    def get_train_type(self):
        return self.__train.get_train_type
    @property
    def get_departure_time(self):
        return self.__schedule.get_departure_time
    @property
    def get_arrival_time(self):
        return self.__schedule.get_arrival_time
    @property
    def get_origin_station(self):
        return self.__origin_station
    @property
    def get_destination_station(self):
        return self.__destination_station

    def assign_origin_to_destination_station(self,origin,destination):
        self.__origin_station = origin
        self.__destination_station = destination

    # def get_departure_info(self):
    #     departure_time = self.__schedule.get_departure_time
    #     arrival_time = self.__schedule.get_arrival_time
    #     train_num = self.__train.get_train_number
    #     train_type = self.__train.get_train_type
    #     return {"depar-time":departure_time,"arri-time":arrival_time,"train-num":train_num,"train-type":train_type}


 








