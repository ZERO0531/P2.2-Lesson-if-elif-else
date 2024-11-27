print("Check what you can do in your age! ")
age = int(input("your age: "))
if age < 16: 
  print("You can't drive. ")
elif age == 16 and 17: 
  print("You can drive but not vote. ")
elif age == 18 and 20: 
  print("You can vote but not rent a car.")
elif age > 20: 
  print("You can do pretty much anything.")
  
