#Welcome to tip calculator
print("Welcome to Tip Calculator!")

#what was the total bill 
total_bill = input ("What was the total bill? $")
total_bill = float(total_bill)

#what percentage tip will you give
tip= input("What percentage of tip will you give? 10, 12 or 15? ")
tip = int(tip)

#how many people to split the bill
num_people = input("How many people to split the bill? ")
num_people = int(num_people)

#each person should pay
final_bill= total_bill + (tip/100 * total_bill)
# rounding up the final price per head to 2dp
charge_per_person = round(final_bill/num_people, 2)

print (f"Each person is to pay ${charge_per_person}")


