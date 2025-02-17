# Write code below 💖

height = int(input("Enter your height in cm: "))
credits = int(input("How many credits do you have: "))

if height > 137 and credits > 10:
  print("Enjoy the ride")
elif height < 137 and credits > 10:
    print("You are not Tall enough to ride")
elif height > 137 and credits < 10:
      print("You dont have enough credits")
else:
        print("You have not met either requirement")