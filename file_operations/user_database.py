import csv

with open("database.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["email", "password"])

def registerUser(email, password):
    with open("database.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([email, password])
    
    print("\nUser registered successfully!!\n")
    

def loginUser(email, password):
    with open("database.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == email and row[1] == password:
                print("\nLogin successful!!\n")
                return
        print("\nInvalid credentials!! Register to continue!!\n")
        

def changePassword(email, password):
    with open("database.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
    
    with open("database.csv", mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for row in data:
            if row[0] == email:
                row[1] = password
            writer.writerow(row)
    
    print("\nPassword changed successfully!!\n")        

while True:
    print("##########################")
    print("Welcome to the user database")
    print("##########################")
    print("Choose an option:")
    operation = input("1. Register\n2. Login\n3. Update Password\n4. Exit\n>> ")
    
    if operation == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        registerUser(email, password)
    
    elif operation == "2":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        loginUser(email, password)
    
    elif operation == "3":
        email = input("Enter your email: ")
        password = input("Enter your new password: ")
        changePassword(email, password)
    
    else:
        print("Thanks for using the user database!! Visit again!!")
        break