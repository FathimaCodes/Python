cars=["bmw", "audi", "honda", "mercedes", "minicooper", "ferrari"]
print(cars)
cars.append("lexus")
print("After appending: ", cars)
cars.remove("ferrari")
print("After removing: ", cars)
cars[1]="Ford"
print("Modify: ", cars)
print(cars[1:5])
print(len(cars))
print(cars[2])
if "minicooper" in cars:
    print("Mini Cooper is in the list")
