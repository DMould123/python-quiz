import random

def football_quiz():
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
        }
    ]

    random.shuffle(questions)

    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()

        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nQuiz completed! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    football_quiz()
