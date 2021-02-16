# Hotel Structure
# 3 buildings (A,B,C)
# 10 floors each (I-X)
# 20 rooms each (1-20)

#Open for occupied
#Close for non-occupied

#Back end

#Get Sheet
try:
 que=input('\nHandle requests?')
 if que.lower().startswith('ye'):
  inq='hotel_space_request.txt'
  fh = open(inq)
 else:
  inq= 'hotel_sheet.txt'
  fh=open('hotel_sheet.txt')
except: fh = open('hotel_sheet.txt')




r,f,b,c=-1,0,0,0
lst=[r for r in fh.read().strip().split('\n')]
print('\n\nRoom Status:\n',lst,'\n',sep='\n')
for v in lst:
 try:
  r+=20
  if r==len(lst)-1:break
  lst[r]=lst[r]+'.'
 except: break

r=0
for v in lst:
 try:
  if r==len(lst)-1: break
  if v.find('.')>0:
   f+=1
   if f%10==0:lst[r]=lst[r]+'*'
  r+=1
 except: break
 
lst3,lst4,lst5=[],[],[]
lst2=' '.join(lst).split('*')
#print(lst2)
for i in lst2:
  c+=1
  if c==1:l1=[[i.strip() for i in v.split()]for v in i.strip().split('.')]
  if c==2:l2=[[i.strip() for i in v.split()]for v in i.strip().split('.')]
  if c==3:l3=[[i.strip() for i in v.split()]for v in i.strip().split('.')]

sheet=[l1,l2,l3]
fh.close()







print('Welcome to our Hotel User Interface\n\n')

#counting
count=0
countt=0
floor=1
building=1
for a in sheet:
 for b in a:
  for c in b:
   count+=1
   
   #Status Report
   if not c.lower().startswith('cl'):
    if c.lower().startswith('op'):print('Building',building,'Floor',floor,'Room',count,'is FREE')
    if not c.lower().startswith('op'):print('Building',building,'Floor',floor,'Room',count,'is BOOKED')
    
   
   #Logistics
   if count==20:
    if floor%10==0: floor=0
    countt+=count
    if countt%200==0: building+=1
    count=0
    floor+=1

print('\n\nWe have',countt,'Rooms in our Hotel\n')



#Edit Room Availbility
sr=input('Share result?')
count=0
while True:
  try:
   u,f,r,i,inp=input('Building:'),input('Floor:'),input('Room:'),input('Change Room Status:'),input('Done?\n')
   fh=open('hotel_sheet.txt','w')
   sheet[int(u)-1][int(f)-1][int(r)-1]=i
   [[[fh.write(rs.capitalize()+'\n') for rs in f]for f in b] for b in sheet]
   fh.close()
   if inp.lower().startswith('do') or inp.lower().startswith('ye'):break
  except: break
try:
 if sr.lower().startswith('ye'):
  count=0
  countt=0
  floor=1
  building=1
  for a in sheet:
   for b in a:
    for c in b:
     count+=1
     
     #Status Report
     if not c.lower().startswith('cl'):
      if c.lower().startswith('op'):print('Building',building,'Floor',floor,'Room',count,'is FREE')
      if not c.lower().startswith('op'):print('Building',building,'Floor',floor,'Room',count,'is BOOKED')
     
     #Logistics
     if count==20:
      if floor%10==0: floor=0
      countt+=count
      if countt%200==0: building+=1
      count=0
      floor+=1
 print('\n\nWe have',countt,'Rooms in our Hotel')
except: pass



