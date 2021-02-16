#Create File------------------------------------------
#Fail Safe
que=input('New?')
x=que.lower().startswith('ye') or que.lower().startswith('ne')

print('\n\nNew is:',x,'\n\n')
if x:
 try:
  fh=open('hotel_sheet.txt')
 except Exception as e:
  print(e)
  quit()


#Create SQLite File
import sqlite3 as s
conet = s.connect('HOTEL_DATABASE.sqlite')
cur = conet.cursor()

lst,it,note=[],0,1
if not x:
 co,con=0,0
 while True:
   co+=1
   rq='SELECT Hotel_DATABASE.slot FROM Hotel_DATABASE WHERE room_id='+str(co)
   instruction = cur.execute(rq)
   for row in instruction:
    row=row[0]
    if co%100==0:print('Loading...')
    lst.append(row)
   if len(lst)==con:break
   con=len(lst)

#----------------------------------------------------


if x:
 for i in fh:
  it+=1
  lst.append(i.split('\n')[0].strip())


if x: cur.execute('DROP TABLE IF EXISTS Hotel_DATABASE')


#CONFIRM VALUES
#print(lst)


#Should Create an iteration code to automate it for more/less numbers of columns
if x:cur.execute('CREATE TABLE Hotel_DATABASE (room_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, slot TEXT, Building INTEGER, Floor INTEGER, Room INTEGER)')
 


o,y=1,1
if x:
 for s in lst:
 #cur.execute("UPDATE Party_Animals SET "+cv[0]+"="+cv[1]+" WHERE id="+str(y))
  try:
   cur.execute("INSERT INTO Hotel_DATABASE (slot) VALUES (?)",(s,))
   y+=1
  except: print(s,"was rejected")
  if o%note==0:y+=1
  o+=1
 
 
 
 
 
 
#counting
count=0
countt=0
floor=1
building=1

for i in range(1,len(lst)+1):
   count+=1
   
   #Building, Floor, and Room UPDATING
   cur.execute("UPDATE Hotel_DATABASE SET Building="+str(building)+" WHERE room_id="+str(i))
   cur.execute("UPDATE Hotel_DATABASE SET Floor="+str(floor)+" WHERE room_id="+str(i))
   cur.execute("UPDATE Hotel_DATABASE SET Room="+str(count)+" WHERE room_id="+str(i))
   conet.commit()
   
   
   
   #Logistics
   if count==20:
    if floor%10==0: floor=0
    countt+=count
    if countt%200==0: building+=1
    count=0
    floor+=1


print('We have',countt,'Rooms in our Hotel')
 
 
 
 
 
#--TRY LATER----------------------------------------

#for i in range(1,it+1):cur.execute("UPDATE HOTEL_DATABASEt SET Alias="+str(i)+" WHERE id="+str(i))
#cur.execute("ALTER TABLE HOTEL_DATABASE DROP Alias")

#-----------------------------------------------------

conet.commit()
cur.close()
if x: fh.close()
from needed import Add_Special_Table_for_OPEN
print('Done...')
