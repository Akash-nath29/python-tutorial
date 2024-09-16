# # # if sourjya attends college, shan will do so
# # # else, shan will spend his day at home

# # a = 5

# # # a > 7 Shan is a good boy
# # # a < 7 shan is worst person ever

# # if a > 7:
# #     print("Shan is a good boy") # 1 tab is equivalent to 4 spaces
# # else:
# #     print("Shan is worst person ever")
    
# # # block statement --> if else elif, for, while, function, class, try, except, finally, with


# # age 
# # if user age is greater than 18, he/she can vote
# # else, he/she cannot vote
# # if user age is equal to 18, he/she should not vote

# # python - elif
# # c - else if
# # javascript - else if ....

# age = 15

# if age > 18 and age < 100: # 1 , 1  && --> 1
#     print("You can vote")
    
# elif age == 18:
#     print("You should not vote")
    
# else:
#     print("You cannot vote")


# Write a Python program that asks the user to input the temperature in Celsius, and then prints out a description of the weather:

# If the temperature is below 0, print 'Freezing cold.'
# If the temperature is between 0 and 15, print 'Cold weather.'
# If the temperature is between 16 and 25, print 'Pleasant weather.'
# If the temperature is between 26 and 35, print 'Warm weather.'
# If the temperature is above 35, print 'It's really hot!'

temp = 16

if temp < 0:
    print("Freezing cold.")
    
elif temp > 0 and temp < 15:
    print("Cold weather")
    
elif temp > 15 and temp < 25:
    print("Pleasant weather")
    
elif temp > 25 and temp < 35:
    print("Warm weather")
    
else:
    print("It's really hot!")