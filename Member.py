from Account import Account
from Booking import Booking

class Member(Account):
    member_id = 0
    def __init__(self,name,email,role,phone_number,password):
        super().__init__(name,email,role,phone_number,password)
        Member.member_id += 1
        self.__member_id = Member.member_id      
        self.__booking = [] 
        self.__discount = []  

    @property
    def get_member_id(self):
        return self.__member_id   
    @property
    def get_all_booking(self):
        return self.__booking
    
    def find_booking_by_id(self,booking_id):
        for booking in self.__booking:
            if booking_id == booking.get_booking_id:
                return booking
    def find_ticket_by_id(self, ticket_id):
        for booking in self.__booking:
            for ticket in booking.get_ticket:
                if ticket_id == ticket.get_ticket_id:
                    return ticket

    def add_booking(self,booking):
        if isinstance(booking,Booking):
            self.__booking.append(booking)
        
    
    def bookTicket():
        pass
    def cancelBooking():
        pass
    def changingBooking():
        pass