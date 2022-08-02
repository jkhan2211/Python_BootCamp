#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

greetings = print("Welcome to the Tip Calculator!")
var_ask = float(input("What was the total bill? "))
var_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
var_people = input("How many people are splitting the bill? ")

calculate_total_bill = var_ask * (1 + (float(var_tip) / 100))
people_division = calculate_total_bill / int(var_people)

print("Each person should pay: $" + str(round(people_division, 2)))