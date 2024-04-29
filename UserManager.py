from DataBase import DataBase as db


class UserManager:

    def __init__(self):
        self._auth = db.auth
        self._user = ""
        self._token = ""
        self._user_info = ""
        self._UID = ""
        self._email = ""
        self._username = ""
        self._first_name = ""
        self._last_name = ""
        self._phonenumber = ""

    def get_user(self):
        return self._user

    def set_user(self, email, password):
        self._user = self._auth.sign_in_with_email_and_password(email, password)
        if self._user:
            self._token = self._user["idToken"]
            self._UID = self._user["localId"]
            self._user_info = db.auth.get_account_info(self._token)
            self.set_user_info()
            return True
        else:
            return False

    def set_user_info(self):
        users = db.database.child("users").child(self._UID).get().val()
        self._email = users["email"]
        self._username = users["userName"]
        self._first_name = users["firstName"]
        self._last_name = users["lastName"]
        self._phonenumber = users["phoneNumber"]
        # print(self._email)
        # print(self._username)
        # print(self._first_name)
        # print(self._last_name)
        # print(self._phonenumber)

    def Logout(self):
        self._user = ""
        self._token = ""
        self._user_info = ""
        self._UID = ""
        self._email = ""
        self._username = ""
        self._first_name = ""
        self._last_name = ""
        self._phonenumber = ""

    def token_expiry(self):
        pass

    def update_info(self):
        pass


user = UserManager()
