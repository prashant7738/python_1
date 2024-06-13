# for coding
sentence= input('Enter sentence :')
n = int(input('Enter 1 for coding and 2 for decoding'))
words= sentence.split(' ')
if n==1:
    for word in words:
        if (len(word)<3):
            nword = word[::-1]

        else:
            
            nword = 'faz' + word[1:] + word[0] +  'jdk'
        
        
        print('Your secret code is \t',nword)

    # for decoding
elif n==2:
    for word in words:
       
        if (len(word)<3):
            code = word[::-1]
        else:
            
            nword =word[-4]  + word[3:-4]

        print('The real decoded word is: \t',nword)

else:
    print('error')
