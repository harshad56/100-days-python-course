from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

qusetion_bank = []
for question in question_data:
    qusetion_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(qusetion_text, question_answer)
    qusetion_bank.append(new_question)

quiz = Quizbrain(qusetion_bank)

while quiz.still_has_qusetion():

    quiz.next_question()

print("you've completed the  quiz")
print(f"your final score was:{quiz.score}/{quiz.question_number}")
