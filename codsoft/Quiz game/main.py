def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
            "answer": "A"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
            "answer": "C"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
            "answer": "B"
        }
    ]

    score = 0

    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")
    
    print(f"Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz_game()
