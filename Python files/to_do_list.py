to_do= []
while True:
    print("\n To-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Task")
    print("4. Exit")
    choice= input("Enter your choice: ")
    if choice=='1':
        task=input("Enter the task to add: ")
        to_do.append(task)
        print(f"Task'{task}' added to the list")
    elif choice=='2':
        task=input("Enter the task to be removed: ")
        if task in to_do:
            to_do.remove(task)
            print(f"Task '{task}' removed from the list")
        else:
            print(f"Task '{task}' not found in the list")
    elif choice=='3':
        print("Tasks: ")
        for task in to_do:
            print(task)
    elif choice=='4':
        print("Exiting To-Do list.")
        break
    else:
        print("Invalid choice.")

