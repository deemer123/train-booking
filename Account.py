from Booking import Booking

class Account:
    account_id = 0
    def __init__(self,name,email,role,phone_number,password):
        Account.account_id += 1
        self.__account_id = Account.account_id
        self.__name = name
        self.__email = email
        self.__role = role
        self.__phone_number = phone_number
        self.__password = password
    
    @property
    def get_account_id(self):
        return self.__account_id  
    @property
    def get_name(self):
        return self.__name  
    @property
    def get_email(self):
        return self.__email  
    @property
    def get_role(self):
        return self.__role  
    @property
    def get_phone_number(self):
        return self.__phone_number
    @property
    def get_password(self):
        return self.__password  






class Admin(Account):
    admin_id = 0
    def __init__(self,name,email,role,phone_number,password):
        super().__init__(name,email,role,phone_number,password)
        Admin.admin_id += 1
        self.__admin_id = Admin.admin_id      





