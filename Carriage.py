from Seat import Seat
class Carriage:
    carriage_id = 0
    def  __init__(self,name,floor,car_type,seat_type,seat_amount):
        Carriage.carriage_id += 1       
        self.__carriage_id = Carriage.carriage_id 
        self.__name = name
        self.__floor = floor
        self.__car_type = car_type
        self.__seat_type = seat_type
        self.__seat_amount = seat_amount
        self.__seat = []
        self.__status = "release"
        self.generate_seats(seat_amount)
    

    def generate_seats(self, seat_count):
        """สร้างที่นั่งทั้งหมดในตู้โดยสาร"""
        for seat_number in range(1, seat_count + 1):
            self.__seat.append(Seat(seat_number))

    @property
    def get_carriage_id(self):
        return self.__carriage_id
    @property
    def get_seat(self):
        return self.__seat
    @property
    def get_seat_amount(self):
        return self.__seat_amount
    @property
    def get_name(self):
        return self.__name
    @property
    def get_seat_type(self):
        return self.__seat_type
    @property
    def get_type(self):
        return self.__car_type
    @property
    def get_floor(self):
        return self.__floor
    @property
    def get_status(self):
        return self.__status
    @property
    def get_all_seat_number_and_status(self):
        return [[seat.get_seat_number,seat.get_status] for seat in self.__seat]
    
    
    def get_all_seat(self):
        return [seat for seat in self.__seat]
    
    def set_seats_status(self,seat_lst):
        for seat in self.__seat:
            if seat.get_seat_number in seat_lst:
                seat.reserve_seat()
    def set_all_seats_status(self,status):
        for seat in self.__seat:
            if status == "booked":
                seat.reserve_seat()
            elif status == "release":
                seat.release_seat()

                   
    def set_seat_price(self,price):
        for seat in self.__seat:
            seat.set_price(price)

    def set_available(self):
          self.__status = "release"
     
    def set_fully_booked(self):
          self.__status = "booked"
    
    def is_fully_booked(self):
          lst = []
          for seat in self.__seat:
               lst.append(seat.get_status)
          if "release" not in lst:
               return  True
          else:
               return False

 
    
