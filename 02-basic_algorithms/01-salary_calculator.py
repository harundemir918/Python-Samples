# Author: harundemir918
# Basic salary calculator

# Get the ID number
idNumber = input("Enter the ID number of the employee: ")

# Get the work time
workTime = int(input("Enter the working time: "))

# Get the hourly wage
hourlyWage = int(input("Enter the hourly wage: "))

# Calculate the salary based on work time and hourly wage
salary = workTime * hourlyWage

# Multiply the salary with 0.14 and assign it to bonus
bonus = salary * 0.14

# Multiply the salary with 0.15 and assign it to tax
tax = salary * 0.15

# Calculate the net salary based on salary, tax and bonus
netSalary = salary - (tax + bonus)

# Print all information to the screen
print ("The employee whose ID number is", idNumber, ", has a salary of", salary, "$, a bonus of", bonus, "$, a tax of", tax, "$, and a net salary of", netSalary, "$.")
