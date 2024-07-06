print("Welcome to the to do list, here you can add your task, manage your task as well as update your task.")

tasks=[] #empty list to add task and update them

#Setting up the choice menu feature
while True:
    print("1. To add the tasks")
    print("2. Update the task you have already done")
    print("3. View all the task")
    print("4. Exit") 
    
    choice=int(input("Please Enter your choice: "))
    if choice==1:
        new_task=input("Please enter the task you want to add in the list: ")
        tasks.append(new_task)
        print('Task has been added.')
        continue
    
    elif choice==2:
        task_update=input("Enter the task you wanna update: ")
        if task_update in tasks:
            index=tasks.index(task_update)
            tasks.pop(index)
            print("Removal of task is successful.")
            continue
    
    elif choice==3:
        for i in tasks:
            print(i)
        print("These are the current tasks.")
        continue
    
    elif choice==4:
        break 
    #to exit out of the while True loop
    
    else:
        print('Please enter a valid choice.')
        continue
    