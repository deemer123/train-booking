from Account import Account
from Member import Member
from Booking import Booking
from Carriage import Carriage
from Departure import Departure
from Payment import Payment
from Route import Route
from Schedule import Schedule
from Seat import Seat
from Station import Station
from Ticket import Ticket
from Train import Train
from Ticket import Ticket
from Instance import create_instance

class Controller:

    is_login = False
    login_account_no = None


    def __init__(self):
        self.__member =    []
        self.__train =     []
        self.__station =   []
        self.__departure = []
        self.__carriag =   []
        self.__route = []
        create_instance(self)
        

    @property
    def get_member_list(self):
        return self.__member
    @property
    def get_train_list(self):
        return self.__train
    @property
    def get_departure_list(self):
        return self.__departure
    @property
    def get_route_list(self):
        return self.__route
    
    def login(self,email,password):
        for member in self.__member:
            if email == member.get_email and password == member.get_password:
                return member
        return None
    
    def logout(self):
        if self.is_login:
            self.is_login = False
            self.login_account_no = None

    def register(self,name,email,phone_number,password):
        self.add_member(Member(name,email,"member",phone_number,password))
        return 'Register Sucess'
    
    @property
    def get_login_member(self):
        for member in self.__member:
            if self.login_account_no == member.get_member_id:
                return member

    def add_member(self,member):
        if isinstance(member, Member):
            self.__member.append(member)
    def add_departure(self,departure):
        if isinstance(departure, Departure):
            self.__departure.append(departure)
    def add_train(self,train):
        if isinstance(train, Train):
            self.__train.append(train)
    def add_station(self,station):
        if isinstance(station, Station):
            self.__station.append(station)
    def add_carriag(self,carriag):
        if isinstance(carriag, Carriage):
            self.__carriag.append(carriag)
    def add_route(self,route):
        if isinstance(route, Route):
            self.__route.append(route)


    def find_member_by_id(self,member_id):
        for member in self.__member:
            if member_id == member.get_member_id:
                return member 
        return "Not Found Member"
    def find_departure_by_id(self,departure_id):
        for departure in self.__departure:
            if departure_id == departure.get_departure_id:
                return departure
        return "Not Found Departure"
    def find_train_by_train_num(self,train_num):
        for train in self.__train:
            if train_num == train.get_train_number:
                return train
        return "Not Found Train"
    def find_carriag_by_id(self,carriag_id):
        for carriag in self.__carriag:
            if carriag_id == carriag.get_carriage_id:
                return carriag
        return "Not Found Carriag"
    

    def search_carriage_by_train_nums(self,train_num):
        train = self.find_train_by_train_num(train_num)
        carriage = train.get_all_carriage()
        return [{"name":car.get_name,"type":car.get_type,"floor":car.get_floor} for car in carriage]
        
    def search_departure_by_origin_destination_data(self,origin_station, destination_station, date):
        departure_lst = []
        for departure in self.__departure:
            if date == departure.get_date:
                if origin_station == departure.get_origin_station and destination_station == departure.get_destination_station:
                    departure_lst.append(departure)
        return departure_lst 
 

    # Booking Ticket method return --> 'sucess','error'
    def booking_ticket(self,member_id,departure_id,train_num,carriage_id,seat_number_list):
        count = 0
        member = self.find_member_by_id(member_id)
        booked_departure = self.find_departure_by_id(departure_id)
        booked_train = self.find_train_by_train_num(train_num)
        booked_carriage = None
        booked_seat = []
        for car in booked_train.get_carriag:
            if carriage_id == car.get_carriage_id:
                booked_carriage = car
        for seat in booked_carriage.get_seat:
            for seat_num in seat_number_list:
                if seat_num == seat.get_seat_number:
                    seat.reserve_seat()
                    booked_seat.append(seat)
        count+=1
        pay = Payment(count,booked_carriage,booked_seat,member)
        pay.processPayment()
        if pay.checkStatus() == 'sucess':
            booking = Booking(member,booked_departure,pay)
            for seat in booked_seat:
                ticket = Ticket(member,booked_departure,booked_carriage,seat)
                ticket.update_attribute()
                booking.ticket_append(ticket)
            member.add_booking(booking)
        return "Book Ticket Sucess"

    def get_all_seat_in_car(self,car_id):
        car = self.find_carriag_by_id(car_id)
        return car.get_all_seat_number_and_status # [[seat_num,status]]
        
    # method that return ticket information by (member_id, booking_id, ticket_id)       
    def ticket_info(self,member_id, booking_id, ticket_id):
        member = self.find_member_by_id(member_id)
        ticket = member.find_ticket_by_id(ticket_id)
        return ticket.return_info()
    
    def get_all_station_name(self):
        return [station.get_station_name for station in self.__station]
    
    def get_stations_name_by_route_name(self,route_name):
        for route in self.__route:
            if route_name == route.get_route_name:
                return route.get_stations_name
    
    def get_booking_member(self):
        member = self.get_login_member
        booking_list = member.get_all_booking
        return booking_list

    def get_ticket_member(self,booking_id):
        member = self.get_login_member
        booking = member.find_booking_by_id(booking_id)
        ticket_list = booking.get_ticket
        return ticket_list

    def cancel_ticket(self,ticket_id):
        member = self.get_login_member
        ticket = member.find_ticket_by_id(ticket_id)
        del ticket
        


# control = Controller()
# print(control.get_route_list)
# member_list = control.get_member_list
# for member in member_list:
#     print(member.get_member_id)
# print(control.booking_ticket(1,1,"7",1,[1]))
# print(control.search_departure_by_origin_destination_data("สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","15/2/2568"))
# print(control.ticket_info(1,1,1))
# # print(control.search_carriage_by_train_nums("7"))
# # print(control.register('naruto','shippuden@email.com','0222222',"123"))
# # print(control.login('shippuden@email.com','123'))
# print(control.get_all_seat_in_car(1))
# print()
# print(control.get_all_seat_in_car(2))







