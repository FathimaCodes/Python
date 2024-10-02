my_dict={'name':'John','age':23, 'city': 'New York'}  #creating a dictionary
print(my_dict['name'])  #accessing values
print(my_dict['age'])

my_dict['age']=28  #modify values
my_dict['email']='john@example.com'  #adding key-values pairs
print(my_dict)

del my_dict['city']
email=my_dict.pop('email')
print(my_dict)

if 'name' in my_dict:
    print('Name exists in the dictionary')
else:
    print('Name does not exist in the dictionary')
