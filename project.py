birth_day = int(input("enter birth date:"))
birth_month = int(input("enter your birth month:"))
birth_year = int(input("enter your birth year:"))
current_date = int(input("enter current date:"))
current_month = int(input("enter current month:"))
current_year = int(input("enter current year:"))
date_diff = current_date - birth_day
month_diff = current_month - birth_month
year_diff = current_year - birth_year
if date_diff < 0:
    date_diff += 30
    month_diff -= 1
if month_diff < 0:
    month_diff += 12
    year_diff -= 1
print("your age is ", year_diff,"years",month_diff,"months",date_diff,"days")