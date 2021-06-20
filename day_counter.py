def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """This function is supposed to return the number of days in the month in a particular year, be it a leap year or a normal year """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  num_days=month_days[month-1] 
  for days in month_days:
    if is_leap(year) is True:
     month_days=[31,29,31,30,31,30,31,31,30,31,30,31]
     num_days=month_days[month-1]
  return num_days
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)













