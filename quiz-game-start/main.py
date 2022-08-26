from question_model import Question
from data import question_data, new_question_data
from quiz_brain import QuizBrain

question_bank = []
for question in new_question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the challenge!")
print(f"Your Final Score is {quiz.score}/{quiz.question_number}")
