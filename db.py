import pyrebase


Config = {
    "apiKey": "AIzaSyDq18MssqgcK8FFiGABLBoxh439mEADbn4",
    "authDomain": "buildsmart-9c980.firebaseapp.com",
    "databaseURL": "https://buildsmart-9c980-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "buildsmart-9c980",
    "storageBucket": "buildsmart-9c980.appspot.com",
    "messagingSenderId": "874619547397",
    "appId": "1:874619547397:web:e4c18ea945419d4c91916c",
    "measurementId": "G-2YER9KMH08",
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()


db = firebase.database()
dat = {"name ": "john", "id ": "1"}
db.push(dat)
db.child("Data").set(dat)


def login():
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        print(auth.get_account_info(login['idToken']))
        email = auth.get_account_info(login['idToken'])['users'][0]['email']
        print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

