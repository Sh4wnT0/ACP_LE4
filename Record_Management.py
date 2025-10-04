import os

doc_path = os.path.expanduser("~/Documents")

while (True):
    print("\n==========================")
    print("1. Register")
    print("2. Open Student Record")
    print("3. Exit")
    print("==========================")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError as e:
        print("Please enter an integer between 1-3: ")
        continue
    
    if choice == 1:
        print("\nEnter Student Information:")
        while(True):
            try:
                student_no = int(input("Student No.: "))
                break
            except ValueError:
                print("Please enter an integer.")
            
        student_name = input("Full name: ")
        student_prog = input("Program: ")

        while(True):
            try:
                student_age = int(input("Age: "))
                break
            except ValueError:
                 print("Please enter an integer.")

        student_gender = input("Gender: ")
        bday = input("Birthday: ")

        while(True):
            try:
                contact = int(input("Contact No.: "))
                break
            except ValueError:
                print("Please enter an integer. ")
    
        data = [f"Name: {student_name}", 
                f"Program: {student_prog}", 
                f"Age: {student_age}",  
                f"Gender: {student_gender}", 
                f"Birthday: {bday}", 
                f"Contact No.: {contact}"]

        with open(f"{student_no}.txt", "w") as f:
            for item in data:
                f.write(item + '\n')
        
            print("Record added successfully")

    elif choice == 2:
            print("\nSearching for who? Enter:")
            student_no = int(input("Student No.: "))
            file = (f"{student_no}.txt")

            try:
                 with open(file, 'r') as f:
                    record = f.readlines()
                    print("\nStudent Record for ID:", student_no)
                    for line in record:
                        print(line.strip())

            except FileNotFoundError:
                    print(f"Error: The file '{file}' does not exist!")

    elif choice == 3:
        print("Thank you for using the system! ")
        break 

    else:
         print("Please only enter values between 1-3.")  
         continue                    
    
