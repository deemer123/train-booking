# from Controller import Controller
from Train import Train
from Carriage import Carriage
from Seat import Seat
from Booking import Booking
from Station import Station
from Route import Route
from Departure import Departure
from Schedule import Schedule
from Member import Member


# control = Controller()

# def get_controller():
#     return control
      
def create_instance(control):
         ##### รถไฟสายเหนือ  #####
         train07 = Train("7","เร็ว")
         train08 = Train("8","ด่วนพิเศษ")
         train09 = Train("9","ด่วนพิเศษ CNR")
         train10 = Train("10","ด่วนพิเศษ CNR")
         train13 = Train("13","ด่วนพิเศษ")
         train14 = Train("10","ด่วนพิเศษ CNR")
         train51 = Train("10","ด่วนพิเศษ CNR")
         train52 = Train("10","ด่วนพิเศษ CNR")
         train102 = Train("10","ด่วนพิเศษ CNR")
         train107 = Train("10","ด่วนพิเศษ CNR")
         train108 = Train("13","ด่วนพิเศษ")
         train109 = Train("109","เร็ว")
         
         
         train51 = Train("51","ด่วน")

         ##### Seat #####
         seat_lst1 = []
         seat_lst2 = []
         seat_lst3 = []
         seat_lst4 = []
         seat_lst5 = []
         seat_lst6 = []
         
         for i in range(75):
            seat = Seat(i+1)
            seat_lst1.append(seat)
         for i in range(75):
            seat = Seat(i+1)
            seat_lst2.append(seat)
         for i in range(75):
            seat = Seat(i+1)
            seat_lst3.append(seat)
         for i in range(75):
            seat = Seat(i+1)
            seat_lst4.append(seat)
         for i in range(75):
            seat = Seat(i+1)
            seat_lst5.append(seat)
         for i in range(75):
            seat = Seat(i+1)
            seat_lst6.append(seat)

         ##### Carriage #####
         car1 = Carriage(1,"1","บชส.76","พัดลม",230)
         car2 = Carriage(2,"2","บนท.ป.40","แอร์",430)
         car3 = Carriage(3,"1","บนอ.ป.24","พัดลม",230)
         car4 = Carriage(4,"2","บชท.48","แอร์",430)


         car5 = Carriage(5,"1","บชส.76","พัดลม",230)
         car6 = Carriage(6,"2","บนท.ป.40","แอร์",430)
         car7 = Carriage(7,"1","บนอ.ป.24","พัดลม",230)
         car8 = Carriage(8,"2","บชท.48","แอร์",430)
         car9 = Carriage(9,"2","บชท.48","แอร์",430)

         car1.assign_seats(seat_lst1)
         car2.assign_seats(seat_lst2)
         car3.assign_seats(seat_lst3)
         car4.assign_seats(seat_lst4)

         car5.assign_seats(seat_lst5)
         car6.assign_seats(seat_lst6)
   

         train07.append_carriage(car1)
         train07.append_carriage(car2)

         train08.append_carriage(car3)
         train08.append_carriage(car4)

         train09.append_carriage(car5)
         train09.append_carriage(car6)



         control.add_train(train07)
         control.add_train(train08)
         control.add_train(train09)
         control.add_carriag(car1)
         control.add_carriag(car2)
         control.add_carriag(car3)
         control.add_carriag(car4)
         control.add_carriag(car5)
         control.add_carriag(car6)
         control.add_carriag(car7)
         control.add_carriag(car8)
         control.add_carriag(car9)


         ##### Station #####
         n0 = Station("สถานีกลางกรุงเทพอภิวัฒน์","เหนือ")
         n01 = Station("ดอนเมือง","เหนือ")
         n02 = Station("รังสิต","เหนือ")
         n03 = Station("อยุธยา","เหนือ")
         n1 = Station("ลพบุรี","เหนือ")
         n2 = Station("พุิษณุโลก","เหนือ")
         n3 = Station("ศิลาอาสน์","เหนือ")
         n4 = Station("เด่นชัย","เหนือ")
         n5 = Station("ขุนตาน","เหนือ")
         n6 = Station("ลำพูน","เหนือ")
         n7 = Station("เชียงใหม่","เหนือ")

         ne1 = Station("สระบุรี","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne2 = Station("ปากช่อง","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne3 = Station("นครราชสีมา","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne4 = Station("ลำปลายมาศ","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne5 = Station("บุรีรัมย์","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne6 = Station("สุรินทร์","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne7 = Station("ศีชรภูมิ","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne8 = Station("อุทุมพรพิสัย","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne9 = Station("ศรัสะเกษ","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne10 = Station("กันทรารมย์","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
         ne11 = Station("อุบลราชธานี","สายตะวันออกเฉียงเหนือ-อุบลราชธานี")

         ne12 = Station("ชุมทางแก่งคอย","สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne13 = Station("ลำนารายณ์","สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne14 = Station("ชุมทางบัวใหญ่","สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne15 = Station("เมืองพล","สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne16 = Station("บ้านไผ่","สายตะวันออกเฉียงเหนือ-หนองคาย" )
         ne17 = Station("ขอนแก่น", "สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne18 = Station("น้ำพอง", "สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne19 = Station("กุมภวาปี","สายตะวันออกเฉียงเหนือ-หนองคาย" )
         ne20 = Station("อุดรธานี", "สายตะวันออกเฉียงเหนือ-หนองคาย")
         ne21 = Station( "หนองคาย","สายตะวันออกเฉียงเหนือ-หนองคาย" )

         s1 = Station("บางบำหรุ","สายใต้" )
         s2 = Station("ศาลายา","สายใต้" )
         s3 = Station("นครปฐม","สายใต้" )
         s4 = Station("ราชบุรี","สายใต้" )
         s5 = Station("เพชรบุรี","สายใต้" )
         s6 = Station("หัวหิน","สายใต้" )
         s7 = Station("ชุมพร", "สายใต้")
         s8 = Station("สุราษฎร์ธานี", "สายใต้")
         s9 = Station("ชุมทางทุ่งสง","สายใต้" )
         s10 = Station("พัทลุง","สายใต้" )
         s11 = Station("ชุมทางหาดใหญ่","สายใต้")
         
         control.add_station(n0)
         control.add_station(n01)
         control.add_station(n02)
         control.add_station(n03)
         control.add_station(n1)
         control.add_station(n2)
         control.add_station(n3)
         control.add_station(n4)
         control.add_station(n5)
         control.add_station(n6)
         control.add_station(n7)


         control.add_station(ne1)
         control.add_station(ne2)
         control.add_station(ne3)
         control.add_station(ne4)
         control.add_station(ne5)
         control.add_station(ne6)
         control.add_station(ne7)
         control.add_station(ne8)
         control.add_station(ne9)
         control.add_station(ne10)
         control.add_station(ne11)

         control.add_station(ne12)
         control.add_station(ne13)
         control.add_station(ne14)
         control.add_station(ne15)
         control.add_station(ne16)
         control.add_station(ne17)
         control.add_station(ne18)
         control.add_station(ne19)
         control.add_station(ne20)
         control.add_station(ne21)
      
         control.add_station(s1)
         control.add_station(s2)
         control.add_station(s3)
         control.add_station(s4)
         control.add_station(s5)
         control.add_station(s6)
         control.add_station(s7)
         control.add_station(s8)
         control.add_station(s9)
         control.add_station(s10)
         control.add_station(s11)

         ##### Route #####
         north_route = Route("สายเหนือ") #  เส้นทางสายเหนือ
         northeas_ubon_route = Route("สายตะวันออกเฉียงเหนือ-อุบลราชธานี") #  เส้นทางสายสายตะวันออกเฉียงเหนือ-อุบล
         northeas_nong_route = Route("สายตะวันออกเฉียงเหนือ-หนองคาย") #  เส้นทางสายสายตะวันออกเฉียงเหนือ-หนองค่ย
         south_route = Route("สายใต้") #  เส้นทางสายสายตะวันออกเฉียงเหนือ-หนองค่ย
         # add station to Route
         north_route.add_station_to_route(n0,n01,n02,n03,n1,n2,n3,n4,n5,n6,n7)
         northeas_ubon_route.add_station_to_route(n0,n01,n02,n03,ne1,ne2,ne3,ne4,ne5,ne6,ne7,ne8,ne9,ne10,ne11)
         northeas_nong_route.add_station_to_route(n0,n01,n02,n03,ne12,ne13,ne14,ne15,ne16,ne17,ne18,ne19,ne20,ne21)
         south_route.add_station_to_route(n0,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11)

         control.add_route(north_route)
         control.add_route(northeas_ubon_route)
         control.add_route(northeas_nong_route)
         control.add_route(south_route)

         ##### Schedule #####
         ##### Departure ##### เที่ยวไป Departure(id,route,Schedule,train)
         d1 = Departure(1,north_route,Schedule("09:05","19:30","15/02/2568"),train07) ## create Departure
         d2 = Departure(2,north_route,Schedule("08:50","18:55","15/02/2568"),train08) 
         d3 = Departure(3,north_route,Schedule("18:40","07:15","15/02/2568"),train09)
         
       

         d1.assign_origin_to_destination_station("สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่") ## assign origin and destination to Departure
         d2.assign_origin_to_destination_station("เชียงใหม่","สถานีกลางกรุงเทพอภิวัฒน์")
         d3.assign_origin_to_destination_station("สถานีกลางกรุงเทพอภิวัฒน์","เชียงใหม่")
         # add Departure to Controller
         control.add_departure(d1)
         control.add_departure(d2)
         control.add_departure(d3)

         # Add Member
         m1 = Member("พัฒนพงศ ร่มเย็น","patta@mail.com","member","0894556552","123456")
         m2 = Member("อนาวั แสง","anawan123@mail.com","member","06666552","147258369")
         control.add_member(m1)
         control.add_member(m2)
        
         
      
         









