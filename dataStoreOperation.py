import json
from threading import Lock
import time
import os
# import math 
lst = []
class DataStore:
    
    def __init__(self,filename):
        self.c=0
        self.filename = filename
        
        
        # isFile = os.path.isfile(filename)
        
        if filename not in lst:
           self.fn =str(filename)+".json" 
           self.fptr = open(self.fn,"w+")
           lst.append(filename)
        else:
           print("Oops!,The file already exists and you cannot acceess it,To remove this error Please Create a new file")
        # dct={}
        # with open(self.fn,"w") as json_file:
        #     json_file.writelines('\n'.join(dct))
        self.lock = Lock()
    #create(key,value,timetolive_in_sec) - syntax 
    def create(self,key,value,timetolive=0):
        self.c+=1
        dataDict = {}
        fp = open(self.fn,'r')
        self.lock.acquire()
        if self.c>1:
            with open(self.fn,"r") as json_file:
                dataDict = json.load(json_file)
        if key in dataDict:
            print("Oops!it seems to be the Key exists already, enter a new key")# error msg
        else:
                if(key.isalnum()):
                      if (len(dataDict)+fp.tell())<(1024*1024*1024) and value<=(16*1024*1024):
                          if timetolive==0:
                                  l = {'value':value,'timetolive':timetolive}
                          else:
                                  l ={'value':value,'timetolive':time.time()+timetolive}
                          if len(key)<=32:
                                dataDict[key]=l
                                
                                json_data = json.dumps(dataDict,indent=4)
                                if self.c==1:
                                    with open(self.fn,"w") as outfile:
                                        #print(json_data)
                                        outfile.write(json_data)
                                    outfile.close()
                                if self.c>1:
                                    with open(self.fn,"r") as json_file:
                                         d = json.load(json_file)
                                         d[key]=l
                                    with open(self.fn,"w") as json_file:
                                         json.dump(d,json_file)
                                    json_file.close()
                                # with open(self.fn,"w") as outfile:
                                   
                                #     outfile.writelines('\n'.join(d))
                                
                          else:
                                print("OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars")
                                #return "OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars"
                      elif value>(16*1024*1024):
                             print("OOPs! The value exceeds more than 16kb, the key must be capped at  16kb")
                             #return "OOPs! The value exceeds more than 16kb, the key must be capped at  16kb"
                      else:
                             print("Sorry! Memory limit has been exceeded")
                             #return "Sorry! Memory limit has been exceeded" 
                else:
                       print("OOPs! Your Key Name is Invalid, Key name can contain numbers(0-9) and alphabets(a-z A-Z) but no special characters") 
                       #return "OOPs! Your Key Name is Invalid, Key name can contain numbers(0-9) and alphabets(a-z A-Z) but no special characters"


        self.lock.release()
        
    def read(self,key):
      resdata=''
      self.lock.acquire()
      with open(self.fn,"r") as json_file:
           data = json.load(json_file)
      json_file.close()
      if key not in data:
         print("Oops ! The key you entered is not available, Please ensure you entered a Valid Key")
         #return "Oops ! The key you entered is not available, Please ensure you entered a Valid Key"
      else:
         t = data[key]
         if t['timetolive']!=0:
            if time.time()<t['timetolive']:
               
                resdata = str(key)+':'+'['+str(t['value'])+','+str(t['timetolive'])+']'
                print("The data is for the key"+"'"+str(key) +"'"+resdata)
                #return data[key]
            else:
                print("Sorry,The Key you entered "+str(key)+" its Time to live has been expired "+str(round(time.time()-t['timetolive'],4))+"Seconds ago")
         else:
                
                resdata = str(key)+':'+"["+str(t['value'])+','+str(t['timetolive']) +"]"
                print("The data is for the key"+"'"+str(key) +"'"+resdata)
                #return data[key]
      self.lock.release()
              
    def delete(self,key):
         self.lock.acquire()
         with open(self.fn,"r") as json_file:
           data = json.load(json_file)
         json_line=[]
         if key not in data:
             print("Oops ! The key you entered is not available, Please ensure you entered a Valid Key")
             #return "Oops ! The key you entered is not available, Please ensure you entered a Valid Key"
         else:
             t = data[key]
             if t['timetolive']!=0:
                 if time.time()> t['timetolive']:
                     with open(self.fn,"r") as json_file:
                            d = json.load(json_file)
                     del d[key]
                     with open(self.fn,"w") as json_file:
                         json.dump(d,json_file)
                     print("Successful!, The key "+str(key)+" is deleted")
                     #return "Successful!, The key "+str(key)+" is deleted"
                 else:
                     print("Sorry,The Key you entered"+str(key)+" its Time to live has been expired "+str(round(time.time()-t['timetolive'],4))+"Seconds ago")
                     #return "Sorry,The Key you entered"+str(key)+" its Time to live has been expired "+str(round(time.time()-t['timetolive'],4))+"Seconds ago"
 
             else:
                 with open(self.fn,"r") as json_file:
                            d = json.load(json_file)
                 del d[key]
                 with open(self.fn,"w") as json_file:
                     json.dump(d,json_file)
                 json_file.close()
                 print("Successful!, The key "+str(key)+" is deleted")
                 #return "Successful!, The key "+str(key)+" is deleted"
         self.lock.release()
         
#modifyValue(key,newvalu e)
    def modifyValue(self,key,value):
      self.lock.acquire()
      with open(self.fn,"r") as json_file:
          data = json.load(json_file)
      if key not in data:
         print("Oops ! The key you entered is not available, Please ensure you entered a Valid Key")
         #return "Oops ! The key you entered is not available, Please ensure you entered a Valid Key"
      else:
             t = data[key]
             if(key.isalnum()):
                  if value<=(16*1024*1024):
                         l = {'value':value,'timetolive':t['timetolive']} # add the timeto live value and new value 
                         if len(key)<=32:
                            with open(self.fn,"r") as json_file:
                                 d = json.load(json_file)
                            d[key] = l
                            with open(self.fn,"w") as json_file:
                                  json.dump(d,json_file)
                         else:
                             print("OOPs! The key exceeds more than 32 char, the key must be capped at 32 chars")
                  else:
                      print( "OOPs! The value exceeds more than 16kb, the key must be capped at 16kb")
             else:
                 print("OOPs! Your Key Name is Invalid, Key name can contain numbers(0-9) and alphabets(a-z A-Z) but no special characters") 
      self.lock.release()
    #extendTimeToLive(key,how_many_seconds_to_be_extended)
    def extendTimeToLive(self,key,timetolive):
         self.lock.acquire()
         with open(self.fn) as json_file:
           data = json.load(json_file)
         if key not in data:
             print("Oops ! The key you entered is not available, Please ensure you entered a Valid Key")
             #return "Oops ! The key you entered is not available, Please ensure you entered a Valid Key"
         else:
             t = data[key]
             if t['timetolive']!=0:
                
                 if t['timetolive']>time.time():
                      l = {'value':t['value'],'timetolive':t['timetolive']+timetolive}
                      with open(self.fn,"r") as json_file:
                             d = json.load(json_file)
                      d[key] = l
                      with open(self.fn,"w") as json_file:
                           json.dump(d,json_file)
                      print("Successful!, The key "+str(key)+" time to live extended")
                 else:
                     print("Sorry,The Key you entered "+str(key)+" its Time to live has been expired "+str(time.time()-t['timetolive'])+"Seconds ago")
             else:
                  l = {'value':t['value'],'timetolive':timetolive}
                  with open(self.fn,"r") as json_file:
                            d = json.load(json_file)
                  d[key] = l
                  with open(self.fn,"w") as json_file:
                            json.dump(d,json_file)
                  print("Successful!, The key "+str(key)+" timr to live extended")
         self.lock.release()
