from DataBase import DataBase as db


class UserManager:

    def __init__(self):
        self._user = ""
        self._token = ""
        self._user_info = ""
        self._UID = ""
        self._auth = db.auth
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
            print(self._UID)
            return True
        else:
            return False

    def Logout(self):
        self._user = ""
        self._token = ""
        self._user_info = ""

    def token_expiry(self):
        pass

    def update_info(self):
        pass


user = UserManager()
