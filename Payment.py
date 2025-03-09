class Payment:
    def __init__(self,payment_id,carriage,seat,member):
        self.__payment_id = payment_id
        self.__booking = None
        self.__member = member
        self.__carriage = carriage
        self.__amount = None
        self.__status = None
        self.__seat = seat
                   
    def processPayment(self):
        self.__amount = sum([float(seat.get_price) for seat in self.__seat])
        # self.__amount = self.__seat.get_price
        self.__status = 'sucess'

    def checkStatus(self):
        if self.__status == 'sucess':
            return 'sucess'