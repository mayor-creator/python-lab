import requests


# request open trivia api
def quiz_data():
    try:
        parameters = {
            "amount": 10,
            "category": 21,
            "difficulty": "medium",
            "type": "boolean",
        }
        endpoint = "https://opentdb.com/api.php?"
        response = requests.get(url=endpoint, params=parameters)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error occurred {error}")
    else:
        return data["results"]


# call the quiz_data() for the quiz question data
quiz_questions_data = quiz_data()


# get the quiz questions and add it to empty list
def get_quiz_questions():
    questions = []
    for question in quiz_questions_data:
        questions.append(question["question"])
    return questions


# get the quiz answers and add it to empty list
def get_quiz_answers():
    answers = []
    for answer in quiz_questions_data:
        answers.append(answer["correct_answer"])
    return answers


# ask the end user for response and compare it.
# return the number answered correctly
def start_quiz():
    quizzes = get_quiz_questions()
    for position, quiz in enumerate(quizzes, start=1):
        ask = input(f"{position}. {quiz}? (True / False)\n").capitalize()

    answers = get_quiz_answers()
    count = 0
    for ans in answers:
        if ask == ans:
            count += 1

    print(f"You got {count} correct on the quiz")


start_quiz()
