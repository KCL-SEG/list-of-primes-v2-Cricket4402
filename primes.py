"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    if(number_of_primes <= 0):
        raise ValueError("Invalid value")
    
    list = []
    factors = 0
    i = 2
    while len(list) < number_of_primes:
        
        if prime_finder(i):
            list.append(i)  
        i = i + 1          
            
    return list

def prime_finder(i):
   
    for j in range(2, i):
        if(i % j == 0):
            return False
    
    return True