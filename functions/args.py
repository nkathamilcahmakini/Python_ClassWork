def my_country(country = "Rwanda"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(f"Hello  {name}")    

def sum (*numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer

#Create a function that can accept any number of integers 
# and return the result of multiply all of them
def multiply_integers(*nums):
    result = 1 
    for num in nums:
        result *= num  
    return result

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")   

#Question 1  
# A function named concatenate_args that takes any number 
# of string arguments in positional arguments format and 
# concatenates them into a single string 

def concatenate_args(*args):
    result = " "
    for arg in args:
        result += arg
    return result           
#Question2
#A function named concatenate_kwargs that takes any number 
# of string arguments in keyword arguments  format and 
# concatenates them into a single string

def concatenate_kwargs(**kwargs):
    name = " "
    for key, value in kwargs.items():
        name += value
    return name