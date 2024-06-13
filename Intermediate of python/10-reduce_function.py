# Reduce function applies function task to two elment of list and do same with next element and so on

from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y : x+y, numbers)
print (sum)