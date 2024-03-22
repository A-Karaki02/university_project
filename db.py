import pyrebase
from firebase import Firebase 
Config = {
  "apiKey": "AIzaSyDq18MssqgcK8FFiGABLBoxh439mEADbn4",
  "authDomain": "buildsmart-9c980.firebaseapp.com",
  "databaseURL": "https://buildsmart-9c980-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "buildsmart-9c980",
  "storageBucket": "buildsmart-9c980.appspot.com",
  "messagingSenderId": "874619547397",
  "appId": "1:874619547397:web:e4c18ea945419d4c91916c",
  "measurementId": "G-2YER9KMH08"
}
firebase = pyrebase.initialize_app(Config)
firebase = Firebase(Config)


db = firebase.database()
dat =  {"name " :"john" ,
         'id ': '1'
        }
db.push(dat)
db.child("Data").set(dat)
