from Station import Station
from Schedule import Schedule


class Departure:
    departure_id = 0
    def  __init__(self, train, schedule_train, route):
        Departure.departure_id += 1       
        self.__departure_id = Departure.departure_id 
        self.__train = train
        self.__schedule_train = schedule_train
        self.__route = route
    
    
    @property
    def get_schedule(self):
        return  self.__schedule_train
    @property
    def get_train(self):
        return  self.__train
    @property
    def get_route(self):
        return  self.__route
    
    def calculate_ticket_price(self, train_type, seat_type, floor_type, distance):
        base_price_per_km = {
            "เร็ว": 0.5,
            "ด่วนพิเศษ CNR": 1.5,
            "ด่วน": 1.0,
            "ด่วนพิเศษ": 1.1,
            "ด่วนพิเศษดีเซลราง": 1.2
        }

        seat_multiplier = {
            "นั่ง": 1.0,
            "เตียงบน": 1.2,
            "เตียงล่าง": 1.5,
            "นอน": 1.4  # เพิ่มประเภทที่นั่ง "นอน"
        }

        floor_multiplier = {
            "3": 1.0,
            "2": 1.3,
            "1": 1.8
        }

        # ตรวจสอบว่า train_type มีอยู่ในตารางหรือไม่
        if train_type not in base_price_per_km:
            return "ประเภทขบวนรถไฟไม่ถูกต้อง"

        if seat_type not in seat_multiplier:
            return "ประเภทที่นั่งไม่ถูกต้อง"

        if floor_type not in floor_multiplier:
            return "ประเภทชั้นไม่ถูกต้อง"

        # คำนวณราคาพื้นฐาน
        base_price = base_price_per_km[train_type] * distance
        seat_price = seat_multiplier[seat_type] * base_price
        total_price = floor_multiplier[floor_type] * seat_price

        print(f"Base Price: {base_price}")  # ตรวจสอบราคาพื้นฐาน
        print(f"Seat Price: {seat_price}")  # ตรวจสอบราคาตามที่นั่ง
        print(f"Total Price: {total_price}")  # ตรวจสอบราคารวม
      
        return int(total_price)
 








