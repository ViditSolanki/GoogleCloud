month = ['January','February','March','April','May','June','July','August','September','October','November','December']
MM = []
mm = []
Month = []
date = raw_input('Enter date (dd-mm-yyyy): ')
if date[3:5]<10:
    mm.append(date[4:5])
    i = int(mm[0])
    MM.append(month[i])
    print MM
    print mm