#take input a day and convert it to year month and days

def convert(total_days):
    years = total_days // 365
    r_days = total_days % 365
    months = r_days // 30
    days = r_days % 30

    return years, months, days

total_days = int(input("Enter the number of days: "))
years, months, days = convert(total_days)

print(f"{total_days} days is equivalent to {years} year(s), {months} month(s) and {days}days")