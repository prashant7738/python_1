def simpleInterest(p , t, r):
  '''This function give the value of simple interest'''
  si = (p*t*r)/100
  print("The simple interest is: " , si)


principle = float(input("Enter principle : "))
time = float(input("Enter time  "))
rate = float(input("Enter rate "))

simpleInterest(principle , time , rate)


# This is python doc attribute
print(simpleInterest.__doc__)