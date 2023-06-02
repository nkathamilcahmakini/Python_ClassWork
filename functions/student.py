def year_of_birth(name, age):
    year = 2023 - age
    print(f"Hello {name} you were born in {year}")
 
    
#Write a function that takes an array of integers and 
#returns a new array containing only the prime numbers.

def isPrime(n): 
    if n <= 1: 
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False 
    return True

def getPrimes(nums):
    return [num for num in nums if isPrime(num)]



nums = [10, 21, 3, 8, 9, 11, 44, 62, 100, 19]
primeNums = getPrimes(nums)
primeNums.sort(reverse=True)
print(primeNums)