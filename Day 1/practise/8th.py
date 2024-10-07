# Function to find all factors of a number

num = int(input("Enter a number: "))
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

factors = find_factors(num)
print(f"The factors of {num} are: {factors}")
