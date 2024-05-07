from DataBase import DataBase as db


class UserManager:

    def __init__(self):
        self.__auth = db.auth
        self.__user = ""
        self.__token = ""
        self.__user_info = ""
        self.__UID = ""
        self.__email = ""
        self.__username = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__phonenumber = ""
        self.__is_supplier = False
        self.__store_name = ""
        self.dtbs = db.firebase.database()

    def get_user(self):
        return self.__user

    def get_user_UID(self):
        return self.__UID

    def set_user(self, email, password):
        self.__user = self.__auth.sign_in_with_email_and_password(email, password)
        if self.__user:
            self.__token = self.__user["idToken"]
            self.__UID = self.__user["localId"]
            self.__user_info = db.auth.get_account_info(self.__token)
            self.set_user_info()
            return True
        else:
            return False

    def set_user_info(self):
        users = db.database.child("users").child(self.__UID).get().val()
        self.__email = users["email"]
        self.__username = users["userName"]
        self.__first_name = users["firstName"]
        self.__last_name = users["lastName"]
        self.__phonenumber = users["phoneNumber"]
        self.__is_supplier = users["isSupplier"]
        self.__store_name = users["supplierName"]
        self.__items_number = users["itemsNumber"]

        # print(self._email)
        # print(self._username)
        # print(self._first_name)
        # print(self._last_name)
        # print(self._phonenumber)

    def get_username(self):
        return self.__username

    def Logout(self):
        self.__user = ""
        self.__token = ""
        self.__user_info = ""
        self.__UID = ""
        self.__email = ""
        self.__username = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__phonenumber = ""
        self.__items_number = -1


    def add_item(self, item):
        new_number = self.__items_number + 1
        if self.dtbs.child("items").child(self.__UID).child(new_number).set(item):
            self.dtbs.child("users").child(self.__UID).update({"itemsNumber": new_number})
            return True
        else:
            return False

    def is_supplier(self):
        return self.__is_supplier

    def get_store_name(self):
        return self.__store_name

    def token_expiry(self):
        pass

    def update_info(self):
        pass


user = UserManager()
