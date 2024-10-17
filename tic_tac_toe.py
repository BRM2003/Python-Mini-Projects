from termcolor import colored, cprint
import string

class TicTacToe():
    __desk = []
    __players_points = {'X': 0, 'O': 0}

    def __init__(self, number=3, num_of_players=2):
        self.desk = number
        self.add_players(num_of_players - 2)
    
    @property
    def desk(self):
        return self.__desk

    @desk.setter
    def desk(self, number):
        if not 2 < number < 11:
            raise ValueError("The number of columns must be between 3 and 10")

        for _ in range(0, number):
            self.__desk.append([' '] * number)

    @property
    def desk_leng(self):
        return len(self.__desk)

    @property
    def points(self):
        return self.__players_points
    
    @property
    def players(self):
        return list(self.__players_points.keys())


    def add_players(self, number_of_players):
        if not 0 <= number_of_players < 4:
            raise ValueError("The number of players must be between 2 and 5")
        
        for i in range(number_of_players):
            self.__players_points[string.ascii_uppercase[i]] = 0


    def get_number_from_user(self, label, error_msg='Invalid number!'):
        while True:
            try:
                num = int(input(label).strip())
                if not 0 < num <= self.desk_leng:
                    raise ValueError
                return num
            except ValueError:
                print(error_msg)
    

    def clear_desk(self):
        for row in range(self.desk_leng):
            for cell in range(len(self.__desk[row])):
                self.__desk[row][cell] = ' '


    def cell_collor(self, mark):
        PLAYERS_COLOR = ['red', 'green', 'blue', 'yellow', 'magenta']
        color = PLAYERS_COLOR[self.players.index(mark)] if mark != " " else "white"
        return colored(mark, color)


    def show_desk(self):
        def calculate_count_of_columns():
            row_end, line = '', '---'
            for index in range(self.desk_leng):
                row_end += line + '+' if index < self.desk_leng - 1 else line
            return row_end
        
        row_line = calculate_count_of_columns()
        for row in self.__desk:
            attributes = ''
            print(row_line)
            for index, attr in enumerate(row):
                cell = self.cell_collor(attr)
                attributes += ' ' + (cell + ' |' if index < len(row) - 1 else cell)
            print(attributes)
        print(f"{row_line}\n")
    

    def set_value_to_spot(self, row, column, player=' '):
        if player.upper() not in self.players:
            print("Invalid player\n")
            return False

        if self.__desk[row][column] != ' ':
            print("This spot is already taken\n")
            return False
        
        self.__desk[row][column] = player.upper()
        return True
    

    def check_winner(self):
        def check_horizontal(desk):
            for row in desk:
                for i in range(len(row) - 2):  # Stop 2 indices before the end to avoid index out of range
                    if row[i] == row[i + 1] == row[i + 2] and row[i] != ' ':  # Check if three consecutive values are the same
                        return row[i]
            return False
        
        def check_decreasing_diagonal(desk):
            for row_i in range(self.desk_leng - 2):
                for column_i in range(len(desk[row_i]) - 2):
                    if desk[row_i][column_i] \
                        == desk[row_i + 1][column_i + 1] \
                        == desk[row_i + 2][column_i + 2] and desk[row_i][column_i] != ' ':
                        return desk[row_i][column_i]
            return False
        
        def check_increasing_diagonal(desk):
            for row_i in range(self.desk_leng - 2):
                for column_i in range(len(desk[row_i]) - 1, len(desk[row_i]) - row_i - 2, -1):
                    if desk[row_i][column_i] \
                        == desk[row_i + 1][column_i - 1] \
                        == desk[row_i + 2][column_i - 2] and desk[row_i][column_i] != ' ':
                        return self.__desk[row_i][column_i]
            return False

        def check_vertical(desk):
            for col in range(len(desk[0])): # Check if the value in this column is the same in the first, second, and third lists
                for row in range(len(desk) - 2):  # Stop 2 rows before the end
                    if desk[row][col] == desk[row+1][col] == desk[row+2][col] and desk[row][col] != ' ':
                        return desk[row][col]
            return False
        
        def check_draw(desk):
            for row in desk:
                for column in row:
                    if column == ' ':
                        return False
            return 'Draw!'
                    
        return check_decreasing_diagonal(self.__desk) \
            or check_increasing_diagonal(self.__desk) \
                    or check_horizontal(self.__desk) \
                        or check_vertical(self.__desk) \
                            or check_draw(self.__desk)


    def get_pozitions_from_user(self, player):
        while True:
            row = self.get_number_from_user(f"Enter row (1-{self.desk_leng}): ") - 1
            column = self.get_number_from_user(f"Enter column (1-{self.desk_leng}): ") - 1
            if self.set_value_to_spot(row, column, player):
                break


    def get_marks(self):
        return "\n".join([f"{self.cell_collor(player)} - {self.points[player]}" for player in self.players])


    def play_game(self, clear=True):
        move = 0

        if clear:
            self.clear_desk()

        self.show_desk()
        game_status = self.check_winner()

        while game_status == False:
            player = self.players[move % len(self.players)]
            print(f"Player {self.cell_collor(player)}'s turn")
            
            self.get_pozitions_from_user(player)
            
            self.show_desk()
            
            game_status = self.check_winner()
            move += 1
            
        if game_status == 'Draw!':
            cprint(game_status, 'white', 'on_red')
        else:
            self.points[game_status] += 1
            print(f"Player {self.cell_collor(game_status)} win!")
        print(self.get_marks())


    def __str__(self):
        self.show_desk()
        return self.get_marks()


if __name__ == "__main__":
    try:
        user_command = int(input("Enter the number of columns: ").strip() or 3)
        players = int(input("Enter the number of players: ").strip() or 2)
        start_game = TicTacToe(user_command, players)
        while str(user_command).lower() != 'n':
            start_game.play_game()
            user_command = input('Restart? (y/n) : ').strip()
    except Exception as e:
        print(str(e))