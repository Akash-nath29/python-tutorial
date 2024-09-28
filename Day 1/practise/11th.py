#python to print all prime number


def print_prime_numbers(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

limit = int(input("Enter the limit of the range: "))
print_prime_numbers(limit)