class Schedule:
    def __init__(self,departure_time,arrival_time,date):
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__date = date

    @property
    def get_date(self):
        return self.__date
    @property
    def get_departure_time(self):
        return self.__departure_time
    @property
    def get_arrival_time(self):
        return self.__arrival_time
    @property
    def get_time(self):
        return f"{self.__departure_time} - {self.__arrival_time}"