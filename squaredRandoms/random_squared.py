import random
# Make a list of 20 random numbers between 0 and 49
random_numbers = [random.randint(0, 49) for x in range(20)]
print(random_numbers)
# square list of numbers using list comprehension
random_squared = [x ** 2 for x in random_numbers]
print(random_squared)
