def person(age):
    if age < 0 or age >= 150:
        term = "Invalid age"
    elif age < 9:
        term = "Child"
    elif age < 18:
        term = "Adolescent"
    elif age < 65:
        term = "Adult"
    else:
        term = "Golden age"

    return term
