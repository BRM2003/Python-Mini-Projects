class TicTacToe():
    desk = []
    win_row = 0
    desk_leng = 0

    PLAYERS = ['X', 'O']

    def __init__(self, number=3, win_row=3):
        if number < 3:
            raise Exception("The number of columns can't be less than 3")
        for _ in range(0, number):
            self.desk.append([' '] * number)
        self.win_row = win_row
        self.desk_leng = len(self.desk)
        


    def show_desk(self):
        def calculate_count_of_columns():
            row_end, line = '', '---'
            for index in range(self.desk_leng):
                row_end += line + '+' if index < self.desk_leng - 1 else line
            return row_end
        
        row_line = calculate_count_of_columns()
        for row in self.desk:
            attributes = ''
            print(row_line)
            for index, attr in enumerate(row):                
                attributes += ' ' + (attr + ' |' if index < len(row) - 1 else attr)
            print(attributes)
        print(f"{row_line}\n")


    def enter_position(self, label):
        while True:
            try:
                user_value = int(input(f"Enter {label} (1-{self.desk_leng}): "))

                if user_value > self.desk_leng or user_value <= 0:
                    raise ValueError
                
                return user_value - 1
            except ValueError:
                print('Invalid input!')
    

    def set_value(self, row, column, player=' '):
        if player.upper() not in self.PLAYERS:
            print("Invalid player\n")
            return False

        if self.desk[row][column] != ' ':
            print("This spot is already taken\n")
            return False
        
        self.desk[row][column] = player.upper()
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
                        return self.desk[row_i][column_i]
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
                    
        return check_decreasing_diagonal(self.desk) \
            or check_increasing_diagonal(self.desk) \
                    or check_horizontal(self.desk) \
                        or check_vertical(self.desk) \
                            or check_draw(self.desk)


    def get_pozitions_from_user(self, player):
        while True:
            row, column = self.enter_position('row'), self.enter_position('column')
            if self.set_value(row, column, player):
                break


    def play_game(self):
        move = 0
        self.show_desk()

        game_status = self.check_winner()
        while game_status == False:
            print(f"Player {self.PLAYERS[move % 2]}'s turn")
            
            self.get_pozitions_from_user(self.PLAYERS[move % 2])
            
            self.show_desk()
            
            game_status = self.check_winner()
            move += 1

        print(game_status) if game_status == 'Draw!' else print(f"Player {game_status} win!") 

        
try:
    num_of_col = int(input("Enter the number of columns: "))
    start_game = TicTacToe(num_of_col)
    start_game.play_game()
except Exception as e:
    print(str(e))