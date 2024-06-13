for i in range(6):
    print(i)
else:
    print('The loop is over ')


# But But
for i in range(6):
    if i==4:
        break
    print(i)
else:
    print('The loop is over ')

# In above condition loop is not fully completed so else is not executed
    
n=0
while n<=3:
    print(n)
    n = n+1
    # if (n==3):
    #     break

else:
    print('While loop is over !!')

