# age = int(input("Enter your age"))

# if(age>=18):
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")



num = int(input("Enter any number :"))
if(num>=1):
    if(num<=10):
        print('This number is between 1-10')
    elif(num<=20):
        print('This number is between 10-20')
    else:
        print('This number is greater than 20')
elif(num>=0):
    print('This number is zero ')
else:
    print('This number is negative ')