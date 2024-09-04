import random
import time

def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def main_menu():
    print("Welcome to the Football Quiz!")
    print("\n" + "-"*40)
    print("1. Start Quiz")
    print("2. View High Score")
    print("3. Exit")
    print("-"*40)

    while True:
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            football_quiz()
            break
        elif choice == '2':
            high_score = load_high_score()
            print(f"\nThe current high score is: {high_score}")
            print("-"*40)
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def football_quiz():
    high_score = load_high_score()
    questions = [
        {
            "question": "Which country has won the most FIFA World Cup titles?",
            "options": ["A) Brazil", "B) Germany", "C) Italy", "D) Argentina"],
            "answer": "A"
        },
        {
            "question": "Who is the all-time top scorer in the UEFA Champions League?",
            "options": ["A) Lionel Messi", "B) Cristiano Ronaldo", "C) Robert Lewandowski", "D) Raul"],
            "answer": "B"
        },
        {
            "question": "Which country hosted the 2018 FIFA World Cup?",
            "options": ["A) Brazil", "B) Russia", "C) South Africa", "D) Germany"],
            "answer": "B"
        },
        {
            "question": "Which player won the Ballon d'Or in 2022?",
            "options": ["A) Karim Benzema", "B) Lionel Messi", "C) Robert Lewandowski", "D) Luka Modric"],
            "answer": "A"
        },
        {
            "question": "Which club has won the most UEFA Champions League titles?",
            "options": ["A) Barcelona", "B) AC Milan", "C) Real Madrid", "D) Bayern Munich"],
            "answer": "C"
        },
        {
            "question": "Which team won the English Premier League in the 2020-2021 season?",
            "options": ["A) Manchester City", "B) Manchester United", "C) Liverpool", "D) Chelsea"],
            "answer": "A"
        },
        {
            "question": "Who holds the record for the most goals scored in a single Premier League season?",
            "options": ["A) Mohamed Salah", "B) Thierry Henry", "C) Cristiano Ronaldo", "D) Alan Shearer"],
            "answer": "A"
        },
        {
            "question": "Which country won the first-ever FIFA World Cup in 1930?",
            "options": ["A) Brazil", "B) Argentina", "C) Uruguay", "D) Italy"],
            "answer": "C"
        },
        {
            "question": "Which player has won the most Ballon d'Or awards?",
            "options": ["A) Lionel Messi", "B) Cristiano Ronaldo", "C) Michel Platini", "D) Johan Cruyff"],
            "answer": "A"
        },
        {
            "question": "Which club is known as 'The Red Devils'?",
            "options": ["A) Liverpool", "B) Arsenal", "C) Manchester United", "D) Bayern Munich"],
            "answer": "C"
        },
        {
            "question": "Which player holds the record for the most goals scored in a single FIFA World Cup tournament?",
            "options": ["A) Miroslav Klose", "B) Just Fontaine", "C) Pelé", "D) Gerd Müller"],
            "answer": "B"
        },
        {
            "question": "Which club did Thierry Henry return to in 2012 after playing for Barcelona?",
            "options": ["A) Arsenal", "B) New York Red Bulls", "C) Monaco", "D) Juventus"],
            "answer": "A"
        },
        {
            "question": "Who won the Golden Boot at the 2018 FIFA World Cup?",
            "options": ["A) Harry Kane", "B) Antoine Griezmann", "C) Kylian Mbappé", "D) Luka Modrić"],
            "answer": "A"
        },
        {
            "question": "Which football club is nicknamed 'The Old Lady'?",
            "options": ["A) Real Madrid", "B) Bayern Munich", "C) Juventus", "D) Inter Milan"],
            "answer": "C"
        },
        {
            "question": "Who is the youngest player to score in a World Cup final?",
            "options": ["A) Lionel Messi", "B) Pelé", "C) Kylian Mbappé", "D) Ronaldo Nazário"],
            "answer": "B"
        }
    ]

    random.shuffle(questions)

    print("\nYou have 10 seconds to answer each question.")
    print("Please only respond with A, B, C, or D.")
    print("\n" + "-"*40)

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}/{len(questions)}: {q['question']}")
        for option in q['options']:
            print(option)
        print("You have 10 seconds to answer.")

        start_time = time.time()

        # Input validation loop with timer
        while True:
            answer = input("Your answer (A, B, C, or D): ").upper()
            elapsed_time = time.time() - start_time

            if elapsed_time > 10:  # 10-second limit per question
                print("Time's up! You didn't answer in time.")
                break

            if answer in ['A', 'B', 'C', 'D']:
                if answer == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}.")
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        print("\n" + "-"*40)

    print(f"\nQuiz complete! Your final score is {score}/{len(questions)} Well Done!")
    print("\n" + "-"*40)

    if score > high_score:
        print(f"New high score! Previous high score was {high_score}.")
        save_high_score(score)
    else:
        print(f"Your score is {high_score}. Keep trying to beat that high score!")

if __name__ == "__main__":
    main_menu()
