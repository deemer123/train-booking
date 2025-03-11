from Ticket import Ticket

class Booking:
    booking_id = 400961
    def __init__(self,member,train,carriage,payment,date):
        Booking.booking_id += 1  
        self.__booking_id = Booking.booking_id
        self.__member = member
        self.__train = train
        self.__carriage = carriage
        self.__payment = payment
        self.__date = date
        self.__amount = None
        self.__ticket = []
        self.__status = "release"
    
    @property
    def get_booking_id(self):
        return self.__booking_id
    @property
    def get_ticket(self):
        return self.__ticket
    @property
    def get_train(self):
        return self.__train
    @property
    def get_date(self):
        return self.__date
    
    def ticket_append(self,ticket):
        self.__ticket.append(ticket)

    def get_booking_info(self):
        self.__carriage.get_carriage_id

    

    


    



