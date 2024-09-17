a= True
b= False
and_result= a and b
print(f"Logical AND of {a} and {b} is {and_result}")
or_result= a or b
print(f"Logical OR of {a} and {b} is {or_result}")

not_a = not a
not_b = not b
print(f"Logical NOT of {a} is {not_a}")
print(f"Logical NOT of {b} is {not_b}")
combined_result= (a and not b) or(not a and b)
print(f"Combined logical operation result is {combined_result}")
