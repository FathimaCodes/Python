def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average= total/count
    return average
numbers_list= [2,4,6,8,10]
average= calculate_average(numbers_list)
print("The average is:",average)