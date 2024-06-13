n= int(input('Enter a number '))
if(n>=1):
    for i in range(1,21):
      print(n, '*',i, '=' , n*i)
      if(i==10):
          break