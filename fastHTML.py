from fasthtml.common import *
from Controller import Controller
import requests
from datetime import datetime, time, timedelta


app,rt = fast_app()



control = Controller()
login = False
login_id = None
seat_id_list = []


popup_style = Style("""
            .popup {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0, 0, 0, 0.5); display: flex;
                align-items: center; justify-content: center; z-index: 1000;
            }
            .popup-content {
                background: white; padding: 20px; border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
                min-width: 300px; text-align: center;
                padding:40px 40px 
            }
            
            }
        """)

#แถบเมนูที่แสดงบนหน้าเว็บ
def navigation_bar():
    if not login:
        return Container(Nav(
            Ul(
                Li(H5(A("หน้าแรก",href="/"))),
                Li(H5(A("ประวัติการซื้อ", hx_get="/login-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                Li(H5(A("ยกเลิกตั๋วโดยสาร", hx_get="/login-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                Li(H5(A("ศูนย์ความช่วยเหลือ", hx_get=f"/", hx_target="#page-content"))),
                style="text-align:left;"
            ),
            Ul(
                Li(H5(A("เข้าสู่ระบบ",hx_get="/login-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                Li(H5(A("สมัครสมาชิก",hx_get="/register-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                style="text-align:right;"
            )
        ))
    else :
        return Container(Nav(
            Ul(
                Li(H5(A("หน้าแรก",href="/"))),
                Li(H5(A("ประวัติการซื้อ",href="/booking"))),
                Li(H5(A("ยกเลิกตั๋วโดยสาร",href="/cancel"))),
                Li(H5(A("ศูนย์ความช่วยเหลือ"))),
                style="text-align:left;"
            ),
            Ul(
                Li(H5(f"{control.get_login_member.get_name}")),
                Li(H5(A("ออกจากระบบ",href="/logout"))),
                style="text-align:right;"
            )))

@rt("/login-popup")
def get_popup():
    if not control.is_login:
        return Div(
            Div(
                H3("เข้าสู่ระบบ"),
                Form(
                # Email input
                Label("Email:", 
                    Input(type="email", id="email", required=True)),
                            # Password input
                Label("Password:", 
                    Input(type="password", id="password", required=True)),
                Hr(),
                Button("เข้าสู่ระบบ", type="submit"),
                method="post",
                action="/login"
            ),
                Button("ปิด", onclick="document.getElementById('popup').remove()",style="width:100%"),
                cls="popup-content"
            ),
            id="popup", cls="popup"
        )
    
@rt("/register-popup")
def get_popup():
    if not control.is_login:
        return Div(
            Div(
                H3("สมัครสมาชิก"),
                Form(
                # Namr input
                Label("Username:", 
                    Input(type="text", id="name", required=True)),
                # Email input
                Label("Email:", 
                    Input(type="email", id="email", required=True)),
                # PhoneNumber input
                Label("Phone Number:", 
                    Input(type="text", id="phone_number", required=True)),
                # Password input
                Label("Password:", 
                    Input(type="password", id="password", required=True)),
                Hr(),
                Button("ยึนยัน", type="submit"),
                method="post",
                action="/register"
            ),
                Button("ปิด", onclick="document.getElementById('popup').remove()",style="width:100%"),
                cls="popup-content"
            ),
            id="popup", cls="popup"
        )
    
@rt("/login")
def post(email:str,password:str):
    member = control.login(email,password)
    if  member == None:
        return H1("Not Found Account")
    else:
        global login
        global login_id
        login = True
        control.is_login = True
        control.login_account_no = member.get_member_id
        login_id = member.get_member_id
        return  home()
    
@rt("/logout")
def logout():
    control.logout()
    global login 
    login = False
    return home()

@rt("/register")
def post(email:str,password:str, phone_number:str , name:str):
    control.register(name,email,phone_number,password)
    print("Register Sucess")
    return  home()

#หน้า home
@rt('/')
def home():
    seat_id_list.clear()
    return navigation_bar(),Container(Card(
            H2("ค้นหาเที่ยวรถ"),
            Form(
                Label("สาย:",style="margin-right:20px"),
                Label(Input(type="radio", id="route", name="route", value="all"), "ทั้งหมด",style="margin-right:10px"),
                Label(Input(type="radio", id="route", name="route",value="n"), "สายเหนือ",style="margin-right:10px"),
                Label(Input(type="radio", id="route", name="route",value="ne_u"), "สายตะวันออกเฉียงเหนือ-อุบล",style="margin-right:10px"),
                Label(Input(type="radio", id="route", name="route",value="ne_n"), "สายตะวันออกเฉียงเหนือ-หนองคาย",style="margin-right:10px"),
                Label(Input(type="radio", id="route", name="route",value="s"), "สายใต้",style="margin-right:10px"),style="display:flex;justify-content:left;",
                hx_get="/routes", target_id="results", hx_trigger="click"),
            Container(id="results")    
            ,style="text-align:center;margin-right:100px;margin-left:100px;padding:50px"  # left, right, center, justify
            ))

#แสดงการเลือกเส้นทาง
@rt('/routes')
def get(route: str):
    station_name = []
    if route == "all":
       station_name = control.get_all_station_name()
    elif route == "n":
       station_name = control.get_stations_name_by_route_name("สายเหนือ")
    elif route == "ne_u":
       station_name = control.get_stations_name_by_route_name("สายตะวันออกเฉียงเหนือ-อุบลราชธานี")
    elif route == "ne_n":
       station_name = control.get_stations_name_by_route_name("สายตะวันออกเฉียงเหนือ-หนองคาย")
    elif route == "s":
       station_name = control.get_stations_name_by_route_name("สายใต้")
    return Form(
                Label("สถานีต้นทาง:",
                Select(
                    *[Option(f"{station}", value=f"{station}") for station in station_name],
                    id="origin_station"
                    )
                ),
                Label("สถานีปลายทาง:",
                Select(
                    *[Option(f"{station}", value=f"{station}") for station in reversed(station_name)],
                    id="detination_station"
                    )
                ),
                Label("วันที่:",
                    Input(type="date", id="bookdate", name="bookdate", value = datetime.today().strftime("%Y-%m-%d"))    
                ),
                Button("ค้นหา", type="submit"),
                method="post",
                action="/departure"
            )


def departure_card(d):
    return Card(
        Form(
            H3(f"เวลาออก {d.get_departure_time} - เวลาถึง {d.get_arrival_time}"), 
            H4(f"ขบวนที่ {d.get_train_number} ประเภท {d.get_train_type}"),
            # A(Button("เลือก"),href='/train')
            Input(type="hidden", id="trainNumber", name="trainNumber",value=f"{d.get_train_number}"),   
            Input(type="hidden", id="departure_id", name="departure_id",value=f"{d.get_departure_id}"),   
            Button("เลือก", type="submit",style="width:80px;"),method="get",action="/train"
        ) 
    )

#แสดงหน้าการเลือกเที่ยวไป
@rt('/departure')
def search_departure(origin_station: str, detination_station: str, bookdate: parsed_date):
    departure = control.search_departure_by_origin_destination_data(origin_station,detination_station,"15/02/2568")
    print(bookdate.strftime(f"%m/%d/%Y"))
    if len(departure) > 0:
        return navigation_bar(),Container(Div("เลือกขบวนโดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/')),
                Hr(),
                Div(*[departure_card(d) for d in departure]),Style="padding-left:10%;padding-right:10%;")
    else:
        return navigation_bar(),Container(Div("เลือกขบวนโดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/')),
                Hr(),
                Div(H3("ไม่พบเที่ยวรถไฟ")),Style="padding-left:10%;padding-right:10%;")

def carriage_card(c,tn,d_id):
    return Card(
        Form(
            H3(f"{c.get_name} : รถโบกี้ {c.get_floor}"), 
            H4(f"{c.get_type} ผู้โดยสารทั่วไป"),
            H4(f"ราคา {c.get_price}"),
            # A(Button("เลือก"),href='/train')
            Input(type="hidden", id="carriage_id", name="carriage_id",value=f"{c.get_carriage_id}"),   
            Input(type="hidden", id="train_num", name="train_num", value=tn),   
            Input(type="hidden", id="departure_id", name="departure_id", value=d_id),   
            Button("เลือก", type="submit",style="width:80px;"),method="get",action="/seat"
        ) 
    )   

#แสดงหน้าการเลือก car
@rt('/train')
def get(trainNumber:str, departure_id:int):
    seat_id_list.clear()
    train = control.find_train_by_train_num(trainNumber)
    carriages = train.get_all_carriage()
    if len(carriages) > 0:
        return navigation_bar(),Container(Div(f"ขบวนที่ {trainNumber} เลือกตู้โดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/')),
                Hr(),
                Div(*[carriage_card(car,trainNumber,departure_id) for car in carriages], id="product-list"),Style="padding-left:10%;padding-right:10%;")


#ตรวจสอบว่าที่นั่งนั้นว่างรึเปล่า
def seat_select(seat,car_num):
    btn_disabled_style = """
            margin:2px;
            height:60px;
            width:60px;
            background-color: dimgrey;
            color: linen;
            opacity: 1;
            display:inline;
            """
    btn_active_style = """
            margin:2px;
            height:60px;
            width:60px;
            display:inline;
            """
    if seat.get_status == 'release':
        return Form(
                Input(id="seat_no", type="hidden", value=seat.get_seat_number),
                Input(id="passenger_name", type="hidden", value="ผู้โดยสาร"),
                Input(id="seat_type", type="hidden", value="ที่นั่ง"),
                Input(id="car_no", type="hidden", value=car_num),
                Input(id="price", type="hidden", value=seat.get_price),
                Button(f"{seat.get_seat_number}",style=btn_active_style),
                hx_post="/add",
                hx_target="#items",
                hx_swap="beforeend"
                ,style='display:inline')
    else:
        return Button(f"{seat.get_seat_number}",style=btn_disabled_style)
        

#แสดงหน้าการเลือกที่นั่ง
@rt('/seat')
def get(carriage_id:str,train_num:int,departure_id:int):
    seat_id_list.clear()
    global login
    if not login:
        return home()
    carriage = control.find_carriag_by_id(int(carriage_id))
    train = control.find_train_by_train_num(str(train_num))
    departure = control.find_departure_by_id(departure_id)
    carriage_list = train.get_all_carriage()
    carriage_num = None
    for i,car in enumerate(carriage_list):
        if carriage == car:
            carriage_num = i+1
    seats = carriage.get_all_seat()
    return Body(navigation_bar(),Hr(),
                Container(H3(f"เลือกที่นั่ง เที่ยวไป "),H4(f"ขบวนที่ {train.get_train_number} {train.get_train_type}"),
                    H4(f"{departure.get_origin_station} >>> {departure.get_destination_station}"),
                    H4(f"คันที่ {carriage_num} {carriage.get_name} : รถโบกี้ {carriage.get_floor} {carriage.get_type} ผู้โดยสารทั่วไป"),
                    Style="padding-left:10%;padding-right:10%;"),
                Container(*[seat_select(seat,carriage_num) for seat in seats],Style="padding-left:10%;padding-right:10%;"),
                Container(
                Table(
                Tr(
                    Th("ลำดับ"),
                    Th("ชื่อผู้โดยสาร"),
                    Th("ประเภทที่นั่ง"),
                    Th("คันที่"),
                    Th("เลขที่นั่ง"),
                    Th("ราคา"),
                    Th("ลบ"),
                )
                ,id="items"),style="margin-top:60px;padding-left:60px;padding-right:60px"),
                Container(
                    Form(
                        Input(id="train_num", type="hidden", value=str(train_num)),
                        Input(id="departure_id", type="hidden", value=int(departure_id)),
                        Input(id="carriage_id", type="hidden", value=int(carriage_id)),
                        Button("จอง", type="submit"),
                        method="get",action="/payment",
                        style="width:100%;padding-left:600px;padding-right:600px;"),
                ))
                

#เพิ่ม row เมื่อเลือกที่นั่ง
@rt('/add')
def post(seat_no:int, price:int,car_no:int, seat_type:str, passenger_name:str):
    if len(seat_id_list) == 4:
        return ""
    # สร้าง unique id สำหรับแต่ละ card
    seat_id = f"seat-{hash(seat_no)}"
    if seat_id in seat_id_list:
        return ""
    seat_id_list.append(seat_id)
    order = seat_id_list.index(seat_id) + 1
    return Tr(
                Td(f"{order}"),
                Td(f"ผู้โดยสารคนที่ {order}"),
                Td(f"{seat_type}"),
                Td(f"{car_no}"),
                Td(f"{seat_no}"),
                Td(f"{price}"),
                Td(Button("ลบ",
                hx_delete=f"/remove/{seat_id}",  # ส่ง id ไปกับ request
                hx_target=f"#{seat_id}",         # ระบุเป้าหมายด้วย id
                hx_swap="outerHTML",style="background-color: #f44336;height:60px;width:60px;"),
                ),id=seat_id)

#ลบที่นั่งจากการเลือก เมือกดปุ่ม "ลบ"
@rt('/remove/{card_id}')  
def delete(card_id: str):
    seat_id_list.remove(card_id)
    return ""

def ticket_card(seats,car,depar):
    return  Card(
                # H3("Text and Border Styles", style="color: #1976d2;"),
                Div(B("ตู้โดยสาร"),
                P(f"ชั้น {car.get_floor} นั่ง {car.get_type} ชนิด 75 ที่"),
                P(f"เที่ยวไป  ขบวนที่ {depar.get_train_number} ({depar.get_train_type})"),
                P(f"เส้นทาง  {depar.get_origin_station} - {depar.get_destination_station}"),
                P("26 ตุลาคม 2567"),Hr(),
                B("ค่าโดยสาร"),
                P(f"ที่นั่งจำนวน   x{len(seats)} {car.get_price} บาท"),Hr(),
                B(f"ยอดรวม  {(car.get_price*len(seats))} บาท"),style="font-size: 16px;line-height:1.8;text-align: left;"),
                style="""
                        width:500px;
                        border: 1px solid #aeb6bf;
                        border-radius: 5px;
                        padding: 20px;
                        margin: 10px;
                        background-color: #f5f5f5;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
                    """
                )

#แสดงลายละเอียดตั๋วและการชำระเงิน
@rt('/payment')
def get(carriage_id: int, departure_id:int,train_num:str):
    book_seats_no = [int(i[5]) for i in seat_id_list]
    print(book_seats_no)
    carriage = control.find_carriag_by_id(carriage_id)
    departure = control.find_departure_by_id(departure_id)
    # member = control.find_member_by_id(int(control.login_account_no))
    return Body(navigation_bar(),
            Container(
                H3(f'ข้อมูลการจองที่นั่ง ',A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/')),Hr(),
                # Card ที่ 1 - แสดงการจัดการ Text และ Border
                Grid(
                    ticket_card(book_seats_no,carriage,departure),
                    ),
                H3(f'ชำระเงิน',style='margin-top:50px;text-align:center;'),Hr(),
                Container(
                    Form(
                        Label("ช่องทางการชำระ:",
                            Select(
                                Option("QR Code", value="q_code"),
                                Option("Credit Card", value="c_card"),
                                id="transection")),
                        Input(id="train_num", type="hidden", value=str(train_num)),
                        Input(id="departure_id", type="hidden", value=int(departure_id)),
                        Input(id="carriage_id", type="hidden", value=int(carriage_id)),
                        Button("ยืนยันการจอง", type="submit",style="margin-top:50px;"),
                        # method="post",action="/booked"),
                        hx_post="/booked",hx_target="body", hx_swap="beforeend"),popup_style,
                    style="display:flex;justify-content:center;")))
               
payment_form =  Card(
                Label("ธนาคาร:",
                Select(
                    Option("Bank1", value="Bank1"),
                    Option("Bank2", value="Bank2"),
                    Option("Bank3", value="Bank3"),
                    id="bank")),
                Label("Card Number:", Input(type="text", id="card_num")),
                Label("Name on card:", Input(type="text", id="card_name")),
                Label("Expiry date:", Input(type="text", id="exp")),
                Label("Security code:", Input(type="text", id="s_code")),
                style="""margin-top: 20px;
                        width:100%;
                        margin-bottom: 50px;
                        padding: 20px;
                        border: 1px solid #aeb6bf;
                        border-radius: 5px;
                        padding: 20px;
                        background-color: #f5f5f5;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.5); """)
                                    
             
@rt('/transection')
def get(transection:str):
    if transection == "c_card":
        return payment_form


#popup ว่าทำการจองเสร็จสิ้นแล้ว
@rt('/booked')
def post(departure_id:int,carriage_id:int,train_num:str):
    member_id = control.get_login_member.get_member_id
    book_seats_no = [int(i[5]) for i in seat_id_list]
    control.booking_ticket(member_id,departure_id,train_num,carriage_id,book_seats_no)
    return Div(
            Div(
                H3("การจองเสร็จสิ้น"),
                Hr(),
                A(Button("ย้อนกลับ"),href="/"),
                cls="popup-content"
            ),
            id="popup", cls="popup"
        )

#แสดงลายละเอียด booking และ ticket
def booking_card(booking):
    ticket_list = booking.get_ticket
    departure = booking.get_departure
    train = departure.get_train
    return Card(
            H3(f"รหัสการจอง {booking.get_booking_id}"), 
            H4(f"ชำระแล้ว",style="color:green;"),  
            Style='''
                        border: 3px solid #aeb6bf;
                        border-radius: 5px;
            '''),*[Card(
                Grid(P(f"ตู้โดยสาร ขบวนที่ {ticket.train_num} ({ticket.car_type})"),P(f"เส้นทาง  {ticket.origin_station} - {ticket.destination_station}",Style="text-align:right")),
                Grid(P(f"ชั้น {ticket.car_floor} ประเภท บทศ{ticket.car_name} คันที่ {train.get_car_order(ticket.get_carriage)} เลขที่นั่ง {ticket.seat_num}"),P(f"{ticket.date} | {ticket.time}",Style="text-align:right")),
                P(f"ราคา {ticket.price} บาท"),
                P(f"รหัสตั๋ว {ticket.get_ticket_id}"),
                Style="margin-left:100px;padding-left:40px;padding-right:40px;"
            ) for ticket in ticket_list]
        
#หน้าจอประวัติการซื้อ
@rt('/booking')
def get():
    booking_list = control.get_booking_member()
    if booking_list == []:
        return Body(navigation_bar(),
                Container(H1("ประวัติการซื้อ"),Hr(),P("ไม่พบประวัติการซื้อ"),
                Style="padding-left:10%;padding-right:10%;"))
    else:
        return Body(
            navigation_bar(),
            Container(
                H1("ประวัติการซื้อ"),Hr(),
                Container(
                *[booking_card(booking) for booking in reversed(booking_list)]
            ),Style="padding-left:10%;padding-right:10%;")
        )

#หน้าจอเลือกตั๋วเพื่อยกเลิกการจอง
@rt('/cancel')
def get():
    booking_list = control.get_booking_member()
    if booking_list == []:
        return Body(navigation_bar(),
                Container(H1("การซื้อตั๋วทั้งหมด"),Hr(),P("ไม่พบประวัติการซื้อตั๋ว"),
                Style="padding-left:10%;padding-right:10%;"))
    else:
        tickets_list = []
        for booking in booking_list:
            for ticket in booking.get_ticket:
                tickets_list.append(ticket)
        print(tickets_list)
        return Body(navigation_bar(),
                    Container(
                        H1("การซื้อตั๋วทั้งหมด"),Hr(),
                        *[Card(
                            Grid(P(f"ตู้โดยสาร ขบวนที่ {ticket.train_num} ({ticket.car_type})"),P(f"เส้นทาง  {ticket.origin_station} - {ticket.destination_station}",Style="text-align:right")),
                            Grid(P(f"ชั้น {ticket.car_floor} ประเภท บทศ{ticket.car_name} เลขที่นั่ง {ticket.seat_num}"),P(f"{ticket.date} | {ticket.time}",Style="text-align:right")),
                            P(f"ราคา {ticket.price} บาท"),
                            P(f"รหัสตั๋ว {ticket.get_ticket_id}"),
                            Style="margin-left:100px;padding-left:40px;padding-right:40px;") for ticket in tickets_list],
                    Style="padding-left:10%;padding-right:10%;"))

serve()