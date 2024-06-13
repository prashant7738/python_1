x= int(input('Enter a number :'))

match x :
    case 0:
        print('The number is zero')
    case 4 :
        print('The number is four ')
    case _ if x>=100:
        print('The number is greater than hundred: ')
    case _ :
        print('The number is ', x)