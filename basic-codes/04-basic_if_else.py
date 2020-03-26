# Author: harundemir918
# Basic if else

print("How old are you?")
age = int(input("Enter your age: "))

if (age < 18):
    print("You are under 18.")
elif (age >= 18 and age < 40):
    print("You are between 18 and 40.")
else:
    print("You are over 40.")
