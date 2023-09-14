#CODSOFT TASK 5 QUIZ GAME

import random

def welcome_message():
    print("Codsoft Task 5 The QUIZ GAME")
    print("Welcome to our Quiz Game!")
    print("You will be ASKED a couple of questions. Answer as many as you can.")
    print(" Now Let's get started!\n")

quiz_questions = [
    {
        "question": "Which city is known as the orange city in maharashtra?",
        "options": ["A. Nagpur", "B. Pune", "C. Mumbai"],
        "correct_answer": "A"
    },
    {
        "question": "Python language was developed by'?",
        "options": ["A.Dennis M. Ritchie ", "B. Guido van Rossum", "C. James Gosling"],
        "correct_answer": "B"
    },
    
    {
        "question": "OS computer abbreviation usually means",
        "correct_answer": "Operating System"
    },

        {
        "question": "Which is a type of Electrically-Erasable Programmable Read-Only Memory?",
        "options": ["A.Flange", "B.FRAM ", "C. Flash"],
        "correct_answer": "C"
    },
]

def calculate_score(user_answers):
    score = 0
    for i, question in enumerate(quiz_questions):
        correct_answer = question.get("correct_answer")
        user_answer = user_answers[i]
        if isinstance(correct_answer, list):
            if user_answer.lower() in [ans.lower() for ans in correct_answer]:
                score += 1
        else:
           if user_answer.lower() == correct_answer.lower():
                score += 1
    return score

# Function to present quiz questions
def present_questions():
    user_answers = []
    for i, question in enumerate(quiz_questions):
        print(f"Question {i + 1}: {question['question']}")
        if "options" in question:
            for option in question["options"]:
                print(option)
            user_answer = input("Your answer (A, B, C, etc.): ").upper()
        else:
            user_answer = input("Your answer: ").strip()
        user_answers.append(user_answer)
        print()
    return user_answers

# Function to display final results
def display_results(score, total_questions):
    print(f"Quiz completed! Your score: {score}/{total_questions}")

# Function to play the quiz game
def play_quiz_game():
    welcome_message()
    user_answers = present_questions()
    score = calculate_score(user_answers)
    display_results(score, len(quiz_questions))
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_quiz_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_quiz_game()
