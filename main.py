from fastapi import FastAPI
from Controller import Controller
from typing import Union

app = FastAPI()
control = Controller()


@app.get('/tickets')
def home(mem_id:str,book_id:str,ticker_id:str):
    stations_list = control.get_all_station_name()
    ticket_info = control.ticket_info(int(mem_id),int(book_id),int(ticker_id))
    return {"Stations":stations_list,"Ticket_data":ticket_info}

@app.get('/login')
def login(email:str,password:str):
    return 

@app.post('/register')
def register():
    pass

@app.get('/search')
def get(org:str,des:str,date:str):
    pass

@app.get('/search/car')
def get(depar_id:int,train:int):
    pass

@app.get('/search/car/seat')
def get(depar_id:int,train:int,car:str):
    pass

@app.post('/booked')
def booked_ticket():
    pass

@app.delete('')
def del_ticket():
    pass