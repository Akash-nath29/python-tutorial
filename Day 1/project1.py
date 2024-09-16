# Python Input

# Python input() function is used to take input from the user. The input() function reads a line entered on a console by an input device such as a keyboard and convert it into a string and returns it.

# a = input("Enter a number: ")
# print(type(a))
# print("User Choice", a)

# int() any datatype (float and integer) --> integer
# float() integer and float --> float
# str() any datatype --> string

# b = int(input("Enter second number: "))
# b = input("Enter second number: ")
# print(type(b))

# Calculator

first_number = int(input("Enter First Number:   "))
second_number = int(input("Enter Second Number:   "))
operation = input("Enter Operation [+, -, *, /]:   ")

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
    
elif operation == "*":
    print(first_number * second_number)
    
elif operation == "/":
    print(first_number / second_number)
    
else:
    print("Enter Valid Opertion!")