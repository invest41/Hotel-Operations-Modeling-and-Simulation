#Create Template
sheet=[[['Close' for r in range(20)]for f in range(10)] for b in range(3)]

# Back-end

#Create file (Automated Baseline Availability)
fh=open('hotel_sheet.txt','w')
[[[fh.write(r+'\n') for r in f]for f in b] for b in sheet]
fh.close()
