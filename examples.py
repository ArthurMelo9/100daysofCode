#A rollercoaster ride
#print("Welcome to Rollercoaster!")
#height= int(input("Enter your height in cm: "))

#if height > 120:
 #   print("You can ride the rollercoaster!")
#else:
 #   print("Sorry, you have to grow taller before you can ride.")



print("Welcome to rollercoaster!")
height=int(input("What is your height in cm? "))
if height>=120:
  print("You're eligible to ride")
  age= int(input("What is your age? "))
  bill = 0
  #if age < 18:
    #print("Ticket costs $5")
  #else:
    #print ("Ticket costs $12")
  if age < 12:
    bill = 5
    print ("Ticket costs $5")
  elif age <=18:
    bill = 18
    print ("Ticket costs $7")
  elif age>=45 and age<=55:
      bill = 0
      print ("You have a free ride!")
  else:
    bill = 12
    print("Ticket costs $12")
  want_photo = input ("Do you want a picture? Y or N ")
  if want_photo == "Y":
      bill +=3
      print(f"Your total bill is ${bill}")
else:
  print("You're not eligible to ride")