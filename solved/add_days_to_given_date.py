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


def are_inputs_valid(days ,months ,years ,days_to_add):
    returned = {
        "is_valid": True,
        "message": "",
    }
    if not(months >= 1 and months <= 12):
        returned["is_valid"] = False
        returned["message"] = "You should write a month number from 1 to 12"
        return returned
    elif months_limits[months] < days:
        returned["is_valid"] = False
        returned["message"] = f"This month days count are {months_limits[months]}, you wrote {days}"
        return returned
    elif years > 2026 or years < 1900:
        returned["is_valid"] = False
        returned["message"] = "you should select a year that is no earlier than 1900 and no later than 2026"
        return returned
    elif days_to_add > 1000:
        returned["is_valid"] = False
        returned["message"] = "Maximum days to add is 1000, try again."
        return returned
    
    return returned


def get_inputs():
    currentDate = input("Enter current date: ")

    splitted = currentDate.split(", ")
    days = int(splitted[0])
    months = int(splitted[1])
    years = int(splitted[2])
    days_to_add = int(splitted[3])

    return {
        "days": days,
        "months": months,
        "years": years,
        "days_to_add": days_to_add,
    }


days = 0
months = 0
years = 0
days_to_add = 0

is_valid = False
error_message = "" 
while not(is_valid):
    error_message and print(error_message)
    
    inputs = get_inputs()
    days = inputs["days"]
    months = inputs["months"]
    years = inputs["years"]
    days_to_add = inputs["days_to_add"]
    
    response = are_inputs_valid(days, months, years, days_to_add)
    is_valid = response["is_valid"]
    error_message = response["message"]

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