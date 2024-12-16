currentDate = input("Enter current date: ")

splitted = currentDate.split(", ")
days = int(splitted[0])
months = int(splitted[1])
years = int(splitted[2])
days_to_add = int(splitted[3])


months_limits = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

# =============================================
while days_to_add > 0:
    days += 1
    if days > months_limits[months]:
        days -= months_limits[months]
        months += 1
    if months > 12:
        months -= 12
        years += 1
    days_to_add -= 1
# =============================================
    
print(f"{days}, {months}, {years}")