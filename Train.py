from Carriage import Carriage

class Train:
     def  __init__(self,train_number,type):
          self.__train_number = train_number
          self.__type = type
          self.__carriage = []
          self.status = "release"
     @property
     def get_train_number(self):
          return self.__train_number
     @property
     def get_carriag(self):
          return self.__carriage
     @property
     def get_train_type(self):
          return self.__type


     def get_all_carriage(self):
          return [car for car in self.__carriage]

     def append_carriage(self,carriage):
            if isinstance(carriage, Carriage):
                self.__carriage.append(carriage)

     def get_car_order(self,car):
          carriage_order = 0
          for i,c in enumerate(self.__carriage):
               if car == c:
                    carriage_order = i+1
          return carriage_order


     def set_available(self):
          pass
     
     def set_fully_booked(self):
          pass



