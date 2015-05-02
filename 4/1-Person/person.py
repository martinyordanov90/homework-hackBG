from datetime import date
first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")
birth_year = input("Enter birth year: ")
birth_year = int(birth_year)
current_age = date.today().year - birth_year
person = {
          "first name" : first_name,
          "second name" : second_name,
          "third name" : third_name,
          "birth year" : birth_year,
          "current age" : current_age
         }
print(person)
