from functools import reduce

numbers = [1, 2, 3, 4]

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24
