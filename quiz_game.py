from termcolor import cprint
from pathlib import Path
import random
import string
import json
import sys

QUESTION_TEXT = 'question'
QUESTION_INCORRECT_OPTIONS_TEXT = 'incorrect_options'
QUESTION_ANSWER_TEXT = 'answer'

class QuizGame:
    quiz = []
    score = 0

    def __init__(self, quiz):
        self.quiz = quiz

    @classmethod
    def get_swapped_options(self, options, answer):
        result = [option.title() for option in options]
        result.append(answer.title())
        random.shuffle(result)
        return result

    @classmethod
    def ask_question(self, index, question, options, answer):
        swapped_options = self.get_swapped_options(options, answer)
            
        print(f"Question {index}: {question}")

        for num in range(0, len(swapped_options)):
            print(f"{string.ascii_uppercase[num]}. {swapped_options[num]}")

            if swapped_options[num] == answer.title():
                correct_answer = [string.ascii_uppercase[num], swapped_options[num]]
        
        return input('Your answer: ').title().strip(), correct_answer


    def play_game(self):
        random.shuffle(self.quiz)
        for index, question_data in enumerate(self.quiz, 1):
            answer, correct_answer = self.ask_question(
                index, 
                question_data[QUESTION_TEXT], 
                question_data[QUESTION_INCORRECT_OPTIONS_TEXT], 
                question_data[QUESTION_ANSWER_TEXT]
            )

            if answer in (correct_answer):
                cprint('Correct!\n', 'green')
                self.score += 1
            else:
                cprint(f"Wrong! The correct answer is {correct_answer[0]} - {correct_answer[1]}\n", 'red')
        print('Quiz over!')

    def show_score(self):
        print(f'Your score is {self.score} out of {len(self.quiz)}')



def read_file(command_arguments, task='r'):
    if len(command_arguments) > 2:
        json_file = command_arguments[2]
        if not Path(json_file).is_file() or not json_file.endswith('.json'):
            raise BaseException("Enter valid path to JSON")
    else:
        while True:
            json_file = input('Please, eneter the path to the json file: ').strip()
            if Path(json_file).is_file() and json_file.endswith('.json'):
                break
            print('Enter valid path to JSON file')
    return Path(json_file).read_text()


def read_questions_from_json(command_arguments):
    data = list(json.loads(read_file(command_arguments)))
    return data

def main():
    command_arguments = sys.argv
    try:
        if command_arguments[1] in ['-r', '-c', '-w']:
            if command_arguments[1] == '-r':
                game = QuizGame(read_questions_from_json(command_arguments))
                game.play_game()
                game.show_score()
    except IndexError:
        cprint("\nThe command format should like: python quiz_game.py ( -r / -c / -w ) <file_name>", "white", "on_red")

if __name__ == "__main__":
    main()



