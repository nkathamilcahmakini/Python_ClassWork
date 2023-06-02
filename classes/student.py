# Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
#              class Student:

from datetime import datetime
class Student:
    school = "AkiraChix" 
    def __init__(self, first_name, second_name, age, country):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age 
        self.country = country
    def greet_student(self):
        return f"Hello {self.first_name} {self.second_name} from {self.country}. Welcome to {self.school}" 

    def show_full_name(self):
        return f"{self.first_name} { self.second_name}" 
    
    def year_of_birth(self):
        current_year = datetime.datetime.now().year
        return current_year - self.age

    def show_initials(self):
        return f"{self.first_name[0]}.{self.second_name[0]}" 