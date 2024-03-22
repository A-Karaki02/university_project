class Person:

    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password):
        self.__ID = ID
        self.__F_Name = F_Name
        self.__L_Name = L_Name
        self.__Email = Email
        self.__phone_number = phone_number
        self.__username = username
        self.__password = password

    def set_ID(self, id):
        self.__ID = id

    def set_name(self, first_name, last_name):
        self.__F_Name = first_name
        self.__L_Name = last_name

    def set_Email(self, Email):
        self.__Email = Email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__F_Name, self.__L_Name

    def get_Email(self):
        return self.__Email

    def get_phone_number(self):
        return self.__phone_number

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class supplier(Person):
    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password, supp_ID):
        super().__init__(ID, F_Name, L_Name, Email, phone_number, username, password, supp_ID)
    
    
class customer(Person):
    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password,cus_ID):
        super().__init__(ID, F_Name, L_Name, Email, phone_number, username, password,cus_ID)
        

class items:
    def __init__(self, item_ID, item_name, Price, description):
        self.item_ID = item_ID
        self.item_name = item_name
        self.Price = Price
        self.description = description
        
    
    