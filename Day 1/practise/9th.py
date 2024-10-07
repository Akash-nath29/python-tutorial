#python to find HCF and LCM of two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    hcf = find_hcf(x, y)
    lcm = (x * y) // hcf
    return lcm

hcf = find_hcf(num1, num2)
lcm = find_lcm(num1, num2)

print(f"The HCF of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")
