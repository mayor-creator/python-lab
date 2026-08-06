numbers = [1, 2, 3, 4, 5]
print(numbers)

# syntax for list comprehension
# new_list = [expression for item in list if condition == True]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# conditionals in list comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

# list comprehension with string
city = "Barcelona."
vowels = "aeiou"

result = [char for char in city if char in vowels]
print(result)
