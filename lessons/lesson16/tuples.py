# tuple items are unchangeable
courses = ("History", "Math", "Physics", "CompSci")
print(courses)

# creating tuple with different data types
juliette = ("Juliette", 30, 4.5, "France", True)
print(juliette)

# creating an empty tuple
empty = ()

# accessing an item in a tuple
print(courses[2])
print(f"The last item is: {courses[-1]}")

# find the number of items of a tuple
print(f"The number of items are: {len(juliette)}")

days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

# using slice to get multiple items from a tuple
print(days[:5])
print(days[5:])

# list inside of a tuple
student_info = ("Linda", 19, ["Photography", "Design", "Arts"])
student_info[2][2] = "CompSci"
print(student_info)

# looping through a tuple
for index, info in enumerate(juliette):
    print(index, info)
