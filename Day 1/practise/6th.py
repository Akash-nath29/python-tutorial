#check the number is positive or negetive

num = float(input("Enter a number: "))
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

result = check_number(num)
print(result)
