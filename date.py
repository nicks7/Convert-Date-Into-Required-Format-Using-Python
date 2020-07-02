from datetime import datetime
c='20-07-02' 
strDate = c
objDate = datetime.strptime(strDate, '%y-%m-%d')
x=datetime.strftime(objDate,'%b %d, %Y')
print(x)