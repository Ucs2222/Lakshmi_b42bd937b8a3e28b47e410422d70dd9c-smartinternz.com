def isLeapYear(year):
  if (year % 4 == 0):
    return True
  else:
    return False


year = int(input("ENTER THE YEAR :"))
if isLeapYear(year):
  print(year, "is a leap year")
else:
  print(year, "not a leap year")
