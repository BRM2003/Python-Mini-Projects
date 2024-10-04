import random
import math

while True:
    try:
        min_value = int(input('Set the minimum number: '))
        max_value = int(input('Set the maximum number: '))
        break
    except ValueError:
        print('Please enter a valid number')

attempts = math.ceil((max_value - min_value) / 3) if math.ceil((max_value - min_value) / 3) <= 20 else 20  # Determines the number of attempts, but not more than 10
number = random.randint(min_value, max_value)  
user_answer = -1

print(f'You have {attempts} attampts')

while user_answer != number:
    try:
        user_answer = int(input(f'Guess the number between {min_value} and {max_value}: '))

        if not min_value <= user_answer <= max_value:
            print('You put the number out of range!')
            continue

        
        print('Too high!') if user_answer > number else \
            print('Too low!') if user_answer < number else \
                print('Congratulations! You guessed the number.')
        
        attempts -= 1
        if user_answer != number:
            if attempts <= 0:
                print("You've got no more attempts left")
                break
            else:
                print(f'You have {attempts} attampts')

    except ValueError:
        print('Please enter a valid number')