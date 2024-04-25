class Person:

    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password):
        self._ID = ID
        self._F_Name = F_Name
        self._L_Name = L_Name
        self._Email = Email
        self._phone_number = phone_number
        self._username = username
        self._password = password

    def set_ID(self, id):
        self._ID = id

    def set_name(self, first_name, last_name):
        self._F_Name = first_name
        self._L_Name = last_name

    def set_Email(self, Email):
        self._Email = Email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def get_ID(self):
        return self._ID

    def get_name(self):
        return self._F_Name, self._L_Name

    def get_Email(self):
        return self._Email

    def get_phone_number(self):
        return self._phone_number

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password


class supplier(Person):
    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password, supp_ID):
        super().__init__(ID, F_Name, L_Name, Email, phone_number, username, password, supp_ID)
    
    
class customer(Person):
    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password,cus_ID):
        super().__init__(ID, F_Name, L_Name, Email, phone_number, username, password,cus_ID)
        

class Items:
    def __init__(self, item_ID, item_name, Price, description):
        self.item_ID = item_ID
        self.item_name = item_name
        self.Price = Price
        self.description = description
        
        
    def set_item_ID(self, item_ID):
        self._item_ID = item_ID   
    
    def set_item_name(self, item_name):
        self._item_name = item_name
            
    def set_price(self, price):
        self._price = price
    
    def set_description(self, description):
        self._description = description    

    def get_item_ID(self):
        return self._item_ID
    
    def get_item_name(self):
        return self._item_name

    def get_price(self):
        return self._price
       
    def get_description(self):
        return self._description

# class Cart: