from random import randint
from time import sleep


class TicTacToe:

    def __init__(self):
        self.player_score = 0
        self.comp_score = 0
        self.playing = True
        self.positions = []
        self.approved_moves = [_ for _ in range(1, 10)]
        self.board_state = []
        self.game_board = None

    def play_game(self):
        self.positions = [(_ + 1) for _ in range(0, 9)]
        self.update_board()
        print("Welcome to Tic Tac Toe!")
        while self.playing:
            self.player_move()
            self.check_winner()
            if not self.playing:
                return

            self.comp_move()
            self.check_winner()
            if not self.playing:
                return

    def player_move(self):
        can_move = False
        try:
            chosen_pos = int(input("Please make your move by typing a number from 1-9 "
                                   "(whole numbers only): ")) - 1
            if chosen_pos not in range(0, 9) or self.positions[chosen_pos] not in self.approved_moves:
                raise ValueError
            else:
                can_move = True
                self.positions[chosen_pos] = "X"
                self.update_board()
        except ValueError:
            while not can_move:
                try:
                    chosen_pos = int(input("Incorrect input. Please make your move by typing a number from 1-9 "
                                           "(whole numbers only): ")) - 1
                    if chosen_pos not in range(0, 9) or self.positions[chosen_pos] not in self.approved_moves:
                        raise ValueError
                    else:
                        can_move = True
                        self.positions[chosen_pos] = "X"
                        self.update_board()
                except ValueError:
                    pass

    def comp_move(self):
        print("Computer is thinking...")
        sleep(2)
        chosen_pos = randint(0, len(self.positions) - 1)
        can_move = False
        while not can_move:
            if self.positions[chosen_pos] not in self.approved_moves:
                chosen_pos = randint(0, len(self.positions) - 1)
            else:
                print(f"Computer's move: Position {chosen_pos + 1}")
                can_move = True
        self.positions[chosen_pos] = "O"
        self.update_board()

    def update_board(self):
        rows = 3
        self.board_state = [[self.positions[_] for _ in range(0,3)],
                            [self.positions[_] for _ in range(3,6)],
                            [self.positions[_] for _ in range(6,9)]]
        self.game_board = f" ___________\n"
        for _ in range(0, rows):
            count = _ * 3
            self.game_board += f"| {self.positions[count]} | {self.positions[count+1]} | {self.positions[count+2]} |\n" \
                               f"|___|___|___|\n"
        print(self.game_board)

    def check_winner(self):
        #--- Check columns ---#
        self.reset_score()
        for column in range(0, 3):
            for row in self.board_state:
                if row[column] == "X":
                    self.player_score += 1
                elif row[column] == "O":
                    self.comp_score += 1
                if self.player_score == 3 or self.comp_score == 3:
                    self.playing = False
                    self.declare_winner()
                    return
            self.reset_score()

        #--- Check rows ---#
        self.reset_score()
        for row in self.board_state:
            for symbol in row:
                if symbol == "X":
                    self.player_score += 1
                elif symbol == "O":
                    self.comp_score += 1
            if self.player_score == 3 or self.comp_score == 3:
                self.playing = False
                self.declare_winner()
                return
            self.reset_score()

        #--- Check diagonals ---#
        self.reset_score()
        pos_to_check = 0
        for row in self.board_state:
            if row[pos_to_check] == "X":
                self.player_score += 1
            elif row[pos_to_check] == "O":
                self.comp_score += 1
            pos_to_check += 1
        if self.player_score == 3 or self.comp_score == 3:
            self.playing = False
            self.declare_winner()
            return

        self.reset_score()
        pos_to_check = 0
        for row in reversed(self.board_state):
            if row[pos_to_check] == "X":
                self.player_score += 1
            elif row[pos_to_check] == "O":
                self.comp_score += 1
            pos_to_check += 1
        if self.player_score == 3 or self.comp_score == 3:
            self.playing = False
            self.declare_winner()
            return

    def declare_winner(self):
        #--- Return winner if any ---#
        draw = False
        print(f"Player score: {self.player_score}")
        print(f"Computer score: {self.comp_score}")
        if self.player_score == 3:
            print("Congratulations! You win!")
            self.play_again()
        elif self.comp_score == 3:
            print("You lose.")
            self.play_again()
        else:
            print(f"Current positions: {self.positions}")
            print(f"Approved moves: {self.approved_moves}")
            self.play_again()
            # for value in self.positions:
            #     if value not in self.approved_moves:
            #         draw = True
            #     else:
            #         draw = False
            # if draw:
            #     print("It's a draw.")
            #     self.play_again()

    def play_again(self):
        legal_choices = ("Y", "N")
        choice = input("Play again? Y/N: ").upper()
        while choice not in legal_choices:
            choice = input("Incorrect input. Play again? Y/N: ").upper()
        if choice == "Y":
            self.playing = True
            self.play_game()
        elif choice == "N":
            print("Thank you for playing!")
            self.playing = False

    def reset_score(self):
        self.player_score = 0
        self.comp_score = 0
