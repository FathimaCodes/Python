number=int(input("Enter a number:"))
if number>0:
    if number % 2 == 0:
        print(f"Number {number} is positive and even.")
    else:
        print(f"Number {number} is positive and odd.")
elif number<0:
    if number % 2 ==0:
        print(f"Number {number} is negative and even.")
    else:
        print(f"Number {number} is negative and odd.")
else:
    print(f"Number {number} is zero, which is neither positive nor negative, and even.")
if number > 1:
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            print(f"The number {number} is not a prime number.")
            break
        else:
            print(f"the number {number} is a prime number.")
elif number <-1:
    print(f"Negative numbers cannot be prime.")