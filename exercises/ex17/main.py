from datetime import datetime

now = datetime.now()

TARGET_AGE = 100


def year_turning_target(current_age: int, target_age: int = TARGET_AGE) -> int:
    """Return the calendar year in which someone of current age reaches target age."""
    current_year = datetime.now().year
    return current_year + (target_age - current_age)


def age_hundred():
    name = input("What is your name?: ").strip()

    while True:
        try:
            current_age = int(input("What is your age?: "))
            if current_age < 0:
                print("Age can't be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    year = year_turning_target(current_age)

    if current_age >= TARGET_AGE:
        return f"Hi, {name.title()}, you already turned {TARGET_AGE} in {year}!"

    return f"Hi, {name.title()} you will turn {TARGET_AGE} in the year {year}"


print(age_hundred())
