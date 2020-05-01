#python code that outputs the age of a person 
import datetime
def agecalculator():

    day = int(input("Enter the date of birth:\n"))
    month= int(input("Enter the month of birth:\n"))
    year = int(input("Enter the year of birth:\n"))

    current_year = datetime.datetime.now().year
    age = current_year - year
    print("Date of birth id dd/mm/yyyy:" , day)
    print("You are" , age, "years old")




