fh=open('hotel_sheet.txt')

# 3 buildings (A,B,C) 
# 10 floors each (I-X) '*'
# 20 rooms each (1-20) '.'



r,f,b,c=-1,0,0,0
lst=[r for r in fh.read().strip().split('\n')]

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

for i in lst2:
  c+=1
  if c==1:l1=[[i for i in v.split()]for v in i.strip().split('.')]
  if c==2:l2=[[i for i in v.split()]for v in i.strip().split('.')]
  if c==3:l3=[[i for i in v.split()]for v in i.strip().split('.')]

sheet=[l1,l2,l3]
fh.close()
fh=open('hotel_space_request.txt','w')

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
   if count==20:
   	countt+=count
   	count=0
   	floor+=1
   	if floor%10==0: floor=0
   	if countt%200==0: building+=1
   if not c.lower().startswith('close'):
    if c.lower().startswith('open'):print('Building',building,'Floor',floor,'Room',count,'is free')
    if not c.lower().startswith('open'):print('Building',building,'Floor',floor,'Room',count,'is Booked')
print('\n\nWe have',countt,'Rooms in our Hotel')




while True:
 try:
  u,f,r=input('Input Details...\nBuilding:'),input('Floor:'),input('Room:')
  sheet[int(u)-1][int(f)-1][int(r)-1]='Booked'
  print('\n\nRoom Status:',sheet[int(u)-1][int(f)-1][int(r)-1],end='\n\n')
  d=input('Are you done?')
  if d.lower().startswith('do') or d.lower().startswith('ye'): break
 except: break


[[[fh.write(rs.capitalize()+'\n') for rs in f]for f in b] for b in sheet]
fh.close()

