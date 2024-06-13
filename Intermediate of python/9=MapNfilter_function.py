l= [1,4,5,7,3,2]

# Map function execute the function in all list element

def square(a) :
    return a*a

result = list(map(square, l))

# OR
# result = list(map(lambda a : a*a , l))

print(result)

# Filter function only shows the value in list if return condition is true else doesnt show
def funct (a):
    return a>4

result1= list(filter(funct, l))
print(result1)
