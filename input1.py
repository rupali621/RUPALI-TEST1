# enter inputs
month=int(input("Enter the month in the numeric form"))
day=int(input("Enter the day in numeric form"))
year=int(input("Enter the year as two numerical digits "))

if (month<1 and month>12):
 print("Error: Invalid Month Input")
elif(day<1 and day>31):
  print("Error: Invalid Day Input")
elif(year<0 and year>99):
   print("Error: Invalid year Input")
  

else:
  print(month,"/", day,"/", year)
  print("Success: Congratulations! you entered the correct date.")