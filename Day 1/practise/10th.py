#python to print all prime number

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False
    return True

def print_prime_numbers(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

print_prime_numbers(start, end)
