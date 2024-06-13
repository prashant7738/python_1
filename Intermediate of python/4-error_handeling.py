# Lets see how we can handel error in a code 
# Let me enter a character instead of integer ---- Error occur > so to solve this we use try and except case

try:
    a =input("enter a number :")
    b= input("enter another number :")

    sum = int(a) + int(b)

    print("the sum of two number " + str(sum))

except Exception as e:
    print(e)

 

#  OR 
# except:
#     print('Invalid input')