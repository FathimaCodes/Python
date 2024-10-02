user_details={}
def add_user(name,email,age):
    user_details[name]={'Email':email,'Age':age}

def display_users():
    for name,details in user_details.items(): 
        print(f"Name:{name}, Email:{details['Email']}, Age:{details['Age']}")

add_user('Ani','ani@example.com',23)
add_user('John','john@example.com',24)
add_user('Jim', 'jim@example.com',27)

display_users()