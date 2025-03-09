from Ticket import Ticket

class Booking:
    booking_id = 0
    def __init__(self,member,departure,payment):
        Booking.booking_id += 1  
        self.__booking_id = Booking.booking_id
        self.__member = member
        self.__departure = departure 
        self.__payment = payment
        self.__ticket = []
        self.__status = ""
    
    @property
    def get_booking_id(self):
        return self.__booking_id
    @property
    def get_ticket(self):
        return self.__ticket
    @property
    def get_departure(self):
        return self.__departure
    
    def ticket_append(self,ticket):
        self.__ticket.append(ticket)

    


    



