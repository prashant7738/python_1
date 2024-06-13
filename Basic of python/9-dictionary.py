student= {'name':'kheman', 'address': 'nawalpur', 'age': 18}

print(student['name'])

# for assinging new categorie
student['college']= 'Thapathali'
print(student)


# for updating value
student['age']= 19
print('The age of ',student['name'], 'is'  , student['age'])


# for deleting any categorie 
del student['address']
print(student)