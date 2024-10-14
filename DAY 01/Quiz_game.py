def quiz_game():
    #List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer": "c"
            
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
            "answer": "b"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["a) Charles Dickens", "b) Jane Austen", "c) Mark Twain", "d) William Shakespeare"],
            "answer": "d"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Great White Shark"],
            "answer": "b"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["a) Gold", "b) Oxygen", "c) Osmium", "d) Silver"],
            "answer": "b"
        }
    ]

    score = 0  # Initialize the user's score

    print("Welcome to the Quiz Game!")
    print("You will be asked 5 questions. Let's see how many you can answer correctly!\n")

    # Iterate through each question
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter the letter of your answer (a, b, c, or d): ").lower()

        # Check if the user's answer is correct
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Display the final score
    print(f"Quiz finished! Your final score is: {score} out of {len(questions)}")

# Start the quiz game
quiz_game()
