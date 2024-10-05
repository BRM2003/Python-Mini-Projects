import random

USER_NAME = 'user'
COMPUTER_NAME = 'computer'
_rock_paper_scissor_info = {
    'r': {'weakness': 'p', 'icon': '🪨'}, 
    'p': {'weakness': 's', 'icon': '📃'}, 
    's': {'weakness': 'r', 'icon': '✄'}
}
_rock_paper_scissor = tuple(_rock_paper_scissor_info.keys())
count_of_winns = {USER_NAME: 0, COMPUTER_NAME: 0}


def rematch_game():
    count_of_winns[USER_NAME] = 0
    count_of_winns[COMPUTER_NAME] = 0

def get_user_choise(list_of_choises):
    while True:
        user_choise = input('Rock, paper, or scissors? (r/p/s): ')[0].lower()

        if user_choise in list_of_choises:
            return user_choise
        print('Invalid choice!')
        

def get_computer_choise(list_of_choise, user_choise):
    computer_choise = random.choice(list_of_choise)
    
    print('You chose', _rock_paper_scissor_info[user_choise]['icon'])
    print('Computer chose', _rock_paper_scissor_info[computer_choise]['icon'])

    return computer_choise


def determine_winner(winner):
    count_of_winns[winner] += 1
    print(f"\nUser - {count_of_winns[USER_NAME]}\t||\t{count_of_winns[COMPUTER_NAME]} - Computer\n")


def play_game():
    while True:
        user_choise = get_user_choise(_rock_paper_scissor)
        computer_choise = get_computer_choise(_rock_paper_scissor, user_choise)

        determine_winner(COMPUTER_NAME) if _rock_paper_scissor_info[user_choise]['weakness'] == computer_choise else \
            determine_winner(USER_NAME) if _rock_paper_scissor_info[computer_choise]['weakness'] == user_choise else \
                print('Draw!')

        if count_of_winns[USER_NAME] >= 2 or count_of_winns[COMPUTER_NAME] >= 2:
            print('You Win!') if count_of_winns[USER_NAME] >= 2 else print('You Lose!')
            if input('Rematch? (y/n): ')[0].lower() != 'y':
                break
            rematch_game()

play_game()
