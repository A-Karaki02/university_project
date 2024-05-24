from datetime import datetime

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
        self.basket = []
        self.db_basket = []

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
        self.__HistoryNum = users["itemsHistoryNumber"]

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
        self.__items_number = self.__items_number + 1
        if (
            self.dtbs.child("items")
            .child(self.__UID)
            .child(self.__items_number)
            .set(item)
        ):
            self.dtbs.child("users").child(self.__UID).update(
                {"itemsNumber": self.__items_number}
            )
            return True
        else:
            return False

    def is_supplier(self):
        return self.__is_supplier

    def get_store_name(self):
        return self.__store_name

    def add_to_basket(
        self, storeKey, itemKey, storeName, itemName, itemType, price, quantity
    ):
        self.basket.append(
            {
                "storeKey": storeKey,
                "itemNumber": itemKey,
                "storeName": storeName,
                "itemName": itemName,
                "itemType": itemType,
                "price": price,
                "quantity": quantity,
            }
        )
        print(self.basket)

    def add_to_db_basket(self, key, itemNum):
        self.db_basket.append([key, itemNum])
        print(self.db_basket)

    def get_basket(self):
        return self.basket

    def get_basket_items(self):
        return self.basket

    def get_item_index(self, key, itemNum):
        index = 0
        for item in self.db_basket:
            if key == item[0] and itemNum == item[1]:
                return index
            index += 1

    def remove_item_from_basket(self, key, itemNum):
        index = self.get_item_index(key, itemNum)
        del self.db_basket[index]
        del self.basket[index]
        print(self.basket)
        print(self.db_basket)

    def edit_user(self, firstName, lastName, userName, phoneNumber, storeName):
        if firstName != "":
            self.dtbs.child("users").child(self.__UID).update({"firstName": firstName})
        if lastName != "":
            self.dtbs.child("users").child(self.__UID).update({"lastName": lastName})
        if phoneNumber != "":
            self.dtbs.child("users").child(self.__UID).update(
                {"phoneNumber": phoneNumber}
            )
        if storeName != "":
            self.dtbs.child("users").child(self.__UID).update(
                {"supplierName": storeName}
            )
        if userName != "":
            self.dtbs.child("users").child(self.__UID).update({"userName": userName})

    def passwordReset(self, email):
        if email:
            self.__auth.send_password_reset_email(email)
        elif self.__email:
            self.__auth.send_password_reset_email(self.__email)

    def checkout_items(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        itemsHistoryNumber_ref = (
            self.dtbs.child("users").child(self.__UID).child("itemsHistoryNumber")
        )

        # Fetch the current itemsHistoryNumber value
        itemsHistoryNumber = itemsHistoryNumber_ref.get().val()

        for item in self.basket:
            print(item)
            seller = item["storeKey"]

            itemsHistoryNumber += 1

            appendedItem = {
                "storeKey": item["storeKey"],
                "itemNumber": itemsHistoryNumber,
                "storeName": item["storeName"],
                "itemName": item["itemName"],
                "itemType": item["itemType"],
                "price": item["price"],
                "quantity": item["quantity"],
                "time": dt_string,
                "isPurchased": True,
            }

            # Append item to user's history
            self.dtbs.child("History").child(self.__UID).child("itemsHistory").child(
                itemsHistoryNumber
            ).set(appendedItem)

            # Increment seller's itemsHistoryNumber
            items_number_ref_seller = (
                self.dtbs.child("users").child(seller).child("itemsHistoryNumber")
            )
            items_number = items_number_ref_seller.get().val()

            items_number += 1

            self.dtbs.child("users").child(seller).update(
                {"itemsHistoryNumber": items_number}
            )

            # Append item to seller's history

            appendedItem["isPurchased"] = False
            appendedItem["itemNumber"] = items_number
            (
                self.dtbs.child("History")
                .child(seller)
                .child("itemsHistory")
                .child(items_number)
                .set(appendedItem)
            )

            # Update the item's quantity if the quantity is 0 remove it

        # Update the user's itemsHistoryNumber
        self.dtbs.child("users").child(self.__UID).update(
            {"itemsHistoryNumber": itemsHistoryNumber}
        )

        # Clear the user's basket after checkout
        self.basket.clear()

    def fetch_history(self):
        try:
            data = self.dtbs.child("History").child(self.__UID).get().val()
            print(
                f"Data fetched from Firebase: {data}"
            )  # Debug print to check the data structure

            if data is None:
                print("No data found in the Firebase database.")
                return []

            items = []

            if isinstance(data, dict):
                for person_key, person_items in data.items():
                    if isinstance(person_items, dict):
                        for item_number, item_data in person_items.items():
                            item_data["personKey"] = person_key
                            item_data["itemNumber"] = item_number
                            items.append(item_data)
                    elif isinstance(person_items, list):
                        for index, item_data in enumerate(person_items):
                            if item_data is not None:  # Filter out None values
                                item_data["personKey"] = person_key
                                item_data["itemNumber"] = index
                                items.append(item_data)
            elif isinstance(data, list):
                for index, person_items in enumerate(data):
                    if isinstance(person_items, dict):
                        for item_number, item_data in person_items.items():
                            item_data["personKey"] = index
                            item_data["itemNumber"] = item_number
                            items.append(item_data)
                    elif isinstance(person_items, list):
                        for item_index, item_data in enumerate(person_items):
                            if item_data is not None:  # Filter out None values
                                item_data["personKey"] = index
                                item_data["itemNumber"] = item_index
                                items.append(item_data)
            else:
                print("Unexpected data structure from Firebase.")
                return []

            return items
        except Exception as e:
            print(f"Error fetching data from Firebase: {e}")
            return []

    def add_to_purchased_items(self, key, itemNum):
        pass

    def token_expiry(self):
        pass

    def update_info(self):
        pass


user = UserManager()
