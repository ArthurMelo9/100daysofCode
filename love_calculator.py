# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_1= name1.lower()
lower_case_2= name2.lower()


final_name = lower_case_1 + lower_case_2
true = final_name.count ("t") + final_name.count("r") + final_name.count("u") + final_name.count("e")
true_str= str(true)
love = final_name.count("l") + final_name.count("o") + final_name.count("v") + final_name.count("e")
love_str = str(love)

final_string =int(true_str + love_str)

if final_string <10 or final_string >90:
  print(f"Your score is {final_string},you go together like coke and mentos")

elif final_string >40 and final_string<50:
  print(f"Your score is {final_string}, you're alright together.")
else:
  print(f"Your score is {final_string}")
