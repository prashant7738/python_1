# tuples cant be changed after creation unlike list

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print(thistuple[0])



# But to change tuples we need to do this:

tuple1 = ('nepal',"india",'china', 'pakistan')
print(tuple1)
temp = list(tuple1)
temp.append('bhutan')
temp.pop(2)
temp[2]='bangladesh'

tuple2=tuple(temp)
print(tuple2)
