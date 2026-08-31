# and operator
# true and true = true
# true and false = false
# false and true = false
# false and false = false

print(True and False)

# or operator
# true or true = true
# true or false = true
# false or true = true
# false or false = false
print(False or False)

# not operator
# not false = true
# not true = false
print(not False)
print(not True)

login = False
if not login:
    print("Please login")
else:
    print("Welcome")


# False Values
# False
# None
# Zero of any numeric type
# Any empty sequence. for example '', (), []
# Any empty mapping for, {}

condition = None
if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")
