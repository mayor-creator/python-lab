def less_than(nums: list[int], limit: int = 5) -> list[int]:
    """Return the numbers from nums that are strictly less than limit"""
    new_list = []
    for num in nums:
        if num < limit:
            new_list.append(num)
    return new_list


values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
small_numbers = less_than(values)
print(small_numbers)

values = [9, 7, 6, 8, 13, 21, 34, 55, 89]
big_numbers = less_than(values, limit=10)
print(big_numbers)


def evenly_divisor():
    """Return all the divisors of a number entered by the user"""
    evenly_number = []
    userInput = int(input("Please enter a number: "))
    numbers = range(1, userInput + 1)
    for i in numbers:
        if userInput % i == 0:
            evenly_number.append(i)
    return evenly_number


print(evenly_divisor())
