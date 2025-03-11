class Schedule:
    def __init__(self,station_name_list):
        self.__station_name_list = station_name_list

    @property
    def get_schedule_train(self):
        return self.__station_name_list
        

