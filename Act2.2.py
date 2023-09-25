name = input ("Enter Father's Name: ")
birthplace = input ("Enter Birthplace: ")
import datetime

birth_date = int(input("Enter birth date (DD): "))
birth_month = int(input("Enter birth month (MM): "))
birth_year = int(input("Enter birth year (YYYY): "))

today = datetime.date.today()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_date))

print("He is", age, "years old.")
