import pyrebase

config = {
        "apiKey": "AIzaSyC0p2g1RRm121F6JR_inekorejofB7OY28",
        "authDomain": "test-ya-hanna.firebaseapp.com",
        "databaseURL": "https://test-ya-hanna-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "test-ya-hanna",
        "storageBucket": "test-ya-hanna.appspot.com",
        "messagingSenderId": "499440260295",
        "appId": "1:499440260295:web:bbbe79252214ccbe9bdae2",
        "measurementId": "G-SYQKG6EW7P"}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
stream_id = "Setting up"
#user = db.child("Motion").get()
#print(user.val())
def stream_handler(message):
     print( "changed to :" + message["data"]) # put
     #print(message["path"]) # /-K7yGTTEp7O549EzTYtI
     #print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("Motion").stream(stream_handler, stream_id = "Motion")
my_stream = db.child("Mot").stream(stream_handler, stream_id = "Mot")
my_stream = db.child("Topic").stream(stream_handler, stream_id = "Topic")
