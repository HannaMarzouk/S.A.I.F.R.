import speech_recognition as sr
#import pyaudio
my_Recognizer = sr.Recognizer()
print("")
print("         -------------------------------------------------------------------------------------")
print("         -------------------------------------------------------------------------------------")
print("         vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
print("         you are working with Speech Recognition of version :" + sr.__version__ + " with a Reognizer =>Sphinx ")
print("         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("         -------------------------------------------------------------------------------------")
print("         -------------------------------------------------------------------------------------")
print("")

order = sr.AudioFile('jackhammer.wav')
with order as source:
    my_Recognizer.adjust_for_ambient_noise(source,duration=1.2)
    audio = my_Recognizer.record(source)
    print(my_Recognizer.recognize_google(audio))
#print(my_Recognizer.recognize_google(audio))
#print(sr.Microphone.list_microphone_names())    
#mic = sr.Microphone(device_index=3)
#with mic as in_mic:
#    audio = my_Recognizer.listen(in_mic)
#    print(my_Recognizer.recognize_google(audio))
        
    

#print(type(audio))
#print(my_Recognizer.recognize_google(audio,show_all=True))    ->show all trascripts for audio in noise
