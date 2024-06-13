# program for kaun banega crorepati

def kbc():
    count = 0
    question = ['What is the capital city of Nepal?','What is the capital city of Japan?']
    option = [' a. New delhi    b.Kathmandu    c.Tokyo    d.dhaka',' a. Capetown    b.Kathmandu    c.Tokyo    d.Sau paulo']
    answer = ['b','c']


    for i in range(0,2):
        print(question[i], option[i])
        print('Answer :',end='')
        n=input()
        if n==answer[i]:
            count +=  1
        else:
            break

    if(count==1):
        print('You become lakhpati')
    elif(count==2):
        print('You become millionaire')
    elif(count==0):
        print('You are Broke')
    else: 
        print('ERROR')

print('Welcome to Kaun Banega Crorepati')
print('Enter 1 to start the game:',end='')
start_kbc = int(input())

if start_kbc == 1 :
    kbc()
else:
    print('Get lost from here !!!')
