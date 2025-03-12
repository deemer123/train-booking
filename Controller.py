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
        return [book for book in self.__bookings if date == book.get_date]
    
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
            self.add_booking(booking)
            member.add_booking(booking)
            return booking
        
    
    def get_all_station_name(self):
        return [station.get_station_name for station in self.__station]
    
    def get_stations_name_by_route_name(self,route_name):
        for route in self.__route:
            if route_name == route.get_route_name:
                return route.get_stations_name
            
    def get_seat_data(self,carriage_id,train_num):
        carriage = self.find_carriag_by_id(int(carriage_id))
        train = self.find_train_by_train_num(str(train_num))
        carriage_list = train.get_all_carriage()
        carriage_num = None
        for i,car in enumerate(carriage_list):
            if carriage == car:
                carriage_num = i+1
        seats_list = carriage.get_all_seat()
        return {
            "carriage":carriage,
            "carriage_num":carriage_num,
            "train":train,
            "seats_list":seats_list
        }
    

    def cancel_ticket(self,ticket_id):
        member = self.get_login_member
        ticket = member.find_ticket_by_id(ticket_id)
        seat = ticket.get_seat
        seat.release_seat()
        member.remove_ticket(ticket_id)
        member.remove_booking()
        return seat.get_status
    

    def search_departure(self, source, destination,date=""):
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
    

    def show_carriage(self, train_num, source, destination, date):
        all_carriages = []  # สร้างลิสต์เพื่อเก็บข้อมูลโบกี้
        # booked_list = self.find_booking_by_date(date)
        for departure in self.__departure:
            train = departure.get_train  # ดึงข้อมูลขบวนรถไฟ
            route = departure.get_route  # ดึงเส้นทางการเดินทาง

            # ตรวจสอบว่าหมายเลขขบวนรถไฟตรงกับที่ระบุ
            if train_num == train.get_train_number:
                distance = route.calculate_distance(source, destination)  # คำนวณระยะทาง
                # วนลูปดึงข้อมูลโบกี้แต่ละอัน
                for carriage in train.get_carriage:
                    # คำนวณราคาตั๋วสำหรับโบกี้นั้น ๆ
                    price = departure.calculate_ticket_price(
                        train.get_train_type,
                        carriage.get_seat_type,
                        carriage.get_floor,
                        distance
                    )
                    date_booked_list = self.find_booking_by_date(date)
                    car_booked_list = [book for book in date_booked_list if book.get_car_id == carriage.get_carriage_id]
                    booked_seat = []
                    
                    # ตรวจสอบการจองของวันนั้นว่ามีการจองหรือไม่
                    if date_booked_list == [] or car_booked_list == []: # กรณีวันนี้-ตู้นี้ยังไม่มีการจอง
                        carriage.set_available()
                        carriage.set_all_seats_status("release")
                    else:                                               # กรณีวันนี้-ตู้นี้มีการจอง
                        for booked in car_booked_list:
                            lst_car_attribute = booked.get_booking_car_and_seat_id()
                            booked_seat += lst_car_attribute['seats']
                        if len(booked_seat) == carriage.get_seat_amount:    # กรณีวันนี้-ตู้นี้มีการจองที่นั่งเต็ม
                            carriage.set_fully_booked()
                            carriage.set_all_seats_status("booked")
                        else:
                            carriage.set_all_seats_status("release")        # กรณีวันนี้-ตู้นี้มีการจองบางที่นั่ง
                            carriage.set_seats_status(booked_seat)       

                    # เพิ่มข้อมูลโบกี้พร้อมรายละเอียดลงในลิสต์
                    all_carriages.append({
                        "seat": carriage.get_all_seat_number_and_status,
                        "carrige_id": carriage.get_carriage_id,
                        "carrige_name": carriage.get_name,
                        "seat_type": carriage.get_seat_type,
                        "room_type": carriage.get_type,
                        "floor": carriage.get_floor,
                        "status": carriage.get_status,
                        "price": price,  # เพิ่มราคาที่คำนวณแล้ว
                    })
        return all_carriages  # คืนค่าข้อมูลโบกี้ทั้งหมด
    
    # เซ็ตที่นั่งตาม "วัน" ที่รับมาว่ามีการจองที่นั่งหรือไม่ในระบบ
    def set_seat_booked(self,date,car_id):
        date_booked_list = self.find_booking_by_date(date)
        carriage = self.find_carriag_by_id(car_id)
        car_booked_list = [book for book in date_booked_list if book.get_car_id == carriage.get_carriage_id]
        booked_seat = []
        # ตรวจสอบการจองของวันนั้นว่ามีการจองหรือไม่
        if date_booked_list == [] or car_booked_list == []: # กรณีวันนี้-ตู้นี้ยังไม่มีการจอง
            carriage.set_available()
            carriage.set_all_seats_status("release")
        else:                                               # กรณีวันนี้-ตู้นี้มีการจอง
            for booked in car_booked_list:
                lst_car_attribute = booked.get_booking_car_and_seat_id()
                booked_seat += lst_car_attribute['seats']
            if len(booked_seat) == carriage.get_seat_amount:    # กรณีวันนี้-ตู้นี้มีการจองที่นั่งเต็ม
                carriage.set_fully_booked()
                carriage.set_all_seats_status("booked")
            else:
                carriage.set_all_seats_status("release")
                carriage.set_seats_status(booked_seat) 
    
    
#### Test App ############

# con = Controller()
# member = con.login("anawan123@mail.com","147258369")
# mem_id = member.get_member_id
# booking = con.booked_ticket(mem_id,"7",1,[1,2],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-03-11",1134)
# booking = con.booked_ticket(mem_id,"7",1,[3,4],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-04-11",1134)
# booking = con.booked_ticket(mem_id,"7",1,[5,6],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-03-11",1134)
# booking2 = con.booked_ticket(mem_id,"9",2,[3,4],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-03-11",1134)
# booking2 = con.booked_ticket(mem_id,"9",2,[3,4],"สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-02-11",1134)
# train_9 = con.find_train_by_train_num("9")
# carriage = train_9.get_carriage
# print(carriage[0].get_carriage_id)
# print(con.get_bookings_list)
# print(con.find_booking_by_date("2025-03-11"))
# print(booking2.get_booking_car_and_seat_id())
# print(con.show_carriage("7","สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-03-11"))
# print()
# print(con.show_carriage("7","สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-04-11"))
# print()
# con.show_carriage("9","สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่","2025-02-11")
# print(train_9.get_carriage)
# booked_list = con.find_booking_by_date("2025-03-11")

# def set_seat_booked(date,car_id):
#     date_booked_list = self.find_booking_by_date(date)
#     carriage = con.find_carriag_by_id(car_id)
#     car_booked_list = [book for book in date_booked_list if book.get_car_id == carriage.get_carriage_id]
#     booked_seat = []
#     # ตรวจสอบการจองของวันนั้นว่ามีการจองหรือไม่
#     if date_booked_list == [] or car_booked_list == []: # กรณีวันนี้-ตู้นี้ยังไม่มีการจอง
#         carriage.set_available()
#         carriage.set_all_seats_status("release")
#     else:                                               # กรณีวันนี้-ตู้นี้มีการจอง
#         for booked in car_booked_list:
#             lst_car_attribute = booked.get_booking_car_and_seat_id()
#             booked_seat += lst_car_attribute['seats']
#         if len(booked_seat) == carriage.get_seat_amount:    # กรณีวันนี้-ตู้นี้มีการจองที่นั่งเต็ม
#             carriage.set_fully_booked()
#             carriage.set_all_seats_status("booked")
#         else:
#             carriage.set_all_seats_status("release")
#             carriage.set_seats_status(booked_seat) 








    



    
# set_seat_booked("2025-03-11",1)
        


