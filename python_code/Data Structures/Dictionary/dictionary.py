'''
 Dictionary Data Type
 Dictionary - Mutable Data Type and is represented by {}
 Dictionary Value can be added, removed and changed.
 Dictionary is a collection of key-value pairs.
 key-value pairs are separated by a colon(:)
 key-value pairs are separated by a comma(,)
 key-value pairs are enclosed in curly braces({})
 key should be unique and immutable data type. - int, float, string, tuple
 value can be any data type.
 key-value pairs are not ordered.
'''

classes = {
    'name' : 'Python Programming',
    'duration' : '2 Months',
    'type' : 'Online',
    'students' : 100,
    'rating' : 4.5,
    'is_active' : True,
    'level' : ['Beginner','Intermediate','Advanced'],
    5 : 'Five',
    5.5 : 'Five Point Five',
    (5,5) : 'Tuple Key'
}

print(classes)
print(classes['name'])
print(classes['duration'])
print(classes['type'])
print(classes['students'])
print(classes['rating'])
print(classes['is_active'])
print(classes['level'])
print(classes['level'][0])
print(classes[5])
print(classes[5.5])
print(classes[(5,5)])

# Invalid Key - KeyError: 'isActive'
# print(classes['isactive'])

print("\n")
print(classes.get('name'))
print(classes.get('duration'))
print(classes.get('type'))
print(classes.get('students'))
print(classes.get('rating'))
print(classes.get('is_active'))
print(classes.get('level'))
print(classes.get('level')[0])
print(classes.get(5))
print(classes.get(5.5))
print(classes.get((5,5)))


# Invalid Key - Returns None
print(classes.get('isActive'))
print(classes.get('isActive','Key Not Found'))

# Type of the Values in the Dictionary
print("Type of 'name' : 'Python Programming' ",type(classes.get('name')))
print("Type of 'duration' : '2 Months'",type(classes['duration']))
print("Type of 'type' : 'Online' ",type(classes['type']))
print("Type of 'students' : 100 ",type(classes['students']))
print("Type of 'rating' : 4.5",type(classes['rating']))
print("Type of 'is_active' : True",type(classes['is_active']))
print("Type of 'level' : ['Beginner','Intermediate','Advanced']",type(classes['level']))
print("Type of Level(0)",type(classes['level'][0]))
print("Type of 5 : 'Five'",type(classes[5]))
print("Type of 5.5 : 'Five Point Five'",type(classes[5.5]))
print("Type of (5,5) : 'Tuple Key'",type(classes[(5,5)]))

# Updating the Value for the Key.
classes['students'] = 200
print(classes['students'])

# Updating the Dictionary - using Update Method
classes.update({'students':300,'is_active':False,'platform':'Youtube'})
print(classes)

# Remove an Item from the Dictionary - using Pop Method
classes.pop('students')
print(classes)