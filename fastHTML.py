from fasthtml.common import *
from Controller import Controller
from datetime import datetime


app,rt = fast_app()

control = Controller()
login = False
login_id = None
seat_id_list = []

# css stylesheet ของ popup
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
            }}""")

# แถบเมนูที่แสดงบนหน้าเว็บ
def navigation_bar():
    if not login:
        return Container(Nav(
            Ul(
                Li(H5(A("หน้าแรก",href="/"))),
                Li(H5(A("ประวัติการซื้อ", hx_get="/login-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                Li(H5(A("ยกเลิกตั๋วโดยสาร", hx_get="/login-popup", hx_target="body", hx_swap="beforeend"),popup_style)),
                Li(H5(A("ศูนย์ความช่วยเหลือ",href="/HelpCenter"))),
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
                Li(H5(A("ศูนย์ความช่วยเหลือ",href="/HelpCenter"))),
                style="text-align:left;"
            ),
            Ul(
                Li(H5(f"{control.get_login_member.get_name}")),
                Li(H5(A("ออกจากระบบ",href="/logout"))),
                style="text-align:right;"
            )))
    
@rt("/HelpCenter")
def page():
    return  Body(navigation_bar(),
                 Container(Div(H1("ศูนย์ความช่วยเหลือ")),Hr(),
                     Grid(Card(
                         Button("วิธีการจองตั๋วโดยสาร",style="width:100%;height:60px;margin-bottom:10px;"),
                         Button("วิธีการยกเลิกตั๋วโดยสาร",style="width:100%;height:60px;margin-bottom:10px;"),
                         Button("สมัครสมาชิก",style="width:100%;height:60px;margin-bottom:10px;"),
                         Button("คำถามที่พบบ่อย",style="width:100%;height:60px;margin-bottom:10px;"),
                     ),Card("",Style="width:100%;"),Style="grid-template-columns: 1fr 3fr;"),
                     
    Style="padding-left:10%;padding-right:10%;"))
    
# แสดงหน้าการเข้าสู่ระบบ
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

# แสดงหน้าการสมัครสมาชิก
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
    
# ทำการเข้าสู่ระบบ        
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
    
# ทำการออกจากระบบ    
@rt("/logout")
def logout():
    control.logout()
    global login 
    login = False
    return home()

# นำข้อมูลการสมัครสมาชิกเข้าสู่ระบบ
@rt("/register")
def post(email:str,password:str, phone_number:str , name:str):
    control.register(name,email,phone_number,password)
    print("Register Sucess")
    return  home()

#หน้า home
@rt('/')
def home():
    seat_id_list.clear()
    station_name = control.get_all_station_name()
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
            Container(
                    Form(
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
                        Input(type="date", id="bookdate", name="bookdate" ,value = datetime.today().strftime("%Y-%m-%d"))    
                    ),
                    Button("ค้นหา", type="submit"),
                    method="get",
                    action="/departure"
                ),id="results")    
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
                method="get",
                action="/departure"
            )

# การ์ดแสดงรายละเอียดเที่ยวรถ
def departure_card(d,ori,des,date):
    return Card(
        Form(
            H3(f"เวลาออก {d["departure_time"]} - เวลาถึง {d["arrival_time"]}"), 
            H4(f"ขบวนที่ {d["train_num"]} ประเภท {d["train_type"]}"),
            Input(type="hidden", id="train_num", name="train_num",value=f"{d["train_num"]}"),   
            Input(type="hidden", id="ori", name="ori",value=f"{ori}"),   
            Input(type="hidden", id="des", name="des",value=f"{des}"),   
            Input(type="hidden", id="date", name="date",value=f"{date}"),   
            Button("เลือก", type="submit",style="width:80px;"),method="get",action="/train"
        ) 
    )


#แสดงหน้าการเลือกเที่ยวรถ
@rt('/departure')
def search_departure(origin_station: str, detination_station: str, bookdate: parsed_date):
    match_departure = control.search_departure(origin_station,detination_station,"15/02/2568")
    # print(bookdate.strftime(f"%m/%d/%Y"))
    if len(match_departure) > 0:
        return navigation_bar(),Container(Div(H1("เลือกขบวนโดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/'))),
                Hr(),
                Div(*[departure_card(departure,origin_station,detination_station,bookdate) for departure in match_departure]),Style="padding-left:10%;padding-right:10%;")
    else:
        return navigation_bar(),Container(Div(H1("เลือกขบวนโดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/'))),
                Hr(),
                Div(H3("ไม่พบเที่ยวรถไฟ")),Style="padding-left:10%;padding-right:10%;")
    

# การ์ดแสดงลายละเอียดตู้รถโบกี้
def carriage_card(car,train_num,ori,des,date):
    if car["status"] == "booked":
        return Card(
                H3(f"{car['carrige_name']} : รถโบกี้ ชั้น: {car['floor']}"), 
                H4(f"{car['room_type']} ผู้โดยสารทั่วไป ประเภท {car['seat_type']}"),
                H4(f"ราคา {car['price']} บาท"),
                Button("เลือก",Style="background-color:#A9A9A9;width:80px;color: linen;"),Style="background-color:#D3D3D3;")
    else:  
        return Card(
            Form(
                H3(f"{car['carrige_name']} : รถโบกี้ ชั้น: {car['floor']}"), 
                H4(f"{car['room_type']} ผู้โดยสารทั่วไป ประเภท {car['seat_type']}"),
                H4(f"ราคา {car['price']} บาท"),
                # A(Button("เลือก"),href='/train')
                Input(type="hidden", id="carriage_id", name="carriage_id",value=f"{car['carrige_id']}"),   
                Input(type="hidden", id="train_num", name="train_num", value=train_num),   
                Input(type="hidden", id="ori", name="ori", value=ori),   
                Input(type="hidden", id="des", name="des", value=des),   
                Input(type="hidden", id="date", name="date", value=date),   
                Input(type="hidden", id="price", name="price", value= car['price']),   
                # Input(type="hidden", id="departure_id", name="departure_id", value=""),   
                Button("เลือก", type="submit",style="width:80px;"),method="get",action="/seat"))   


# แสดงหน้าการเลือกตู้รถโบกี้
@rt('/train')
def get(train_num:str,ori:str,des:str,date:str):
    seat_id_list.clear()
    # carriages_list = control.get_carriages_list_by_train_num(train_num)
    carriages_list = control.show_carriage(train_num,ori,des,date[:10])
    if len(carriages_list) > 0:
        return navigation_bar(),Container(Div(H1(f"ขบวนที่ {train_num} เลือกตู้โดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/'))),
                Hr(),
                Div(*[carriage_card(car,train_num,ori,des,date) for car in carriages_list], id="product-list"),Style="padding-left:10%;padding-right:10%;")
    else:
        return navigation_bar(),Container(Div(H1(f"ขบวนที่ {train_num} เลือกตู้โดยสาร เที่ยวไป",A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/'))),
                Hr(),Div(H3("ไม่พบตู้โบกี้")),Style="padding-left:10%;padding-right:10%;")


#ตรวจสอบว่าที่นั่งนั้นว่างรึเปล่าและแสดงปุ่มเลือกที่นั่ง
def seat_select(seat,car_num,price,seat_type):
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
                Input(id="seat_type", type="hidden", value= seat_type),
                Input(id="car_no", type="hidden", value=car_num),
                Input(id="price", type="hidden", value= price),
                Button(f"{seat.get_seat_number}",style=btn_active_style),
                hx_post="/add",
                hx_target="#items",
                hx_swap="beforeend"
                ,style='display:inline')
    else:
        return Button(f"{seat.get_seat_number}",style=btn_disabled_style)
        

#แสดงหน้าการเลือกที่นั่ง
@rt('/seat')
def get(carriage_id:str,train_num:str,ori:str,des:str,date:str,price:float):
    control.set_seat_booked(date[:10],int(carriage_id))
    seat_id_list.clear()
    global login
    if not login:
        return home()
    carriage = control.find_carriag_by_id(int(carriage_id))
    train = control.find_train_by_train_num(str(train_num))
    carriage_list = train.get_all_carriage()
    carriage_num = None
    for i,car in enumerate(carriage_list):
        if carriage == car:
            carriage_num = i+1
    seats_list = carriage.get_all_seat()
    return Body(navigation_bar(),
                Container(H1(f"เลือกที่นั่ง เที่ยวไป "),Hr(),H4(f"ขบวนที่ {train.get_train_number} {train.get_train_type}"),
                    H4(f"{ori} >>> {des}"),
                    H4(f"คันที่ {carriage_num} {carriage.get_name} : รถโบกี้ {carriage.get_floor} {carriage.get_type} ผู้โดยสารทั่วไป"),
                    Style="padding-left:10%;padding-right:10%;"),
                Div(id="alert", style="color: red; text-align: center;"),  # เพิ่มพื้นที่แจ้งเตือน
                Container(*[seat_select(seat,carriage_num,price,carriage.get_seat_type) for seat in seats_list],Style="padding-left:10%;padding-right:10%;"),
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
                        Input(id="carriage_id", type="hidden", value=int(carriage_id)),
                        Input(type="hidden", id="ori", name="ori", value=ori),   
                        Input(type="hidden", id="des", name="des", value=des),   
                        Input(type="hidden", id="date", name="date", value=date),
                        Input(type="hidden", id="price", name="price", value=price),
                        Button("จอง", type="submit"), 
                        # hx_post="/validate_selection", 
                        # hx_target="#alert", 
                        # hx_swap="innerHTML",
                        method="get",action="/payment",
                        style="width:100%;padding-left:600px;padding-right:600px;"),
                ))
                
@rt('/validate_selection')
def post(carriage_id: int,train_num:str,ori:str,des:str,date:str,price:float):
    price(carriage_id,train_num,ori,des,date,price)
    if len(seat_id_list) == 0:  # ตรวจสอบว่ามีการเลือกที่นั่งหรือไม่
        return H3("กรุณาเลือกที่นั่งก่อนทำการจอง", style="color: red; text-align: center;")
    return H3("ดำเนินการจองได้", style="color: green; text-align: center;")



#เพิ่ม row เมื่อเลือกที่นั่ง
@rt('/add')
def post(seat_no:int, price:float,car_no:int, seat_type:str, passenger_name:str):
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
                Td(f"{int(price)}"),
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

# การ์ดแสดงลายละเอียดตั๋ว
def ticket_card(seats,car,train_num,ori,des,date,price):
    train = control.find_train_by_train_num(train_num)
    return  Card(
                # H3("Text and Border Styles", style="color: #1976d2;"),
                Div(B("ตู้โดยสาร"),
                P(f"ชั้น {car.get_floor} นั่ง {car.get_type} ชนิด {car.get_seat_amount} ที่"),
                P(f"เที่ยวไป  ขบวนที่ {train_num} ({train.get_train_type})"),
                P(f"เส้นทาง  {ori} - {des}"),
                P(f"วันที่ {date[:10]}"),Hr(),
                B("ค่าโดยสาร"),
                P(f"ที่นั่งจำนวน   x{len(seats)} {price} บาท"),Hr(),
                B(f"ยอดรวม  {price*len(seats)} บาท"),style="font-size: 16px;line-height:1.8;text-align: left;"),
                style="""
                        width:500px;
                        border: 1px solid #aeb6bf;
                        border-radius: 5px;
                        padding: 20px;
                        margin: 10px;
                        background-color: #f5f5f5;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.5);""")


#แสดงลายละเอียดตั๋วและการชำระเงิน
@rt('/payment')
def get(carriage_id: int,train_num:str,ori:str,des:str,date:str,price:float):
    book_seats_no = [int(seat[5:]) for seat in seat_id_list]
    print(book_seats_no)
    carriage = control.find_carriag_by_id(carriage_id)
    # departure = control.find_departure_by_id(departure_id)
    member = control.find_member_by_id(int(control.login_account_no))
    return Body(navigation_bar(),
            Container(
                H3(f'ข้อมูลการจองที่นั่ง ',A(Button("เปลี่ยนแปลงการค้นหา",style="margin-left:50px"),href='/')),Hr(),
                # Card ที่ 1 - แสดงการจัดการ Text และ Border
                Grid(
                    ticket_card(book_seats_no,carriage,train_num,ori,des,date,price),
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
                        Input(id="carriage_id", type="hidden", value=int(carriage_id)),
                        Input(type="hidden", id="ori", name="ori", value=ori),   
                        Input(type="hidden", id="des", name="des", value=des),   
                        Input(type="hidden", id="date", name="date", value=date),
                        Input(type="hidden", id="price", name="price", value=price),   
                        Button("ยืนยันการจอง", type="submit",style="margin-top:50px;"),
                        # method="post",action="/booked"),
                        hx_post="/booked",hx_target="body", hx_swap="beforeend"),popup_style,
                    style="display:flex;justify-content:center;")))
               


#popup ว่าทำการจองเสร็จสิ้นแล้ว
@rt('/booked')
def post(carriage_id:int,train_num:str,ori:str,des:str,date:str,price:float):
    member_id = control.get_login_member.get_member_id
    member = control.get_login_member
    book_seats_no = [int(seat[5:]) for seat in seat_id_list]
    booking = control.booked_ticket(member_id,train_num,carriage_id,book_seats_no,ori,des,date[:10],price)
    return Div(
            Div(
                H3(f"การจองเสร็จสิ้น"),
                Hr(),
                A(Button("ย้อนกลับ"),href="/"),
                cls="popup-content"
            ),
            id="popup", cls="popup"
        )


# การ์ดแสดงลายละเอียด booking และ ticket
def booking_card(booking):
    ticket_list = booking.get_ticket
    train = booking.get_train
    return Card(
            H3(f"รหัสการจอง {booking.get_booking_id}"), 
            H4(f"ชำระแล้ว",style="color:green;"),  
            Style='''
                        border: 3px solid #aeb6bf;
                        border-radius: 5px;
            '''),*[Card(
                Grid(P(f"ตู้โดยสาร ขบวนที่ {ticket.train_num} ({ticket.car_type})"),P(f"{ticket.origin_station} - {ticket.destination_station}",Style="text-align:right")),
                Grid(P(f"ชั้น {ticket.car_floor} ประเภท {ticket.car_name} คันที่ {train.get_car_order(ticket.get_carriage)} เลขที่นั่ง {ticket.seat_num}"),P(f"{ticket.date} | {ticket.departure_time}-{ticket.arrival_time}",Style="text-align:right")),
                P(f"ราคา {int(ticket.price)} บาท"),
                P(f"รหัสตั๋ว {ticket.get_ticket_id}"),
                Style="margin-left:100px;padding-left:40px;padding-right:40px;"
            ) for ticket in ticket_list]
        

#หน้าจอประวัติการซื้อ
@rt('/booking')
def get():
    member = control.get_login_member
    booking_list = member.get_all_booking
    print(booking_list)
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


#หน้าจอเลือกตั๋วเพื่อยกเลิกตั๋ว
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
                            Grid(P(f"ตู้โดยสาร ขบวนที่ {ticket.train_num} ({ticket.car_type})"),P(f"{ticket.origin_station} - {ticket.destination_station}",Style="text-align:right")),
                            Grid(P(f"ชั้น {ticket.car_floor} ประเภท บทศ{ticket.car_name} เลขที่นั่ง {ticket.seat_num}"),P(f"{ticket.date} | {ticket.departure_time} - {ticket.arrival_time}",Style="text-align:right")),
                            P(f"ราคา {ticket.price} บาท"),
                            Grid(P(f"รหัสตั๋ว {ticket.get_ticket_id}"),
                            Form(
                                Button("ยกเลิก",
                                hx_delete=f"/delete/ticket-{ticket.get_ticket_id}",  # ส่ง id ไปกับ request
                                hx_target=f"#ticket-{ticket.get_ticket_id}",         # ระบุเป้าหมายด้วย id
                                hx_swap="outerHTML"
                            ),style="text-align:right;")),
                            Style="margin-left:100px;padding-left:40px;padding-right:40px;",id= f"ticket-{ticket.get_ticket_id}") for ticket in tickets_list],
                    Style="padding-left:10%;padding-right:10%;"))


# ลบตั๋วโดยใช้ ticket_id
@rt('/delete/ticket-{ticket_id}')
def delete(ticket_id:int):
    print(control.cancel_ticket(ticket_id))
    print(f"delete ID:{ticket_id}")

    
serve()