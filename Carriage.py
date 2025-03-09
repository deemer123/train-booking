class Carriage:
    def  __init__(self,carriage_id,floor,name,type,price):
        self.__carriage_id = carriage_id
        self.__floor = floor
        self.__name = name
        self.__type = type
        self.__seat = []
        self.__price = price
        self.__status = "release"
        

    @property
    def get_seat(self):
        return self.__seat
    @property
    def get_price(self):
        return self.__price
    @property
    def get_name(self):
        return self.__name
    @property
    def get_type(self):
        return self.__type
    @property
    def get_carriage_id(self):
        return self.__carriage_id
    @property
    def get_floor(self):
        return self.__floor
    
    
    def get_all_seat(self):
        return [seat for seat in self.__seat]
    
    def assign_seats(self,lst):
        self.__seat = lst
        self.set_seat_price(self.__price)

    def set_seat_price(self,price):
        for seat in self.__seat:
            seat.set_price(price)

    def set_available(self):
          pass
     
    def set_fully_booked(self):
          pass

 
    
