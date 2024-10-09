from termcolor import cprint
import random
import string

QUESTION_TEXT = 'question'
QUESTION_INCORRECT_OPTIONS_TEXT = 'incorrect_options'
QUESTION_ANSWER_TEXT = 'answer'


def get_swapped_options(options, answer):
    result = [option.title() for option in options]
    result.append(answer.title())
    random.shuffle(result)
    return result


def ask_question(index, question, options, answer):
    swapped_options = get_swapped_options(options, answer)
        
    print(f"Question {index}: {question}")

    for num in range(0, len(swapped_options)):
        print(f"{string.ascii_uppercase[num]}. {swapped_options[num]}")

        if swapped_options[num] == answer.title():
            correct_answer = [string.ascii_uppercase[num], swapped_options[num]]
    
    return input('Your answer: ').title().strip(), correct_answer


def play_game(quiz):
    random.shuffle(quiz)
    score = 0

    for index, question in enumerate(quiz, 1):
        answer, correct_answer = ask_question(
            index, 
            question[QUESTION_TEXT], 
            question[QUESTION_INCORRECT_OPTIONS_TEXT], 
            question[QUESTION_ANSWER_TEXT]
        )

        if answer in (correct_answer):
            cprint('Correct!\n', 'green')
            score += 1
        else:
            cprint(f"Wrong! The correct answer is {correct_answer[0]} - {correct_answer[1]}\n", 'red')

    print(f'Quiz over! Your final score is {score} out of {len(quiz)}')


def main():
    questions = [
        {
            QUESTION_TEXT: 'What is the capital of France?',
            QUESTION_INCORRECT_OPTIONS_TEXT: ['berlin', 'madrid', 'rome'],
            QUESTION_ANSWER_TEXT: 'paris'
        },
        {
            QUESTION_TEXT: 'Which planet is known as the red planet?',
            QUESTION_INCORRECT_OPTIONS_TEXT: ['jupiter', 'earth', 'saturn'],
            QUESTION_ANSWER_TEXT: 'mars'
        },
        {
            QUESTION_TEXT: 'What is the largest ocean on Earth?',
            QUESTION_INCORRECT_OPTIONS_TEXT: ['Atlantic', 'indian', 'arctic'],
            QUESTION_ANSWER_TEXT: 'pacific'
        }
    ]
    play_game(questions)

if __name__ == "__main__":
    main()



