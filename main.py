from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    temp = Question(question['question'], question['correct_answer'])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()


print(f"You've completed the quiz, Your final score is: {quiz.score}/{quiz.question_number}")




