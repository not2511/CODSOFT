names=[]
numbers=[]
while(True):
    print("Enter choice: ")
    print("1. Add contact")
    print("2. View contact")
    print("3. Exit")
    choice=int(input())
    if choice==1:
        name=input("Enter your name: ")
        number=input("Enter the number: ")
        names.append(name)
        numbers.append(number)
        continue
    elif choice==2:
        search_term = input("Enter search term: ")
        if search_term in names:
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            print("Name: {}, Phone Number: {}".format(search_term, phone_number))
        else:
            print("Not Found")
        continue
    elif choice==3:
        break
    else: 
        print("Wrong choice, try again.")
        continue