from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# create a list with Question objects
question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)  # get a list and return a QuizBrain object
quiz_ui = QuizInterface(quiz)  # get a QuizBrain object and create interface
