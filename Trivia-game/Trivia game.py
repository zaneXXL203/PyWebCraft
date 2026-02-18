import random

questions = {
    "What keyword is used to define a function in Python?": "def",
    "What data type is returned by the expression 3 / 2 in Python 3?": "float",
    "Which symbol is used to write a comment in Python?": "#",
    "What built-in function is used to get the length of a list?": "len()",
    "What keyword is used to handle exceptions in Python?": "try",
    "What is the output of print(type([]))?": "<class 'list'>",
    "Which Python data type is immutable: list or tuple?": "tuple",
    "What keyword is used to import a module in Python?": "import"
}

def trivia_game():
    question_list = list(questions.keys())
    total_question = 5
    score = 0

    selected_questions = random.sample(question_list, total_question)

    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer:
            score +=1
            print("CORRECT! \n")
        else:
            print(f"""WRONG!
CORRECT-ANSWER -> {correct_answer} \n""")

    print(f"GAME OVER! SCORE:{score}/{total_question}")


trivia_game()