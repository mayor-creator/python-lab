print("CALCULATION")

def add(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    return number_1 / number_2

play = True
answer = 0
while play:
    num_1 = float(input("what is the first number?: "))
    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")

    num_2 = float(input("What is the next number?: "))

    if operation == "+":
        answer = add(num_1, num_2)
    elif operation == "-":
        answer = subtraction(num_1, num_2)
    elif operation == "*":
        answer = multiplication(num_1, num_2)
    elif operation == "/":
        if num_2 == 0:
            print("Can't divide by 0")
        else:
            answer = division(num_1, num_2)
    else:
        print("Invalid Operation")

    print(f"{num_1} {operation} {num_2} = {float(answer)}")
    
    question = input(f"Type 'yes' to continue calculating with {answer} or type 'no' to start a new calculation: ").lower()

    if question == "no":
        play = False
    else:
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")

        num_2 = float(input("What is the next number?: "))

        if operation == "+":
            answer_2 = add(answer, num_2)
        elif operation == "-":
            answer_2 = subtraction(answer, num_2)
        elif operation == "*":
            answer_2 = multiplication(answer, num_2)
        elif operation == "/":
            if num_2 == 0:
                print("Can't divide by 0")
            else:
                answer_2 = division(answer, num_2)
        else:
            print("Invalid operation")
        
        print(f"{answer} {operation} {num_2} = {float(answer_2)}")