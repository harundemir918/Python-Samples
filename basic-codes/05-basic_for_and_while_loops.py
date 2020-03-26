# Author: harundemir918
# Basic for and while loops

print("What do you want to print?")

# The string that will be printed 
string = input("Enter the string: ")

print("How many times you want to print", string, "?")

# The number of strings
number = int(input("Enter the number: "))

print("You printed", string, number, "times using while loop.")

i = 0 # Start number of loop
while i < number:   # How many times the loop runs
                    # If start number is bigger than the number that user entered, exit the loop 
    print(string)   # Print the string
    i += 1          # Add 1 to the start number


print("And now, you printed", string, number, "times using for loop.")
for i in range(number): # For loop using range method
                        # Range is used to set the end number of loop
    print(string)
