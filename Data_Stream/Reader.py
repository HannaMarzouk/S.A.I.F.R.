import pyrebase
config = {
    "apiKey": "AIzaSyArr_N_bfnhw143Sm0kBjKBlDdsJzj7NzQ",
    "authDomain": "saifr-3c037.firebaseapp.com",
    "databaseURL": "https://saifr-3c037-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "saifr-3c037",
    "storageBucket": "saifr-3c037.appspot.com",
    "messagingSenderId": "464125842101",
    "appId": "1:464125842101:web:02f5fe14c4bab7502624fc",
    "measurementId": "G-NNPNBWT1H6" 
    }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

Motion_Data_old = 0    
Topic_Data_old = 0    
Mot_Data_old = 0  
Motion_Data = "Motion"
Topic_Data = "topic"
Mot_Data = "mot"
        
while 1: 
    Motion_Data = db.child("Motion").get().val()
    Topic_Data = db.child("Topic").get().val()
    Mot_Data = db.child("Mot").get().val()
    if (Motion_Data != Motion_Data_old):
        print ('Motion: ' + Motion_Data)
        Motion_Data_old = Motion_Data 
    if (Topic_Data != Topic_Data_old):
        print ('Topic: ' + Topic_Data)
        Topic_Data_old = Topic_Data
    if (Mot_Data != Mot_Data_old):
        print ('Mot: ' + Mot_Data)
        Mot_Data_old = Mot_Data
        
        
#    Y = Topic_Data.get()    
#   Z = Mot_Data.get()    
        
# if (Mot_Data is not Mot_Data_old):
#    print (Mot_data)
#if (Topic_Data is not Topic_Data_old):
#   print (topic_data)        
#user = db.child("Motion").get()
#print(user.val())
#Motion_Data.update(Motion_Data_old)
