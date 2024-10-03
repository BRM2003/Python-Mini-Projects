import random

number_of_dice_rolled = 0

def throw_the_dices():
    global number_of_dice_rolled
    result = []
    count_of_dices = 0

    while count_of_dices <= 0:
        try:
            count_of_dices = int(input('How many dices do you wnat to roll? : '))
            
            if count_of_dices <= 0:
                print('The quantity of dices must be greater than 0') 
        except ValueError:
            print('Invalid choise!')
    
    number_of_dice_rolled += count_of_dices
    
    for _ in range(0, count_of_dices):
        result.append(random.randint(1, 6))
    
    print(result)


while True:
    command = input('Role the Dice? (y/n): ').lower()

    if command == 'n':
        print(f"You rolled {number_of_dice_rolled} times.\nThanks for Playing!")
        break

    throw_the_dices() if command == 'y' else print('Invalid choise!')
