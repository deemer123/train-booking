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
            ###### V2 ###################################################
            c1 = Station("สถานีกลางกรุงเทพอภิวัฒน์",)
            c2 = Station("ดอนเมือง",)
            c3 = Station("รังสิต",)   
            c4 = Station("อยุธยา",)
            n1 = Station("ลพบุรี",)
            n2 = Station("นครสวรรค์")
            n3 = Station("พิษณุโลก",)
            n4 = Station("ศิลาอาสน์",)
            n5 = Station("เด่นชัย",)
            n6 = Station("นครลำปาง")
            n7 = Station("ขุนตาน",)
            n8 = Station("ลำพูน",)
            n9 = Station("เชียงใหม่",)

            ne1 = Station("สระบุรี",)
            ne2 = Station("ปากช่อง",)
            ne3 = Station("นครราชสีมา",)
            ne4 = Station("ลำปลายมาศ",)
            ne5 = Station("บุรีรัมย์",)
            ne6 = Station("สุรินทร์",)
            ne7 = Station("ศีชรภูมิ",)
            ne8 = Station("อุทุมพรพิสัย",)
            ne9 = Station("ศรัสะเกษ",)
            ne10 = Station("กันทรารมย์",)
            ne11 = Station("อุบลราชธานี",)

            ne12 = Station("ชุมทางแก่งคอย", )
            ne13 = Station("ลำนารายณ์", )
            ne14 = Station("ชุมทางบัวใหญ่", )
            ne15 = Station("เมืองพล", )
            ne16 = Station("บ้านไผ่", )
            ne17 = Station("ขอนแก่น", )
            ne18 = Station("น้ำพอง", )
            ne19 = Station("กุมภวาปี", )
            ne20 = Station("อุดรธานี", )
            ne21 = Station( "หนองคาย", )

            s1 = Station("บางบำหรุ", )
            s2 = Station("ศาลายา", )
            s3 = Station("นครปฐม", )
            s4 = Station("ราชบุรี", )
            s5 = Station("เพชรบุรี", )
            s6 = Station("หัวหิน", )
            s7 = Station("ชุมพร", )
            s8 = Station("สุราษฎร์ธานี", )
            s9 = Station("ชุมทางทุ่งสง", )
            s10 = Station("พัทลุง", )
            s11 = Station("ชุมทางหาดใหญ่", )

            control.add_station(c1)
            control.add_station(c2)
            control.add_station(c3)
            control.add_station(c4)
            control.add_station(n1)
            control.add_station(n2)
            control.add_station(n3)
            control.add_station(n4)
            control.add_station(n5)
            control.add_station(n6)
            control.add_station(n7)
            control.add_station(n8)
            control.add_station(n9)


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
            
            north = [c1, c2, c3, c4, n1, n2, n3, n4, n5, n6, n7, n8, n9]
            northeast_ubon = [c1, c2, c3, c4, ne1, ne2, ne3, ne4, ne5, ne6, ne7, ne8, ne9, ne10, ne11]
            northeast_nongkuy = [c1, c2, c3, c4, n1, ne12, ne13, ne14, ne15, ne16, ne17, ne18, ne19, ne20, ne21]
            south = [c1, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
            
            schedule_train07 = Schedule([(north[0].get_station_name, "09.05"), 
                                    (north[1].get_station_name, "09.18"),
                                    (north[2].get_station_name , "09.28"),
                                    (north[3].get_station_name, "09.54"),
                                    (north[4].get_station_name , "10.28"),
                                    (north[5].get_station_name , "11.37"),
                                    (north[6].get_station_name , "13.12"),
                                    (north[7].get_station_name , "14.30"),
                                    (north[8].get_station_name , "15.23"),
                                    (north[9].get_station_name , "17.30"),
                                    (north[10].get_station_name , "18.22"),
                                    (north[11].get_station_name , "19.14"),
                                    (north[12].get_station_name , "19.30")])
            
            schedule_train09 = Schedule([(north[0].get_station_name, "18.40"), 
                                (north[1].get_station_name, "18.55"),
                                (north[2].get_station_name , "19.06"),
                                (north[3].get_station_name, "19.44"),
                                (north[4].get_station_name , "20.41"),
                                (north[5].get_station_name , "22.14"),
                                (north[6].get_station_name , "00.15"),
                                (north[7].get_station_name , "01.44"),
                                (north[8].get_station_name , "02.48"),
                                (north[9].get_station_name , "04.57"),
                                (north[10].get_station_name , "06.01"),
                                (north[11].get_station_name , "06.50"),
                                (north[12].get_station_name , "07.15")])
        
            schedule_train13 = Schedule([(north[0].get_station_name, "20.05",), 
                                    (north[1].get_station_name, "20.20"),
                                    (north[2].get_station_name , "20.31"),
                                    (north[3].get_station_name, "21.06"),
                                    (north[4].get_station_name , "21.58"),
                                    (north[5].get_station_name , "23.28"),
                                    (north[6].get_station_name , "01.47"),
                                    (north[7].get_station_name , "03.11"),
                                    (north[8].get_station_name , "04.16"),
                                    (north[9].get_station_name , "06.30"),
                                    (north[10].get_station_name , "07.32"),
                                    (north[11].get_station_name , "08.19"),
                                    (north[12].get_station_name , "08.40")])
        
        
            schedule_train109 = Schedule([(north[0].get_station_name, "14.15"), 
                                    (north[1].get_station_name, "14.30"),
                                    (north[2].get_station_name , "14.42"),
                                    (north[3].get_station_name, "15.17"),
                                    (north[4].get_station_name , "16.21"),
                                    (north[5].get_station_name , "18.24"),
                                    (north[6].get_station_name , "20.35"),
                                    (north[7].get_station_name , "22.27"),
                                    (north[8].get_station_name , "23.39"),
                                    (north[9].get_station_name , "01.54"),
                                    (north[10].get_station_name , "02.57"),
                                    (north[11].get_station_name , "03.43"),
                                    (north[12].get_station_name , "04.05")])
            

            schedule_train51 = Schedule([(north[0].get_station_name, "20.30"), 
                                    (north[1].get_station_name, "22.45"),
                                    (north[2].get_station_name , "22.58"),
                                    (north[3].get_station_name, "23.35"),
                                    (north[4].get_station_name , "00.27"),
                                    (north[5].get_station_name , "02.21"),
                                    (north[6].get_station_name , "04.37"),
                                    (north[7].get_station_name , "06.10"),
                                    (north[8].get_station_name , "07.17"),
                                    (north[9].get_station_name , "09.51"),
                                    (north[10].get_station_name , "11.00"),
                                    (north[11].get_station_name , "11.48"),
                                    (north[12].get_station_name , "12.10")])
            
            schedule_train111 = Schedule([(north[0].get_station_name, "07.30"), 
                                    (north[1].get_station_name, "07.45"),
                                    (north[2].get_station_name , "07.57"),
                                    (north[3].get_station_name, "08.27"),
                                    (north[4].get_station_name , "09.42"),
                                    (north[5].get_station_name , "11.21"),
                                    (north[6].get_station_name , "13.43"),
                                    (north[7].get_station_name , "15.27"),
                                    (north[8].get_station_name , "16.30"),])
            
            schedule_train107 = Schedule([(north[0].get_station_name, "20.45"),
                                    (north[1].get_station_name, "21.00"),
                                    (north[2].get_station_name , "02.30"),
                                    (north[3].get_station_name , "21.47"),
                                    (north[4].get_station_name, "22.38"),
                                    (north[5].get_station_name , "00.04"),
                                    (north[6].get_station_name , "02.36"),
                                    (north[7].get_station_name , "04.08"),
                                    (north[8].get_station_name , "05.15")])
            
            
            # add schedule northes ubon
            schedule_train21 = Schedule([(northeast_ubon[0].get_station_name, "06.10"), 
                                    (northeast_ubon[1].get_station_name, "06.25"),
                                    (northeast_ubon[2].get_station_name , "06.36"),
                                    (northeast_ubon[3].get_station_name, "06.58"),
                                    (northeast_ubon[4].get_station_name , "07.33"),
                                    (northeast_ubon[5].get_station_name , "08.52"),
                                    (northeast_ubon[6].get_station_name , "10.21"),
                                    (northeast_ubon[7].get_station_name , "11.13"),
                                    (northeast_ubon[8].get_station_name , "11.34"),
                                    (northeast_ubon[9].get_station_name , "12.09"),
                                    (northeast_ubon[10].get_station_name , "12.32"),
                                    (northeast_ubon[11].get_station_name , "13.01"),
                                    (northeast_ubon[12].get_station_name , "13.18"),
                                    (northeast_ubon[13].get_station_name , "13.38"),
                                    (northeast_ubon[14].get_station_name , "14.00"),])
            
            schedule_train135 = Schedule([(northeast_ubon[0].get_station_name, "07.10"), 
                                    (northeast_ubon[1].get_station_name, "07.25"),
                                    (northeast_ubon[2].get_station_name , "07.38"),
                                    (northeast_ubon[3].get_station_name, "08.27"),
                                    (northeast_ubon[4].get_station_name , "09.17"),
                                    (northeast_ubon[5].get_station_name , "10.52"),
                                    (northeast_ubon[6].get_station_name , "12.12"),
                                    (northeast_ubon[7].get_station_name , "13.47"),
                                    (northeast_ubon[8].get_station_name , "14.19"),
                                    (northeast_ubon[9].get_station_name , "15.07"),
                                    (northeast_ubon[10].get_station_name , "15.40"),
                                    (northeast_ubon[11].get_station_name , "16.34"),
                                    (northeast_ubon[12].get_station_name , "17.00"),
                                    (northeast_ubon[13].get_station_name , "17.26"),
                                    (northeast_ubon[14].get_station_name , "18.00"),])
            

            schedule_train71 = Schedule([(northeast_ubon[0].get_station_name, "10.35"), 
                                    (northeast_ubon[1].get_station_name, "10.50"),
                                    (northeast_ubon[2].get_station_name , "11.01"),
                                    (northeast_ubon[3].get_station_name , "11.30"),
                                    (northeast_ubon[4].get_station_name, "12.05"),
                                    (northeast_ubon[5].get_station_name , "13.25"),
                                    (northeast_ubon[6].get_station_name , "14.27"),
                                    (northeast_ubon[7].get_station_name , "15.50"),
                                    (northeast_ubon[8].get_station_name , "16.14"),
                                    (northeast_ubon[9].get_station_name , "17.08"),
                                    (northeast_ubon[10].get_station_name , "17.38"),
                                    (northeast_ubon[11].get_station_name , "18.18"),
                                    (northeast_ubon[12].get_station_name , "18.40"),
                                    (northeast_ubon[13].get_station_name , "19.07"),
                                    (northeast_ubon[14].get_station_name , "19.50"),
                                    ])
            
            schedule_train139 = Schedule([(northeast_ubon[0].get_station_name, "19.25"), 
                                    (northeast_ubon[1].get_station_name, "19.39"),
                                    (northeast_ubon[2].get_station_name , "19.51"),
                                    (northeast_ubon[3].get_station_name , "20.25"),
                                    (northeast_ubon[4].get_station_name, "21.09"),
                                    (northeast_ubon[5].get_station_name , "22.46"),
                                    (northeast_ubon[6].get_station_name , "00.07"),
                                    (northeast_ubon[7].get_station_name , "01.47"),
                                    (northeast_ubon[8].get_station_name , "02.22"),
                                    (northeast_ubon[9].get_station_name , "03.15"),
                                    (northeast_ubon[10].get_station_name , "03.53"),
                                    (northeast_ubon[11].get_station_name , "04.44"),
                                    (northeast_ubon[12].get_station_name , "05.07"),
                                    (northeast_ubon[13].get_station_name , "05.38"),
                                    (northeast_ubon[14].get_station_name , "06.15"),
                                    ])
            


            schedule_train23 = Schedule([(northeast_ubon[0].get_station_name, "21.05"), 
                                    (northeast_ubon[1].get_station_name, "21.20"),
                                    (northeast_ubon[2].get_station_name , "21.30"),
                                    (northeast_ubon[3].get_station_name , "22.01"),
                                    (northeast_ubon[4].get_station_name, "22.35"),
                                    (northeast_ubon[5].get_station_name , "00.07"),
                                    (northeast_ubon[6].get_station_name , "01.36"),
                                    (northeast_ubon[7].get_station_name , "03.02"),
                                    (northeast_ubon[8].get_station_name , "03.31"),
                                    (northeast_ubon[9].get_station_name , "04.13"),
                                    (northeast_ubon[10].get_station_name , "04.42"),
                                    (northeast_ubon[11].get_station_name , "05.19"),
                                    (northeast_ubon[12].get_station_name , "05.38"),
                                    (northeast_ubon[13].get_station_name , "06.06"),
                                    (northeast_ubon[14].get_station_name , "06.40"),
                                    ])
            

            schedule_train141 = Schedule([(northeast_ubon[0].get_station_name, "23.05"), 
                                    (northeast_ubon[1].get_station_name, "23.21"),
                                    (northeast_ubon[2].get_station_name , "23.35"),
                                    (northeast_ubon[3].get_station_name , "00.16"),
                                    (northeast_ubon[4].get_station_name , "00.58"),
                                    (northeast_ubon[5].get_station_name, "02.54"),
                                    (northeast_ubon[6].get_station_name , "04.19"),
                                    (northeast_ubon[7].get_station_name , "05.53"),
                                    (northeast_ubon[8].get_station_name , "06.30"),
                                    (northeast_ubon[9].get_station_name , "07.26"),
                                    (northeast_ubon[10].get_station_name , "08.05"),
                                    (northeast_ubon[11].get_station_name , "08.47"),
                                    (northeast_ubon[12].get_station_name , "09.06"),
                                    (northeast_ubon[13].get_station_name , "09.38"),
                                    (northeast_ubon[14].get_station_name , "10.20"),])
            
            # add schedule northes nongkuy
            schedule_train75 = Schedule([(northeast_nongkuy[0].get_station_name, "08.45"), 
                                    (northeast_nongkuy[1].get_station_name, "09.00"),
                                    (northeast_nongkuy[2].get_station_name , "09.12"),
                                    (northeast_nongkuy[3].get_station_name, "09.41"),
                                    (northeast_nongkuy[4].get_station_name , "10.28"),
                                    (northeast_nongkuy[5].get_station_name , "11.41"),
                                    (northeast_nongkuy[6].get_station_name , "14.04"),
                                    (northeast_nongkuy[7].get_station_name , "14.39"),
                                    (northeast_nongkuy[8].get_station_name , "15.00"),
                                    (northeast_nongkuy[9].get_station_name , "15.30"),
                                    (northeast_nongkuy[10].get_station_name , "15.55"),
                                    (northeast_nongkuy[11].get_station_name , "16.28"),
                                    (northeast_nongkuy[12].get_station_name , "16.55"),
                                    (northeast_nongkuy[13].get_station_name , "17.30"),])
            
            schedule_train25 = Schedule([(northeast_nongkuy[0].get_station_name, "20.25"), 
                                    (northeast_nongkuy[1].get_station_name, "20.40"),
                                    (northeast_nongkuy[2].get_station_name , "20.53"),
                                    (northeast_nongkuy[3].get_station_name, "21.38"),
                                    (northeast_nongkuy[4].get_station_name , "22.28"),
                                    (northeast_nongkuy[5].get_station_name , "23.58"),
                                    (northeast_nongkuy[6].get_station_name , "02.40"),
                                    (northeast_nongkuy[7].get_station_name , "03.14"),
                                    (northeast_nongkuy[8].get_station_name , "03.37"),
                                    (northeast_nongkuy[9].get_station_name , "04.10"),
                                    (northeast_nongkuy[10].get_station_name , "04.37"),
                                    (northeast_nongkuy[11].get_station_name , "05.12"),
                                    (northeast_nongkuy[12].get_station_name , "05.39"),
                                    (northeast_nongkuy[13].get_station_name , "06.25"),])
            
            schedule_train133 = Schedule([(northeast_nongkuy[0].get_station_name, "21.25"),
                                    (northeast_nongkuy[1].get_station_name, "22.45"),
                                    (northeast_nongkuy[2].get_station_name , "22.57"),
                                    (northeast_nongkuy[3].get_station_name, "23.41"),
                                    (northeast_nongkuy[4].get_station_name , "00.28"),
                                    (northeast_nongkuy[5].get_station_name , "01.41"),
                                    (northeast_nongkuy[6].get_station_name , "04.04"),
                                    (northeast_nongkuy[7].get_station_name , "04.39"),
                                    (northeast_nongkuy[8].get_station_name , "05.00"),
                                    (northeast_nongkuy[9].get_station_name , "05.30"),
                                    (northeast_nongkuy[10].get_station_name , "05.55"),
                                    (northeast_nongkuy[11].get_station_name , "06.28"),
                                    (northeast_nongkuy[12].get_station_name , "06.55"),
                                    (northeast_nongkuy[13].get_station_name , "07.30"),])


            # add schedule south hadyai
            schedule_train43 = Schedule([(south[0].get_station_name, "07.41"),
                                    (south[1].get_station_name, "07.59"),
                                    (south[2].get_station_name , "08.22"),
                                    (south[3].get_station_name, "09.07"),
                                    (south[4].get_station_name , "09.45"),
                                    (south[5].get_station_name , "10.31"),
                                    (south[6].get_station_name , "13.50"),
                                    (south[7].get_station_name , "16.20"),])
            
            schedule_train171 = Schedule([(south[0].get_station_name, "15.10"),
                                    (south[1].get_station_name, "15.21"),
                                    (south[2].get_station_name , "15.41"),
                                    (south[3].get_station_name, "16.04"),
                                    (south[4].get_station_name , "16.24"),
                                    (south[5].get_station_name , "17.50"),
                                    (south[6].get_station_name , "18.44"),
                                    (south[7].get_station_name , "19.06"),
                                    (south[8].get_station_name , "01.11"),
                                    (south[9].get_station_name , "02.59"),
                                    (south[10].get_station_name , "04.39"),
                                    (south[11].get_station_name , "05.50"),])
            
            schedule_train37 = Schedule([(south[0].get_station_name, "16.10"),
                                    (south[1].get_station_name, "16.21"),
                                    (south[2].get_station_name , "17.10"),
                                    (south[3].get_station_name, "18.00"),
                                    (south[4].get_station_name , "18.51"),
                                    (south[5].get_station_name , "19.45"),
                                    (south[6].get_station_name , "23.16"),
                                    (south[7].get_station_name , "21.06"),
                                    (south[8].get_station_name , "01.49"),
                                    (south[9].get_station_name , "03.38"),
                                    (south[10].get_station_name , "05.21"),
                                    (south[11].get_station_name , "06.35"),])
            
            schedule_train45 = Schedule([(south[0].get_station_name, "16.10"),
                                    (south[1].get_station_name, "16.21"),
                                    (south[2].get_station_name , "16.42"),
                                    (south[3].get_station_name, "18.00"),
                                    (south[4].get_station_name , "18.51"),
                                    (south[5].get_station_name , "19.45"),
                                    (south[6].get_station_name , "23.16"),
                                    (south[7].get_station_name , "21.06"),
                                    (south[8].get_station_name , "01.49"),
                                    (south[9].get_station_name , "03.38"),
                                    (south[10].get_station_name , "05.21"),
                                    (south[11].get_station_name , "06.35"),])
            
            
            schedule_train31 = Schedule([(south[0].get_station_name, "16.50"),
                                    (south[1].get_station_name, "17.01"),
                                    (south[2].get_station_name , "17.22"),
                                    (south[3].get_station_name, "17.48"),
                                    (south[4].get_station_name , "18.37"),
                                    (south[5].get_station_name , "19.30"),
                                    (south[6].get_station_name , "20.20"),
                                    (south[7].get_station_name , "23.55"),
                                    (south[8].get_station_name , "02.20"),
                                    (south[9].get_station_name , "04.08"),
                                    (south[10].get_station_name , "05.51"),
                                    (south[11].get_station_name , "07.05"),])
            

            schedule_train169 = Schedule([(south[0].get_station_name, "17.30"),
                                    (south[1].get_station_name, "17.41"),
                                    (south[2].get_station_name , "18.02"),
                                    (south[3].get_station_name, "18.29"),
                                    (south[4].get_station_name , "19.23"),
                                    (south[5].get_station_name , "20.20"),
                                    (south[6].get_station_name , "21.20"),
                                    (south[7].get_station_name , "01.25"),
                                    (south[8].get_station_name , "04.06"),
                                    (south[9].get_station_name , "05.59"),
                                    (south[10].get_station_name , "07.53"),
                                    (south[11].get_station_name , "09.18"),])
            
            schedule_train83 = Schedule([(south[0].get_station_name, "18.50"),
                                    (south[1].get_station_name, "19.01"),
                                    (south[2].get_station_name , "19.22"),
                                    (south[3].get_station_name, "19.48"),
                                    (south[4].get_station_name , "20.38"),
                                    (south[5].get_station_name , "21.32"),
                                    (south[6].get_station_name , "22.29"),
                                    (south[7].get_station_name , "02.18"),
                                    (south[8].get_station_name , "04.58"),])
            
            schedule_train85 = Schedule([(south[0].get_station_name, "19.50"),
                                    (south[1].get_station_name, "20.01"),
                                    (south[2].get_station_name , "20.22"),
                                    (south[3].get_station_name, "20.50"),
                                    (south[4].get_station_name , "21.47"),
                                    (south[5].get_station_name , "22.41"),
                                    (south[6].get_station_name , "23.42"),
                                    (south[7].get_station_name , "03.08"),
                                    (south[8].get_station_name , "06.23"),
                                    (south[9].get_station_name , "08.30"),])
            
            schedule_train167 = Schedule([(south[0].get_station_name, "20.30"),
                                    (south[1].get_station_name, "20.41"),
                                    (south[2].get_station_name , "21.02"),
                                    (south[3].get_station_name, "21.30"),
                                    (south[4].get_station_name , "22.24"),
                                    (south[5].get_station_name , "23.19"),
                                    (south[6].get_station_name , "00.18"),
                                    (south[7].get_station_name , "04.20"),
                                    (south[8].get_station_name , "07.16"),
                                    (south[9].get_station_name , "09.34"),])
            
            schedule_train39 = Schedule([(south[0].get_station_name, "22.50"),
                                    (south[1].get_station_name, "23.01"),
                                    (south[2].get_station_name , "23.19"),
                                    (south[3].get_station_name, "23.42"),
                                    (south[4].get_station_name , "00.27"),
                                    (south[5].get_station_name , "01.14"),
                                    (south[6].get_station_name , "02.04"),
                                    (south[7].get_station_name , "05.22"),])
            

            # add schedule back north to bangkok
            schedule_train8 = Schedule([(north[12].get_station_name , "08.50"), 
                                    (north[11].get_station_name , "09.04"),
                                    (north[10].get_station_name , "09.46"),
                                    (north[9].get_station_name , "10.38"),
                                    (north[8].get_station_name , "12.38"),
                                    (north[7].get_station_name , "13.25"),
                                    (north[6].get_station_name , "14.34"),
                                    (north[5].get_station_name , "16.21"),
                                    (north[4].get_station_name , "17.26"),
                                    (north[3].get_station_name , "18.05"),
                                    (north[2].get_station_name , "18.30"),
                                    (north[1].get_station_name , "18.40"),
                                    (north[0].get_station_name , "18.55")])
            
            schedule_train102 = Schedule([(north[12].get_station_name , "06.30"), 
                                    (north[11].get_station_name , "06.48"),
                                    (north[10].get_station_name , "07.35"),
                                    (north[9].get_station_name , "08.27"),
                                    (north[8].get_station_name , "10.43"),
                                    (north[7].get_station_name , "11.37"),
                                    (north[6].get_station_name , "13.16"),
                                    (north[5].get_station_name , "15.53"),
                                    (north[4].get_station_name , "18.05"),
                                    (north[3].get_station_name , "19.14"),
                                    (north[2].get_station_name , "19.55"),
                                    (north[1].get_station_name , "20.08"),
                                    (north[0].get_station_name , "20.25")])
            

            schedule_train52 = Schedule([(north[12].get_station_name , "15.30"), 
                                    (north[11].get_station_name , "15.48"),
                                    (north[10].get_station_name , "16.45"),
                                    (north[9].get_station_name , "17.54"),
                                    (north[8].get_station_name , "20.23"),
                                    (north[7].get_station_name , "21.20"),
                                    (north[6].get_station_name , "22.58"),
                                    (north[5].get_station_name , "01.11"),
                                    (north[4].get_station_name , "02.44"),
                                    (north[3].get_station_name , "03.56"),
                                    (north[2].get_station_name , "04.40"),
                                    (north[1].get_station_name , "04.53"),
                                    (north[0].get_station_name , "05.10")])
            
            schedule_train108 = Schedule([(north[8].get_station_name , "19.05"),
                                    (north[7].get_station_name , "20.12"),
                                    (north[6].get_station_name , "22.09"),
                                    (north[5].get_station_name , "00.48"),
                                    (north[4].get_station_name , "02.08"),
                                    (north[3].get_station_name , "03.21"),
                                    (north[2].get_station_name , "04.03"),
                                    (north[1].get_station_name , "04.15"),
                                    (north[0].get_station_name , "04.30"),])
            
            schedule_train14 = Schedule([(north[12].get_station_name , "17.00"), 
                                    (north[11].get_station_name ,"17.20"),
                                    (north[10].get_station_name ,"18.24"),
                                    (north[9].get_station_name , "19.27"),
                                    (north[8].get_station_name , "21.41"),
                                    (north[7].get_station_name , "22.36"),
                                    (north[6].get_station_name , "00.01"),
                                    (north[5].get_station_name , "01.59"),
                                    (north[4].get_station_name , "03.39"),
                                    (north[3].get_station_name , "04.50"),
                                    (north[2].get_station_name , "05.34"),
                                    (north[1].get_station_name , "05.45"),
                                    (north[0].get_station_name , "06.00")])
            
            schedule_train10 = Schedule([(north[12].get_station_name , "18.00"), 
                                    (north[11].get_station_name , "18.20"),
                                    (north[10].get_station_name , "19.21"),
                                    (north[9].get_station_name , "20.17"),
                                    (north[8].get_station_name , "22.36"),
                                    (north[7].get_station_name , "23.33"),
                                    (north[6].get_station_name , "00.50"),
                                    (north[5].get_station_name , "02.41"),
                                    (north[4].get_station_name , "04.09"),
                                    (north[3].get_station_name , "05.29"),
                                    (north[2].get_station_name , "06.23"),
                                    (north[1].get_station_name , "06.35"),
                                    (north[0].get_station_name , "06.50")])
            
            schedule_train112 = Schedule([
                                    (north[8].get_station_name , "07.30"),
                                    (north[7].get_station_name , "08.27"),
                                    (north[6].get_station_name , "10.03"),
                                    (north[5].get_station_name , "12.42"),
                                    (north[4].get_station_name , "14.39"),
                                    (north[3].get_station_name , "15.59"),
                                    (north[2].get_station_name , "16.53"),
                                    (north[1].get_station_name , "17.05"),
                                    (north[0].get_station_name , "17.20")])
            


            schedule_train72= Schedule([(northeast_ubon[14].get_station_name, "05.40"),
                                    (northeast_ubon[13].get_station_name, "06.08"),
                                    (northeast_ubon[12].get_station_name, "06.28"),
                                    (northeast_ubon[11].get_station_name, "06.44"),
                                    (northeast_ubon[10].get_station_name, "07.20"),
                                    (northeast_ubon[9].get_station_name, "07.49"),
                                    (northeast_ubon[8].get_station_name, "08.35"),
                                    (northeast_ubon[7].get_station_name, "08.57"),
                                    (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "11.27"),
                                    (northeast_ubon[4].get_station_name, "12.43"),
                                    (northeast_ubon[3].get_station_name, "13.24"),
                                    (northeast_ubon[2].get_station_name, "14.04"),
                                    (northeast_ubon[1].get_station_name, "14.16"),
                                    (northeast_ubon[0].get_station_name, "14.30 ")])
            
            schedule_train136 = Schedule([(northeast_ubon[14].get_station_name, "07.00"),
                                    (northeast_ubon[13].get_station_name, "07.38"),
                                    (northeast_ubon[12].get_station_name, "08.04"),
                                    (northeast_ubon[11].get_station_name, "08.28"),
                                    (northeast_ubon[10].get_station_name, "09.08"),
                                    (northeast_ubon[9].get_station_name, "09.39"),
                                    (northeast_ubon[8].get_station_name, "10.27"),
                                    (northeast_ubon[7].get_station_name, "10.55"),
                                    # (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "14.00"),
                                    (northeast_ubon[4].get_station_name, "15.45"),
                                    (northeast_ubon[3].get_station_name, "16.37"),
                                    (northeast_ubon[2].get_station_name, "17.28"),
                                    (northeast_ubon[1].get_station_name, "17.40"),
                                    (northeast_ubon[0].get_station_name, "17.55")])
            

            schedule_train22 = Schedule([(northeast_ubon[14].get_station_name, "14.50"),
                                    (northeast_ubon[13].get_station_name, "15.12"),
                                    (northeast_ubon[12].get_station_name, "15.31"),
                                    (northeast_ubon[11].get_station_name, "15.48"),
                                    (northeast_ubon[10].get_station_name, "16.16"),
                                    (northeast_ubon[9].get_station_name, "16.41"),
                                    (northeast_ubon[8].get_station_name, "17.15"),
                                    (northeast_ubon[7].get_station_name, "17.35"),
                                    # (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "19.48"),
                                    (northeast_ubon[4].get_station_name, "21.05"),
                                    (northeast_ubon[3].get_station_name, "21.42"),
                                    (northeast_ubon[2].get_station_name, "22.11"),
                                    (northeast_ubon[1].get_station_name, "22.22"),
                                    (northeast_ubon[0].get_station_name, "22.35")])
            
            schedule_train142 = Schedule([(northeast_ubon[14].get_station_name, "17.35"),
                                    (northeast_ubon[13].get_station_name, "18.14"),
                                    (northeast_ubon[12].get_station_name, "18.41"),
                                    (northeast_ubon[11].get_station_name, "19.02"),
                                    (northeast_ubon[10].get_station_name, "19.49"),
                                    (northeast_ubon[9].get_station_name, "20.22"),
                                    (northeast_ubon[8].get_station_name, "21.17"),
                                    (northeast_ubon[7].get_station_name, "21.45"),
                                    # (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "01.03"),
                                    (northeast_ubon[4].get_station_name, "02.29"),
                                    (northeast_ubon[3].get_station_name, "03.07"),
                                    (northeast_ubon[2].get_station_name, "03.43"),
                                    (northeast_ubon[1].get_station_name, "03.55"),
                                    (northeast_ubon[0].get_station_name, "04.10")])
            

            schedule_train24 = Schedule([(northeast_ubon[14].get_station_name, "19.00"),
                                    (northeast_ubon[13].get_station_name, "19.30"),
                                    (northeast_ubon[12].get_station_name, "19.56"),
                                    (northeast_ubon[11].get_station_name, "20.16"),
                                    (northeast_ubon[10].get_station_name, "20.53"),
                                    (northeast_ubon[9].get_station_name, "21.23"),
                                    (northeast_ubon[8].get_station_name, "22.04"),
                                    (northeast_ubon[7].get_station_name, "22.32"),
                                    # (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "01.31"),
                                    (northeast_ubon[4].get_station_name, "03.00"),
                                    (northeast_ubon[3].get_station_name, "03.42"),
                                    (northeast_ubon[2].get_station_name, "04.23"),
                                    (northeast_ubon[1].get_station_name, "04.35"),
                                    (northeast_ubon[0].get_station_name, "04.50")])
            
            schedule_train140 = Schedule([(northeast_ubon[14].get_station_name, "20.30"),
                                    (northeast_ubon[13].get_station_name, "20.58"),
                                    (northeast_ubon[12].get_station_name, "21.24"),
                                    (northeast_ubon[11].get_station_name, "21.43"),
                                    (northeast_ubon[10].get_station_name, "22.25"),
                                    (northeast_ubon[9].get_station_name, "22.56"),
                                    (northeast_ubon[8].get_station_name, "23.44"),
                                    (northeast_ubon[7].get_station_name, "00.11"),
                                    # (northeast_ubon[6].get_station_name, "10.03"),
                                    (northeast_ubon[5].get_station_name, "03.03"),
                                    (northeast_ubon[4].get_station_name, "04.50"),
                                    (northeast_ubon[3].get_station_name, "05.50"),
                                    (northeast_ubon[2].get_station_name, "06.43"),
                                    (northeast_ubon[1].get_station_name, "06.55"),
                                    (northeast_ubon[0].get_station_name, "07.10")])
            

            schedule_train76 = Schedule([(northeast_nongkuy[13].get_station_name, "07.45"),
                                    (northeast_nongkuy[12].get_station_name, "08.16"),
                                    (northeast_nongkuy[11].get_station_name, "08.40"),
                                    (northeast_nongkuy[10].get_station_name, "09.10"),
                                    (northeast_nongkuy[9].get_station_name , "09.32"),
                                    (northeast_nongkuy[8].get_station_name , "09.57"),
                                    (northeast_nongkuy[7].get_station_name , "10.15"),
                                    (northeast_nongkuy[6].get_station_name , "10.45"),
                                    (northeast_nongkuy[5].get_station_name , "13.21"),
                                    (northeast_nongkuy[4].get_station_name , "14.44"),
                                    (northeast_nongkuy[3].get_station_name , "15.35"),
                                    (northeast_nongkuy[2].get_station_name , "16.10"),
                                    (northeast_nongkuy[1].get_station_name , "16.21"),
                                    (northeast_nongkuy[0].get_station_name , "16.35"),])
            

            schedule_train26 = Schedule([(northeast_nongkuy[13].get_station_name, "19.40"),
                                    (northeast_nongkuy[12].get_station_name, "20.20"),
                                    (northeast_nongkuy[11].get_station_name, "20.47"),
                                    (northeast_nongkuy[10].get_station_name, "21.22"),
                                    (northeast_nongkuy[9].get_station_name , "21.49"),
                                    (northeast_nongkuy[8].get_station_name , "22.22"),
                                    (northeast_nongkuy[7].get_station_name , "22.45"),
                                    (northeast_nongkuy[6].get_station_name , "23.17"),
                                    (northeast_nongkuy[5].get_station_name , "02.04"),
                                    (northeast_nongkuy[4].get_station_name , "03.23"),
                                    (northeast_nongkuy[3].get_station_name , "04.24"),
                                    (northeast_nongkuy[2].get_station_name , "05.03"),
                                    (northeast_nongkuy[1].get_station_name , "05.15"),
                                    (northeast_nongkuy[0].get_station_name , "05.30"),])
            

            schedule_train134 = Schedule([(northeast_nongkuy[13].get_station_name, "20.15"),
                                    (northeast_nongkuy[12].get_station_name, "20.59"),
                                    (northeast_nongkuy[11].get_station_name, "21.33"),
                                    (northeast_nongkuy[10].get_station_name, "22.21"),
                                    (northeast_nongkuy[9].get_station_name , "22.51"),
                                    (northeast_nongkuy[8].get_station_name , "23.29"),
                                    (northeast_nongkuy[7].get_station_name , "23.54"),
                                    (northeast_nongkuy[6].get_station_name , "00.36"),
                                    (northeast_nongkuy[5].get_station_name , "03.47"),
                                    (northeast_nongkuy[4].get_station_name , "05.21"),
                                    (northeast_nongkuy[3].get_station_name , "06.21"),
                                    (northeast_nongkuy[2].get_station_name , "07.03"),
                                    (northeast_nongkuy[1].get_station_name , "07.15"),
                                    (northeast_nongkuy[0].get_station_name , "07.30"),])
            

            schedule_train32 = Schedule([(south[11].get_station_name, "17.45"),
                                    (south[10].get_station_name, "18.57"),
                                    (south[9].get_station_name, "20.37"),
                                    (south[8].get_station_name, "22.24"),
                                    (south[7].get_station_name, "00.54"),
                                    (south[6].get_station_name, "04.27"),
                                    (south[5].get_station_name, "05.23"),
                                    (south[4].get_station_name, "06.08"),
                                    (south[3].get_station_name, "07.06"),
                                    (south[2].get_station_name, "07.34"),
                                    (south[1].get_station_name, "07.57"),
                                    (south[0].get_station_name, "08.10"),])
            

            schedule_train38 = Schedule([(south[11].get_station_name, "18.05"),
                                    (south[10].get_station_name, "19.18"),
                                    (south[9].get_station_name, "21.02"),
                                    (south[8].get_station_name, "22.50"),
                                    (south[7].get_station_name, "01.27"),
                                    (south[6].get_station_name, "05.17"),
                                    (south[5].get_station_name, "06.13"),
                                    (south[4].get_station_name, "06.59"),
                                    (south[3].get_station_name, "08.00"),
                                    (south[2].get_station_name, "08.29"),
                                    (south[1].get_station_name, "08.52"),
                                    (south[0].get_station_name, "09.05"),])
            

            schedule_train46 = Schedule([(south[11].get_station_name, "18.05"),
                                    (south[10].get_station_name, "19.18"),
                                    (south[9].get_station_name, "21.02"),
                                    (south[8].get_station_name, "22.50"),
                                    (south[7].get_station_name, "01.27"),
                                    (south[6].get_station_name, "05.17"),
                                    (south[5].get_station_name, "06.13"),
                                    (south[4].get_station_name, "06.59"),
                                    (south[3].get_station_name, "08.00"),
                                    (south[2].get_station_name, "08.29"),
                                    (south[1].get_station_name, "08.52"),
                                    (south[0].get_station_name, "09.05"),])
            

            schedule_train170 = Schedule([(south[11].get_station_name, "18.20"),
                                    (south[10].get_station_name, "19.41"),
                                    (south[9].get_station_name, "21.30"),
                                    (south[8].get_station_name, "23.28"),
                                    (south[7].get_station_name, "02.32"),
                                    (south[6].get_station_name, "06.40"),
                                    (south[5].get_station_name, "07.43"),
                                    (south[4].get_station_name, "08.32"),
                                    (south[3].get_station_name, "09.38"),
                                    (south[2].get_station_name, "10.13"),
                                    (south[1].get_station_name, "10.34"),
                                    (south[0].get_station_name, "10.50"),])
            
            
            schedule_train172 = Schedule([(south[11].get_station_name, "16.05"),
                                    (south[10].get_station_name, "17.21"),
                                    (south[9].get_station_name, "19.02"),
                                    (south[8].get_station_name, "20.55"),
                                    (south[7].get_station_name, "23.56"),
                                    (south[6].get_station_name, "03.51"),
                                    (south[5].get_station_name, "04.46"),
                                    (south[4].get_station_name, "05.32"),
                                    (south[3].get_station_name, "06.26"),
                                    (south[2].get_station_name, "06.54"),
                                    (south[1].get_station_name, "07.17"),
                                    (south[0].get_station_name, "07.30"),])
            
            schedule_train168 = Schedule([
                                    (south[9].get_station_name, "16.11"),
                                    (south[8].get_station_name, "18.32"),
                                    (south[7].get_station_name, "21.20"),
                                    (south[6].get_station_name, "01.26"),
                                    (south[5].get_station_name, "02.23"),
                                    (south[4].get_station_name, "03.09"),
                                    (south[3].get_station_name, "04.05"),
                                    (south[2].get_station_name, "04.35"),
                                    (south[1].get_station_name, "04.58"),
                                    (south[0].get_station_name, "05.10"),])
            
            schedule_train86 = Schedule([
                                    (south[9].get_station_name, "17.17"),
                                    (south[8].get_station_name, "19.31"),
                                    (south[7].get_station_name, "22.19"),
                                    (south[6].get_station_name, "02.20"),
                                    (south[5].get_station_name, "03.19"),
                                    (south[4].get_station_name, "04.05"),
                                    (south[3].get_station_name, "05.05"),
                                    (south[2].get_station_name, "05.34"),
                                    (south[1].get_station_name, "06.52"),
                                    (south[0].get_station_name, "09.05"),])
            
            schedule_train84 = Schedule([
                                    (south[9].get_station_name, "18.28"),
                                    (south[8].get_station_name, "20.23"),
                                    (south[7].get_station_name, "23.18"),
                                    (south[6].get_station_name, "03.04"),
                                    (south[5].get_station_name, "04.02"),
                                    (south[4].get_station_name, "04.45"),
                                    (south[3].get_station_name, "05.54"),
                                    (south[2].get_station_name, "06.29"),
                                    (south[1].get_station_name, "06.52"),
                                    (south[0].get_station_name, "07.05"),])
            
            schedule_train40 = Schedule([
                                    (south[8].get_station_name, "09.00"),
                                    (south[7].get_station_name, "11.18"),
                                    (south[6].get_station_name, "14.36"),
                                    (south[5].get_station_name, "15.25"),
                                    (south[4].get_station_name, "16.09"),
                                    (south[3].get_station_name, "17.07"),
                                    (south[2].get_station_name, "17.35"),
                                    (south[1].get_station_name, "17.54"),
                                    (south[0].get_station_name, "18.05"),])
            
            schedule_train44 = Schedule([
                                    (south[8].get_station_name, "18.25"),
                                    (south[7].get_station_name, "20.21"),
                                    (south[6].get_station_name, "00.14"),
                                    (south[5].get_station_name, "01.03"),
                                    (south[4].get_station_name, "01.45"),
                                    (south[3].get_station_name, "02.42"),
                                    (south[2].get_station_name, "03.10"),
                                    (south[1].get_station_name, "03.32"),
                                    (south[0].get_station_name, "03.45"),])
        

         
         
            # add train north
            train7 = Train("7", "ด่วนพิเศษดีเซลราง")
            train9 = Train("9", "ด่วนพิเศษ CNR",)
            train13 = Train("13", "ด่วนพิเศษ")
            train109 = Train("109", "เร็ว",)
            train51 = Train("51", "ด่วน",)
            train111 = Train("111", "เร็ว",)
            train107 = Train("107", "เร็ว",)

            # add train northes ubon
            train21 = Train("21", "ด่วนพิเศษดีเซลราง")
            train135 = Train("135", "เร็ว")
            train71 = Train("71", "ด่วน")
            train139 = Train("139", "เร็ว",)
            train23 = Train("23", "ด่วนพิเศษ CNR")
            train141 = Train("141", "เร็ว",)

            # add train northes 
            train75 = Train("75", "ด่วน")
            train25 = Train ("25", "ด่วนพิเศษ CNR")
            train133 = Train("133", "เร็ว")
            
            # add train sourth
            train43 = Train("43", "ด่วนพิเศษดีเซลราง")
            train171 = Train("171", "เร็ว")
            train37 = Train("37",  "ด่วนพิเศษ")
            train45 = Train("45", "ด่วนพิเศษ")
            train31 = Train("31",  "ด่วนพิเศษ")
            train169 = Train("169", "เร็ว", )
            train83 = Train("83", "ด่วน")
            train85 = Train("85", "ด่วน", )
            train167 = Train("167", "เร็ว", )
            train39 = Train("39", "ด่วนพิเศษดีเซลราง", )
            

            # back train
            train102 = Train("102", "เร็ว")
            train8 = Train("8", "ด่วนพิเศษดีเซลราง")
            train52 = Train("52", "ด่วน")
            train14 = Train("14", "ด่วนพิเศษ")
            train10 = Train("10", "ด่วนพิเศษ CNR")
            train112 = Train("112", "เร็ว")
            train108 = Train("108", "เร็ว")

            train72 = Train("72", "ด่วน")
            train136 = Train("136", "เร็ว")
            train22 = Train("22", "ด่วนพิเศษดีเซลราง")
            train142 = Train("142", "เร็ว")
            train24 = Train("24", "ด่วนพิเศษ CNR")
            train140 = Train("140", "เร็ว")

            train76 = Train("76", "ด่วน")
            train26 = Train("26", "ด่วนพิเศษ CNR")
            train134 = Train("134", "เร็ว")

            train172 = Train("172", "เร็ว")
            train32 = Train("32", "ด่วนพิเศษ CNR")
            train38 = Train("38", "ด่วนพิเศษ")
            train46 = Train("46", "ด่วนพิเศษ")
            train170 = Train("170", "เร็ว")

            train168 = Train("168", "เร็ว")
            train86 = Train("86", "ด่วน")
            train84 = Train("84", "เร็ว")

            train40 = Train("40", "ด่วนพิเศษดีเซลราง")
            train44 = Train("44", "ด่วนพิเศษดีเซลราง")

            control.add_train(train7)
            control.add_train(train9)
            control.add_train(train13)
            control.add_train(train109)
            control.add_train(train51)
            control.add_train(train111)
            control.add_train(train107)

            control.add_train(train21)
            control.add_train(train135)
            control.add_train(train71)
            control.add_train(train139)
            control.add_train(train23)
            control.add_train(train141)

            control.add_train(train75)
            control.add_train(train25)
            control.add_train(train133)

            control.add_train(train43)
            control.add_train(train171)
            control.add_train(train37)
            control.add_train(train45)
            control.add_train(train31)
            control.add_train(train169)
            control.add_train(train83)
            control.add_train(train85)
            control.add_train(train167)
            control.add_train(train39)

            control.add_train(train102)
            control.add_train(train8)
            control.add_train(train52)
            control.add_train(train14)
            control.add_train(train10)
            control.add_train(train112)
            control.add_train(train108)

            control.add_train(train72)
            control.add_train(train136)
            control.add_train(train22)
            control.add_train(train142)
            control.add_train(train24)
            control.add_train(train140)

            control.add_train(train76)
            control.add_train(train26)
            control.add_train(train134)

            control.add_train(train172)
            control.add_train(train32)
            control.add_train(train38)
            control.add_train(train46)
            control.add_train(train170)

            control.add_train(train168)
            control.add_train(train86)
            control.add_train(train84)

            control.add_train(train40)
            control.add_train(train44)

            # add carrige
            carriage7 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง", 76)
            carriage09 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน", 24)
            carriage09_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน", 40)
            carriage09_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carriage09_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carriage109 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage109_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage109_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage13 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carrage13_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage13_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage13_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage51 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage51_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage51_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage111 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage111_1 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)

            carriage107 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage107_1 = Carriage("บนท.ป.40", "2", "ปร้บอากาศ", "นอน",40)
            carriage107_2 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carriage107_3 = Carriage("บนท.ป.36", "2", "ปรับอากาศ", "นอน",36)


            carriage21 = Carriage("กซข.ป.76", "2", "อากาศ", "นั่ง",76)

            carriage135 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage135_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage135_2 = Carriage("บสส.20", "2", "พัดลม", "นอน",20)

            carriage71 = Carriage("กซข.74", "3", "พัดลม", "นั่ง",74)
            carriage71_1 = Carriage("กซม.ป.62", "2", "ปรับอากาศ", "นั่ง",62)

            carriage139 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage139_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage139_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นั่ง",40)
            carriage139_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)

            carriage23 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carriage23_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carriage23_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carriage23_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carriage141 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carriage141_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)

            carriage75 = Carriage("กซข.74", "3", "พัดลม", "นั่ง",74)
            carriage75_1 = Carriage("กซม.ป.62", "2", "ปรับอากาศ", "นั่ง",62)

            carriage25 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carriage25_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carriage25_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carriage25_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carriage133 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage133_1 = Carriage("บสส.20", "3", "พัดลม", "นั่ง",20)
            carriage133_2 = Carriage("บนท.ป.34.JR", "2", "ปรับอากาศ", "นอน",34)
            carriage133_3 = Carriage("บชท.ป.72.JR", "2", "ปรับอากาศ", "นั่ง",72)
            carriage133_4 = Carriage("บนท.ป.26JR", "2", "ปรับอากาศ", "นอน",26)

            carriage43 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง",76)

            carriage171 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage171_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage171_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carriage171_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carriage171_4 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carriage37 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carriage37_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage37_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage37_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage45 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage31 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carriage31_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carriage31_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carriage31_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carriage169 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage169_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage169_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carriage169_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carriage169_4 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carriage83 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carriage83_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage83_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage83_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carriage83_4 = Carriage("บชท.ป.30", "2", "ปรับอากาศ", "นั่ง",30)

            carriage85 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carriage85_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage85_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage85_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carriage167 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage167_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carriage167_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carriage167_3 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carriage39 = Carriage("บชส.76", "3", "ปรับอากาศ", "นั่ง",76)


            # leg back
            carriage8 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง",76)

            carriage102 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carriage102_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)

            carrage52 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage52_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage52_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carrage14 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carrage14_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage14_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage14_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carrage10 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carrage10_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carrage10_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carrage10_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carrage112 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage112_1 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)

            carrage108 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76,)
            carrage108_1 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage108_2 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carrage108_3 = Carriage("บนท.ป.36", "2", "ปรับอากาศ", "นอน",36)

            carrage72 = Carriage("กซข.74", "3", "พัดลม", "นั่ง",74)
            carrage72_1 = Carriage("กซม.ป.62", "2", "ปรับอากาศ", "นั่ง",62)

            carrage136 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage136_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage136_2 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)   

            carrage22 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง",76)

            carrage142 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage142_1 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)

            carrage24 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carrage24_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carrage24_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carrage24_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carrage140 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage140_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage140_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage140_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)

            carrage76 = Carriage("กซข.74", "3", "พัดลม", "นั่ง",74)
            carrage76_1 = Carriage("กซม.ป.62", "2", "ปรับอากาศ", "นั่ง",62)

            carrage26 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carrage26_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carrage26_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carrage26_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)


            carrage134 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage134_1 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carrage134_2 = Carriage("บนท.ป.34.JR", "2", "ปรับอากาศ", "นอน",34)
            carrage134_3 = Carriage("บชท.ป.72.JR", "2", "ปรับอากาศ", "นั่ง",72)
            carrage134_4 = Carriage("บนท.ป.26JR", "2", "ปรับอากาศ", "นอน",26)

            carrage172 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage172_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage172_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage172_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carrage172_4 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carrage32 = Carriage("บนอ.ป.24.CN", "1", "ปรับอากาศ", "นอน",24)
            carrage32_1 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)
            carrage32_2 = Carriage("บนท.ป.36.CN", "2", "ปรับอากาศ", "นอน",36)
            carrage32_3 = Carriage("บนท.ป.40.CN", "2", "ปรับอากาศ", "นอน",40)

            carrage38 = Carriage("บนอ.ป.24", "1", "พัดลม", "นอน",24)
            carrage38_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage38_2 = Carriage("บชส.76", "3", "ปรับอากาศ", "นั่ง",76)
            carrage38_3 = Carriage("บนท.ป.40", "2", "พัดลม", "นอน",40)

            carrage46 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carrage170 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage170_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage170_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage170_3 = Carriage("บสส.20", "2", "พัดลม", "นั่ง",20)
            carrage170_4 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carrage168 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage168_1 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage168_2 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage168_3 = Carriage("บนท.32", "2", "พัดลม", "นอน",32)

            carrage86 = Carriage("บนอ.ป.24", "1", "พัดปรับอากาศลม", "นอน",24)
            carrage86_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage86_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage86_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)

            carrage84 = Carriage("บนอ.ป.24", "1", "ปรับอากาศ", "นอน",24)
            carrage84_1 = Carriage("บชท.48", "2", "พัดลม", "นั่ง",48)
            carrage84_2 = Carriage("บชส.76", "3", "พัดลม", "นั่ง",76)
            carrage84_3 = Carriage("บนท.ป.40", "2", "ปรับอากาศ", "นอน",40)
            carrage84_4 = Carriage("บชท.ป.30", "2", "ปรับอากาศ", "นั่ง",30)

            carrage40 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง",76)

            carrage44 = Carriage("กซข.ป.76", "2", "ปรับอากาศ", "นั่ง",76)

            control.add_carriag(carriage7)

            # add carrige in train leg go
            train7.add_carriage(carriage7)
            train9.add_carriage(carriage09)
            train9.add_carriage(carriage09_1)
            train9.add_carriage(carriage09_2)
            train9.add_carriage(carriage09_3)

            train109.add_carriage(carriage109)
            train109.add_carriage(carriage109_1)
            train109.add_carriage(carriage109_2)

            train13.add_carriage(carriage13)
            train13.add_carriage(carrage13_1)
            train13.add_carriage(carriage13_2)
            train13.add_carriage(carriage13_3)

            train51.add_carriage(carriage51)
            train51.add_carriage(carriage51_1)
            train51.add_carriage(carriage51_2)

            train111.add_carriage(carriage111)
            train111.add_carriage(carriage111_1)

            train107.add_carriage(carriage107)
            train107.add_carriage(carriage107_1)
            train107.add_carriage(carriage107_2)
            train107.add_carriage(carriage107_3)

            train21.add_carriage(carriage21)

            train135.add_carriage(carriage135)
            train135.add_carriage(carriage135_1)
            train135.add_carriage(carriage135_2)

            train71.add_carriage(carriage71)
            train71.add_carriage(carriage71_1)

            train139.add_carriage(carriage139)
            train139.add_carriage(carriage139_1)
            train139.add_carriage(carriage139_2)
            train139.add_carriage(carriage139_3)

            train23.add_carriage(carriage23)
            train23.add_carriage(carriage23_1)
            train23.add_carriage(carriage23_2)
            train23.add_carriage(carriage23_3)

            train141.add_carriage(carriage141)
            train141.add_carriage(carriage141_1)

            train75.add_carriage(carriage75)
            train75.add_carriage(carriage75_1)

            train25.add_carriage(carriage25)
            train25.add_carriage(carriage25_1)
            train25.add_carriage(carriage25_2)
            train25.add_carriage(carriage25_3)

            train133.add_carriage(carriage133)
            train133.add_carriage(carriage133_1)
            train133.add_carriage(carriage133_2)
            train133.add_carriage(carriage133_3)
            train133.add_carriage(carriage133_4)

            train43.add_carriage(carriage43)

            train171.add_carriage(carriage171)
            train171.add_carriage(carriage171_1)
            train171.add_carriage(carriage171_2)
            train171.add_carriage(carriage171_3)
            train171.add_carriage(carriage171_4)

            train37.add_carriage(carriage37)
            train37.add_carriage(carriage37_1)
            train37.add_carriage(carriage37_2)
            train37.add_carriage(carriage37_3)

            train45.add_carriage(carriage45)

            train31.add_carriage(carriage31)
            train31.add_carriage(carriage31_1)
            train31.add_carriage(carriage31_2)
            train31.add_carriage(carriage31_3)

            train169.add_carriage(carriage169)
            train169.add_carriage(carriage169_1)
            train169.add_carriage(carriage169_2)
            train169.add_carriage(carriage169_3)
            train169.add_carriage(carriage169_4)


            train83.add_carriage(carriage83)
            train83.add_carriage(carriage83_1)
            train83.add_carriage(carriage83_2)
            train83.add_carriage(carriage83_3)
            train83.add_carriage(carriage83_4)

            train85.add_carriage(carriage85)
            train85.add_carriage(carriage85_1)
            train85.add_carriage(carriage85_2)
            train85.add_carriage(carriage85_3)

            train167.add_carriage(carriage167)
            train167.add_carriage(carriage167_1)
            train167.add_carriage(carriage167_2)
            train167.add_carriage(carriage167_3)

            train39.add_carriage(carriage39)


            # add carrige in train leg back
            train8.add_carriage(carriage8)
            
            train102.add_carriage(carriage102)
            train102.add_carriage(carriage102_1)

            train52.add_carriage(carrage52)
            train52.add_carriage(carrage52_1)
            train52.add_carriage(carrage52_2)

            train14.add_carriage(carrage14)
            train14.add_carriage(carrage14_1)
            train14.add_carriage(carrage14_2)
            train14.add_carriage(carrage14_3)

            train10.add_carriage(carrage10)
            train10.add_carriage(carrage10_1)
            train10.add_carriage(carrage10_2)
            train10.add_carriage(carrage10_3)

            train112.add_carriage(carrage112)
            train112.add_carriage(carrage112_1)

            train108.add_carriage(carrage108)
            train108.add_carriage(carrage108_1)
            train108.add_carriage(carrage108_2)
            train108.add_carriage(carrage108_3)

            train72.add_carriage(carrage72)
            train72.add_carriage(carrage72_1)

            train136.add_carriage(carrage136)
            train136.add_carriage(carrage136_1)
            train136.add_carriage(carrage136_2)

            train22.add_carriage(carrage22)

            train142.add_carriage(carrage142)
            train142.add_carriage(carrage142_1)

            train24.add_carriage(carrage24)
            train24.add_carriage(carrage24_1)
            train24.add_carriage(carrage24_2)
            train24.add_carriage(carrage24_3)

            train140.add_carriage(carrage140)
            train140.add_carriage(carrage140_1)
            train140.add_carriage(carrage140_2)
            train140.add_carriage(carrage140_3)

            train76.add_carriage(carrage76)
            train76.add_carriage(carrage76_1)

            train26.add_carriage(carrage26)
            train26.add_carriage(carrage26_1)
            train26.add_carriage(carrage26_2)
            train26.add_carriage(carrage26_3)


            train134.add_carriage(carrage134)
            train134.add_carriage(carrage134_1)
            train134.add_carriage(carrage134_2)
            train134.add_carriage(carrage134_3)
            train134.add_carriage(carrage134_4)

            train172.add_carriage(carrage172)
            train172.add_carriage(carrage172_1)
            train172.add_carriage(carrage172_2)
            train172.add_carriage(carrage172_3)
            train172.add_carriage(carrage172_4)

            train32.add_carriage(carrage32)
            train32.add_carriage(carrage32_1)
            train32.add_carriage(carrage32_2)
            train32.add_carriage(carrage32_3)

            train38.add_carriage(carrage38)
            train38.add_carriage(carrage38_1)
            train38.add_carriage(carrage38_2)
            train38.add_carriage(carrage38_3)

            train46.add_carriage(carrage46)

            train170.add_carriage(carrage170)
            train170.add_carriage(carrage170_1)
            train170.add_carriage(carrage170_2)
            train170.add_carriage(carrage170_3)
            train170.add_carriage(carrage170_4)

            train168.add_carriage(carrage168)
            train168.add_carriage(carrage168_1)
            train168.add_carriage(carrage168_2)
            train168.add_carriage(carrage168_3)

            train86.add_carriage(carrage86)
            train86.add_carriage(carrage86_1)
            train86.add_carriage(carrage86_2)
            train86.add_carriage(carrage86_3)

            train84.add_carriage(carrage84)
            train84.add_carriage(carrage84_1)
            train84.add_carriage(carrage84_2)
            train84.add_carriage(carrage84_3)
            train84.add_carriage(carrage84_4)

            train40.add_carriage(carrage40)

            train44.add_carriage(carrage44)
            
            

            distance_bkk_to_chiangmai = [5, 15, 8, 41, 62 , 113, 143, 99, 46, 108, 41, 46, 22]
            distance_bkk_to_ubon = [5, 15, 8, 41, 42 , 67, 84, 82, 30, 44, 42, 32, 21, 29, 31]
            distance_bkk_to_nongkuy = [5, 15, 8, 41, 54 , 84, 137, 32, 30, 42, 34, 49, 36, 52]
            distance_bkk_to_hadyai = [5, 11, 17, 29, 53 , 49, 63, 256, 166, 122, 89, 83]
            route_bkk_to_chiangmai = Route("สายเหนือ",north, distance_bkk_to_chiangmai)
            route_bkk_to_ubon = Route("สายตะวันออกเฉียงเหนือ-อุบลราชธานี",northeast_ubon, distance_bkk_to_ubon)
            route_bkk_to_nongkuy = Route("สายตะวันออกเฉียงเหนือ-หนองคาย",northeast_nongkuy, distance_bkk_to_nongkuy)
            route_bkk_to_hadyai = Route("สายใต้",south, distance_bkk_to_hadyai)

            control.add_route(route_bkk_to_chiangmai)
            control.add_route(route_bkk_to_ubon)
            control.add_route(route_bkk_to_nongkuy)
            control.add_route(route_bkk_to_hadyai)


            # add departure north เลขคู่คือ ขากลับ เลขคี่คือ ขาไป
            departure111 = Departure(train111, schedule_train111, route_bkk_to_chiangmai)
            departure07 = Departure(train7, schedule_train07, route_bkk_to_chiangmai)
            departure109 = Departure(train109, schedule_train109, route_bkk_to_chiangmai)
            departure09 = Departure(train9, schedule_train09, route_bkk_to_chiangmai)
            departure13 = Departure(train13, schedule_train13, route_bkk_to_chiangmai)
            departure107 = Departure(train107, schedule_train107, route_bkk_to_chiangmai)
            departure51 = Departure(train51, schedule_train51, route_bkk_to_chiangmai)

            departure08 = Departure(train8, schedule_train8, route_bkk_to_chiangmai)
            departure102 = Departure(train102, schedule_train102, route_bkk_to_chiangmai)
            departure52 = Departure(train52, schedule_train52, route_bkk_to_chiangmai)
            departure108 = Departure(train108, schedule_train108, route_bkk_to_chiangmai)
            departure14 = Departure(train14, schedule_train14, route_bkk_to_chiangmai)
            departure10 = Departure(train10, schedule_train10, route_bkk_to_chiangmai)
            departure112 = Departure(train112, schedule_train112, route_bkk_to_chiangmai)


            # add departure northes ubon
            departure21 = Departure(train21, schedule_train21, route_bkk_to_ubon)
            departure135 = Departure(train135, schedule_train135, route_bkk_to_ubon)
            departure71 = Departure(train71, schedule_train71, route_bkk_to_ubon)
            departure139 = Departure(train139, schedule_train139, route_bkk_to_ubon)
            departure23 = Departure(train23, schedule_train23, route_bkk_to_ubon)
            departure141 = Departure(train141, schedule_train141, route_bkk_to_ubon)

            departure72 = Departure(train72, schedule_train72, route_bkk_to_ubon)
            departure136 = Departure(train136, schedule_train136, route_bkk_to_ubon)
            departure22 = Departure(train22, schedule_train22, route_bkk_to_ubon)
            departure142 = Departure(train142, schedule_train142, route_bkk_to_ubon)
            departure24 = Departure(train24, schedule_train24, route_bkk_to_ubon)
            departure140 = Departure(train140, schedule_train140, route_bkk_to_ubon)




            # add departure northes nongkuy
            departure75 = Departure(train75, schedule_train75, route_bkk_to_nongkuy)
            departure25 = Departure(train25, schedule_train25, route_bkk_to_nongkuy)
            departure133 = Departure(train133, schedule_train133, route_bkk_to_nongkuy)

            departure76 = Departure(train76, schedule_train76, route_bkk_to_nongkuy)
            departure26 = Departure(train26, schedule_train26, route_bkk_to_nongkuy)
            departure134 = Departure(train134, schedule_train134, route_bkk_to_nongkuy)


            # add departure south
            departure43 = Departure(train43, schedule_train43, route_bkk_to_hadyai)
            departure171 = Departure(train171, schedule_train171, route_bkk_to_hadyai)
            departure37 = Departure(train37, schedule_train37, route_bkk_to_hadyai)
            departure45 = Departure(train45, schedule_train45, route_bkk_to_hadyai)
            departure31 = Departure(train31, schedule_train31, route_bkk_to_hadyai)
            departure169 = Departure(train169, schedule_train169, route_bkk_to_hadyai)
            departure83 = Departure(train83, schedule_train83, route_bkk_to_hadyai)
            departure85 = Departure(train85, schedule_train85, route_bkk_to_hadyai)
            departure167 = Departure(train167, schedule_train167, route_bkk_to_hadyai)
            departure39 = Departure(train39, schedule_train39, route_bkk_to_hadyai)

            departure32 = Departure(train32, schedule_train32, route_bkk_to_hadyai)
            departure38 = Departure(train38, schedule_train38, route_bkk_to_hadyai)
            departure46 = Departure(train46, schedule_train46, route_bkk_to_hadyai)
            departure170 = Departure(train170, schedule_train170, route_bkk_to_hadyai)
            departure172 = Departure(train172, schedule_train172, route_bkk_to_hadyai)
            departure168 = Departure(train168, schedule_train168, route_bkk_to_hadyai)
            departure86 = Departure(train86, schedule_train86, route_bkk_to_hadyai)
            departure84 = Departure(train84, schedule_train84, route_bkk_to_hadyai)
            departure40 = Departure(train40, schedule_train40, route_bkk_to_hadyai)
            departure44 = Departure(train44, schedule_train44, route_bkk_to_hadyai)


            
            # add departure in control north
            control.add_departure(departure111)
            control.add_departure(departure07)
            control.add_departure(departure109)
            control.add_departure(departure09)
            control.add_departure(departure13)
            control.add_departure(departure107)
            control.add_departure(departure51)

            control.add_departure(departure08)
            control.add_departure(departure102)
            control.add_departure(departure52)
            control.add_departure(departure108)
            control.add_departure(departure14)
            control.add_departure(departure10)
            control.add_departure(departure112)


            # add departure in control northes ubon
            control.add_departure(departure21)
            control.add_departure(departure135)
            control.add_departure(departure71)
            control.add_departure(departure139)
            control.add_departure(departure23)
            control.add_departure(departure141)

            control.add_departure(departure72)
            control.add_departure(departure136)
            control.add_departure(departure22)
            control.add_departure(departure140)
            control.add_departure(departure142)
            control.add_departure(departure24)


            # add departure in control northes nongkuy
            control.add_departure(departure75)
            control.add_departure(departure25)
            control.add_departure(departure133)

            control.add_departure(departure76)
            control.add_departure(departure26)
            control.add_departure(departure134)


            # add departure in control south
            control.add_departure(departure43)
            control.add_departure(departure171)
            control.add_departure(departure37)
            control.add_departure(departure45)
            control.add_departure(departure31)
            control.add_departure(departure169)
            control.add_departure(departure83)
            control.add_departure(departure85)
            control.add_departure(departure167)
            control.add_departure(departure39)


            control.add_departure(departure32)
            control.add_departure(departure38)
            control.add_departure(departure46)
            control.add_departure(departure170)
            control.add_departure(departure172)
            control.add_departure(departure168)
            control.add_departure(departure86)
            control.add_departure(departure84)
            control.add_departure(departure40)
            control.add_departure(departure44)

            # Add Member
            m1 = Member("พัฒนพงศ ร่มเย็น","patta@mail.com","member","0894556552","123456")
            m2 = Member("มนศักดิ์ มาโค", "totomove55@gmail.com", "member", "0653619287", "1234")
            m3 = Member("อนุวัฒน์ แสนสุขเหลือ","anawan123@mail.com","member","06666552","147258369")
            control.add_member(m1)
            control.add_member(m2)
            control.add_member(m3)


        
     
         









