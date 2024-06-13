a={2,4,6}
b={6,8,10}

# To find union of set
# print(a.union(b))


# To find intersection 
# print(a.intersection(b))
# a.intersection_update(b)
# print(a)


# To find symmetric difference
# print(a.symmetric_difference(b))


print(a.isdisjoint(b))
print(a.issubset(b))


# to remove any data
a.remove(2)
print(a)

# a.discard(4) #IT doesnt show error even if 4 isnt present in a set but remove does

# a.pop()  #remove one last element in list but remove random element in set


# To add any element in  a set
# a.add(5)



# To remove whole element in a set
a.clear()
print(a)


# To remove whole set itself
del a