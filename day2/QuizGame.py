questions = [
    {"question": "India is a ____ country", "answer": "democratic"},
    {"question": "World richest man", "answer": "elon musk"},
    {"question": "Most luxury car in the world", "answer": "rolls royse"},
    {"question": "Computer only understand", "answer": "0 and 1"},
    {"question": "What is 5 factorial", "answer": "120"}
]

score = 0
print("------------- QUIZ GAME -------------")

for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    user_answer = input("Your answer: ").lower().strip()
    
    if user_answer == q["answer"].lower():
        print("Correct")
        score += 1
    else:
        print(f"Wrong The answer is: {q['answer']}")

print(f"\nFinal Score: {score}/{len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good job")
else:
    print("Keep practicing")