name = 'prashant kafle'
address = 'kawasoti'
age=17.835

letter = f'my name is {name} and I live in {address}. My age is also {age:.2f}'
print(letter)


# to literally show {name} like this instead of prashant we use double bracket 

letter_1 = f'my name is {{name}} and I live in {{address}}. My age is also {age:.2f}'
print(letter_1)