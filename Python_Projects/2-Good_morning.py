import time

timezone = int(time.strftime('%H'))    # %S for second and %M for minutes         

name= input('Enter your name : ')

if(timezone>=20  and timezone<=5):   
    print('Good Night ' + name)
elif(timezone<=10):
    print('Good Morning ' + name)
elif(timezone<=17):
    print('Good Afternoon ' + name)
else:
    print('Good Evening ' + name )
