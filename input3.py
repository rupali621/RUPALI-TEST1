#def inputs
salary=float(input("Please enter your salary in Germany:"))
country=input("Enter the country you want to migrate to:")

def convertSalary(country,salary):
  if(country=="canada"):
    final_salary=salary*1.55
    if(final_salary>64000):
      print("You will be rich in Canada with a salary of", final_salary, "CAD")
    else:
      print("You will be poor in Canada with a salary of", final_salary, "CAD")
  elif (country  == "us"):
    final_salary=salary*2.5
    if(final-salary>35000):
      print("You will be rich in United Kingdom with a salary of ", final-salary, "pound")
    else:
      print("You will be poor in United Kingdom with a salary of ", final-salary, "pound")
  elif(country=="cambodia"):
    final_salary=salary*4555
    if(final_salary>5649856):
      print("you will be rich in cambodia with a salary of ", final_salary, "cambodia riel")
    else:
      print("you will be poor in cambodia with a salary of " ,final_salary, "cambodia riel")
    
  elif(country=="United Kingdom"):
     final_salary = salary*1.2
     if(final_salary > 56515):
       print("you will be rich in US with a salary of", final_salary," USD")
     else: 
        print("you will be poor in US with a salary of", final_salary, "USD")
  else:
      print("invalid country")
            
convertSalary(country,salary)
          
          
        
        
    
    
  
    
  
    