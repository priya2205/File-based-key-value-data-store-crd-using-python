#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import dataStoreOperation as crd 
import threading
from threading import*
import time
#importing the main file "dataStore" is the name of the file I have used as a library 

ds = crd.DataStore('fourth')
ds.create('priya',20)
#to create a key with key_name,value given and with no time-to-live property
ds.create("!priya_v",40)
ds.create("eriujahhekjfhjhfsjhfdbfjdfkjdfbdjfhkdjeawegadjkadgadjad",802894)
ds.create("soba",32)

ds.create("madhu",30,3) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)
ds.create("priya",20)
#it returns an ERROR since the key_name already exists in the database
ds.read("priya")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

time.sleep(3)
ds.read("madhu")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


ds.create("priya",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it

ds.create("elliot",28)
#ds.modifyKey("elliot",24)
ds.create("vandu",30,200)
 
ds.extendTimeToLive("vandu",90)
#it replaces the initial valueof timetolive of the respective key with new value of timetolive
ds.read("vandu")
ds.delete("elliot")
#it deletes the respective key and its value from the database(memory is also freed)
ds.modifyValue("vandu",40)
#it replaces the initial value of the respective key with new value

#we can access these using multiple threads like
t1=Thread(target=(ds.create),args=('abc',200,10)) 
t1.start()
t2=Thread(target=(ds.create),args=('priyavandu',40,10))
t2.start()
t3=Thread(target=(ds.read),args=('priyavandu',)) 
t3.start()

#ds = crd.DataStore('third')
dx = crd.DataStore('fourth')
#this gives an error because there exists a file with this name already so not more than 1 person can acces a file at any time


'''
the code also returns other errors like 
"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
"key doesnot exist" if key_name was mis-spelt or deleted earlier
"File memory limit reached" if file memory exceeds 1GB
Key exists already
'''
