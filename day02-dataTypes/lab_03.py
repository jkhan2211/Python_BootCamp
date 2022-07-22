# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
#Write your code below this line 👇

age_as_int = int(age)
days = 365
weeks = 52
months = 12
assumed_years = 90
age_in_days = age_as_int * days
age_in_weeks = age_as_int * weeks
age_in_months = age_as_int * months
total_years = assumed_years * days
total_weeks = assumed_years * weeks
total_months = assumed_years * months
days_left = total_years - age_in_days 
weeks_left = total_weeks - age_in_weeks
months_left = total_months - age_in_months

print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left")

