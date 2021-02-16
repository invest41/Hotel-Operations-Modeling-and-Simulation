import sqlite3 as s

conet = s.connect('HOTEL_DATABASE.sqlite')
cur = conet.cursor()
cur.execute('DROP TABLE IF EXISTS Open_Room')





cur.execute('CREATE TABLE Open_Room (room_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, slot TEXT,Building INTEGER, Floor INTEGER, Room INTEGER)')
rep = tuple(cur.execute('SELECT * FROM Hotel_DATABASE'))

for i in rep:
 a,b,c,d,e = i

 b=str(b)
 if b.lower().startswith('o'):
  cur.execute("INSERT INTO Open_Room (slot,Building,Floor,Room) VALUES (?,?,?,?)",(b,c,d,e))




conet.commit()
cur.close()
