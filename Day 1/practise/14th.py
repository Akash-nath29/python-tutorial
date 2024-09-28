#find the max and min number in 10 numbers


num_list = []
for i in range(10):
    num = int(input("Enter the number:  "))
    num_list.append(num)

print(max(num_list))
print(min(num_list))