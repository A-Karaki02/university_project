class Person:

    def __init__(self, ID, F_Name, L_Name, Email, phone_number, username, password):
        self._ID = ID
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Email = Email
        self.phone_number = phone_number
        self.username = username
        self.password = password

    def set_ID(self, id):
        self._ID = id

    def set_name(self, first_name, last_name):
        self.F_Name = first_name
        self.L_Name = last_name

    def set_Email(self, Email):
        self.Email = Email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_ID(self):
        return self._ID

    def get_name(self):
        return self.F_Name, self.L_Name

    def get_Email(self):
        return self.Email

    def get_phone_number(self):
        return self.phone_number

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


# class supplier(Person):
