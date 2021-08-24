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

Motion_Data_old = 0    
Topic_Data_old = 0    
Mot_Data_old = 0  
    
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
