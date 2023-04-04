#define colors
RED = "red"
 
BLUE = "blue"

YELLOW = "yellow"

#enter inputs

color1= input("please enter your first primary color")
color2=input("please enter your second primary color")

if (color1!=RED):
  print("Error: Invalid Color1")
  
elif(color2!=BLUE):
  print("Error: Invalid Color2")
elif(color1==color2):
    print("Error: The two colors you entered are same")
else:
     
   if(color1==RED and color2==BLUE):
    print("PURPLE")
   elif(color1==RED and color2==YELLOW):
     print("ORANGE")
   elif(color1==BLUE and color2==RED):
     print("PURPLE")
   elif(color1==YELLOW and color2==RED):
     print("ORANGE")
   elif(color1==YELLOW and color2==BLUE):
    print("GREEN")