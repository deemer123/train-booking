class Seat:
    def  __init__(self,seat_number):
        self.__seat_number = seat_number
        self.__price = None
        self.__status = "release"

    @property
    def get_seat_number(self):
        return self.__seat_number
    @property
    def get_status(self):
        return self.__status
    @property
    def get_price(self):
        return self.__price

    def set_price(self,p):
        self.__price = p
    def reserve_seat(self):
        self.__status = "booked"
    def release_seat(self):
        self.__status = "release"
    