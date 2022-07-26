from question_model import Question
from quiz_brain import BrainOfgame
from data import question_data

question_bank=[Question(dict_1['text'],dict_1['answer']) for dict_1 in question_data ]




game_loop=BrainOfgame(question_bank)
game_loop.main_game_loop()
print(f"Your Final Score is:",game_loop.current_score,'/',len(game_loop.question_list))


