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
        self.__tickets = []
        self.__status = "release"
    
    @property
    def get_booking_id(self):
        return self.__booking_id
    @property
    def get_ticket(self):
        return self.__tickets
    @property
    def get_train(self):
        return self.__train
    @property
    def get_date(self):
        return self.__date
    @property
    def get_car_id(self):
        return self.__carriage.get_carriage_id
    
    def ticket_append(self,ticket):
        self.__tickets.append(ticket)


    def get_booking_car_and_seat_id(self):
        car_id = None
        seats_num_list = []
        for ticket in self.__tickets:
            car_id = ticket.get_car_id
            seats_num_list.append(ticket.seat_num)
        return {
            "car_id":car_id,
            "seats":seats_num_list
        }

    

    


    



