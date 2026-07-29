# using the range() to make a list of numbers
numbers = list(range(1, 11))
print(numbers)

# statistics with numbers
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")

# list comprehensions
squares = [value**2 for value in range(1, 10)]
print(squares)

odd_numbers = [number for number in range(1, 50) if number % 2 != 0]
print(odd_numbers)
