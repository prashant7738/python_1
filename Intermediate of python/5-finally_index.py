def funct():
    try:
        n= int(input('Enter a index number '))
        l = [2,3,4,5,6]
        print (l[n])
        return 1
    
    except:
        print('error')
        return 0

    finally:
        print('This will always be executed !!')
        # print('This will always be executed !!')


x = funct()
print(x)
        
    

