class Ticket:
    ticket_id = 800568
    def __init__(self,member,train,carriage,seat,origin,destination,date,departure_time,arrival_time,price):
        Ticket.ticket_id += 1
        self.__ticket_id = Ticket.ticket_id  
        self.__member = member
        self.__train = train
        self.__carriage = carriage
        self.__seat = seat
        self.__origin = origin
        self.__destination = destination
        self.__date = date

        self.__member_name = None
        self.__origin_station = None
        self.__destination_station = None
        self.__departure_train_num = None
        self.__departure_type = None
        self.__departure_time = departure_time
        self.__arrival_time= arrival_time
        self.__departure_date = None
        self.__departure_car_floor = None 
        self.__departure_car_name = None
        self.__departure_car_type = None
        self.__departure_seat_num = None
        self.__price = price

    @property
    def get_ticket_id(self):
        return self.__ticket_id
    @property
    def origin_station(self):
        return self.__origin_station
    @property
    def destination_station(self):
        return self.__destination_station
    @property
    def train_num(self):
        return self.__departure_train_num
    @property
    def type(self):
        return self.__departure_type
    @property
    def date(self):
        return self.__departure_date
    @property
    def time(self):
        return self.__departure_time
    @property
    def get_car_id(self):
        return self.__carriage.get_carriage_id
    @property
    def car_floor(self):
        return self.__departure_car_floor
    @property
    def car_name(self):
        return self.__departure_car_name
    @property
    def car_type(self):
        return self.__departure_car_type
    @property
    def seat_num(self):
        return self.__departure_seat_num
    @property
    def price(self):
        return self.__price
    @property
    def departure_time(self):
        return self.__departure_time
    @property
    def arrival_time(self):
        return self.__arrival_time
    @property
    def get_carriage(self):
        return self.__carriage
    @property
    def get_seat(self):
        return self.__seat


    def update_attribute(self):
        self.__origin_station = self.__origin
        self.__destination_station = self.__destination
        self.__departure_train_num = self.__train.get_train_number
        self.__departure_type = self.__train.get_train_type
        self.__departure_date = self.__date
        self.__departure_car_floor = self.__carriage.get_floor
        self.__departure_car_name = self.__carriage.get_name
        self.__departure_car_type = self.__carriage.get_type
        self.__departure_seat_num = self.__seat.get_seat_number
        self.__member_name = self.__member.get_name
  
    
    



    
