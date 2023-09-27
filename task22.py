# Task: To determine if the year inputed by the user is leap or not
# requesting user to input the year and the number of years they want to check
# Using the formula to determine if a year is leap or not


year = int(input("\nWhat year do you want to start with: "))
number_of_years = int(input("How many years do you want to check: "))


for number_of_years in range(1,number_of_years + 1):        # The +1 at the end index is to print the number of years inputed by user
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        print(f"{year} is a leap year")

    else:
        print(f"{year} is not a leap year")
        
    year += 1                                              
        
    