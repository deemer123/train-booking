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
        self.__route =     []
        self.__bookings = []
        create_instance(self)
        
    @property
    def get_bookings_list(self):
        return self.__bookings
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
    @property
    def get_login_member(self):
        for member in self.__member:
            if self.login_account_no == member.get_member_id:
                return member
    

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
    
    
    def add_booking(self,booking):
        self.__bookings.append(booking)
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

    def find_booking_by_date(self,date):
        for book in self.__bookings:
            if date == book.get_date:
                return book
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
        for train in self.__train:
            for carriage in train.get_carriage:
                if carriag_id == carriage.get_carriage_id:
                    return carriage
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
    
    def get_booking_member(self):
        member = self.get_login_member
        booking_list = member.get_all_booking
        return booking_list

    def get_ticket_member(self,booking_id):
        member = self.get_login_member
        booking = member.find_booking_by_id(booking_id)
        ticket_list = booking.get_ticket
        return ticket_list

    ## Booking Ticket method return --> 'sucess','error'
    def booked_ticket(self,member_id,train_num,carriage_id,seat_number_list,ori,des,date,price):
        departure_time = None
        arrival_time = None
        for i in self.search_departure(ori,des):
            if i['train_num'] == train_num:
                departure_time = i['departure_time']
                arrival_time = i['arrival_time']
        member = self.find_member_by_id(member_id)
        booked_train = self.find_train_by_train_num(train_num)
        booked_carriage = self.find_carriag_by_id(carriage_id)
        booked_seat = []
        for seat in booked_carriage.get_seat:
            for seat_num in seat_number_list:
                if seat_num == seat.get_seat_number:
                    seat.reserve_seat()
                    booked_seat.append(seat)
        pay = Payment(1,booked_carriage,booked_seat,member)
        pay.processPayment()
        if pay.checkStatus() == 'sucess':
            booking = Booking(member,booked_train,booked_carriage,pay,date)
            for seat in booked_seat:
                ticket = Ticket(member,booked_train,booked_carriage,seat,ori,des,date,departure_time,arrival_time,price)
                ticket.update_attribute()
                booking.ticket_append(ticket)
            member.add_booking(booking)
            return booking
       


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
    
    

    def cancel_ticket(self,ticket_id):
        member = self.get_login_member

        ticket = member.find_ticket_by_id(ticket_id)
        seat = ticket.get_seat
        seat.release_seat()
        member.remove_ticket(ticket_id)
        member.remove_booking()
        return seat.get_status
    
    def search_departure(self, source, destination, date=""):
        match_departure = []
        for departure in self.__departure:
            schedule = departure.get_schedule
            train = departure.get_train
            schedule_train = schedule.get_schedule_train
            source_index = -1
            destination_index = -1

            # ค้นหาดัชนีของสถานีต้นทางและปลายทาง
            for i in range(len(schedule_train)):
                if schedule_train[i][0] == source:
                    source_index = i
                if schedule_train[i][0] == destination:
                    destination_index = i

            # ตรวจสอบว่าพบสถานีต้นทางและปลายทางในตารางเวลา
            if source_index != -1 and destination_index != -1 and source_index < destination_index:
                departure_time = schedule_train[source_index][1]
                arrival_time = schedule_train[destination_index][1]
                train_num = train.get_train_number
                train_type = train.get_train_type

                match_departure.append({
                    "departure_time": departure_time,
                    "arrival_time": arrival_time,
                    "train_num": train_num,
                    "train_type": train_type
                })
        return match_departure
    

    def show_carriage(self, train_num, source, destination):
        all_carriages = []  # สร้างลิสต์เพื่อเก็บข้อมูลโบกี้

        for departure in self.__departure:
            train = departure.get_train  # ดึงข้อมูลขบวนรถไฟ
            route = departure.get_route  # ดึงเส้นทางการเดินทาง

            # ตรวจสอบว่าหมายเลขขบวนรถไฟตรงกับที่ระบุ
            if train_num == train.get_train_number:
                distance = route.calculate_distance(source, destination)  # คำนวณระยะทาง

                # วนลูปดึงข้อมูลโบกี้แต่ละอัน
                for carriage in train.get_carriage:
                    if carriage.is_fully_booked():
                        carriage.set_fully_booked()
                    else:
                        carriage.set_available()
                    # คำนวณราคาตั๋วสำหรับโบกี้นั้น ๆ
                    price = departure.calculate_ticket_price(
                        train.get_train_type,
                        carriage.get_seat_type,
                        carriage.get_floor,
                        distance
                    )

                    # เพิ่มข้อมูลโบกี้พร้อมรายละเอียดลงในลิสต์
                    all_carriages.append({
                        "carrige_id": carriage.get_carriage_id,
                        "carrige_name": carriage.get_name,
                        "seat_type": carriage.get_seat_type,
                        "room_type": carriage.get_type,
                        "floor": carriage.get_floor,
                        "status": carriage.get_status,
                        "price": price,  # เพิ่มราคาที่คำนวณแล้ว
                    })

        return all_carriages  # คืนค่าข้อมูลโบกี้ทั้งหมด
    


# con = Controller()
# member = con.login("anawan123@mail.com","147258369")
# mem_id = member.get_member_id
# con.booked_ticket(mem_id,"7",164,[1,2],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-03-11",1134)
       
    


        
        


