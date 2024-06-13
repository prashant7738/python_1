# to find factorial of any number n

n= int(input('Enter a number:'))

def fact(n):
    while(n>=0):
        if (n==0 or n==1):
            return 1
        else:
            return n* fact(n-1)
        
print('The factorial of given number is :',fact(n))


# fibonacci series

def fibo(n):
    a=0
    b=1
    print('The fibonicci series are :')
    
    for i in range(0,n):
        print(a, end=',')
        a=b
        b=a+b

fibo(n)
