from tkinter import *
import random
import json
from datetime import datetime


class Joc(Tk):
    # ==== adding necessary class variables
    game_board = []
    new_random_tiles = [2, 2, 2, 2, 2, 2, 4]
    score = 0
    high_score = 0
    game_score = 0
    highest_score = 0
    square = {}

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.game_score = StringVar(self)
        self.game_score.set("0")
        self.highest_score = StringVar(self)
        self.highest_score.set(self.incarcaScorul())

        # ==== adding new game , score and highest score option
        self.button_frame = Frame(self)
        self.button_frame.grid(row=2, column=0, columnspan=4)
        Button(self.button_frame, text="New Game", font=("times new roman", 15), command=self.new_game).grid(row=0,
                                                                                                             column=0)
        self.button_frame.pack(side="top")

        Label(self.button_frame, text="Score:", font=("times new roman", 15)).grid(row=0, column=1)
        Label(self.button_frame, textvariable=self.game_score, font=("times new roman", 15)).grid(row=0, column=2)
        Label(self.button_frame, text="Record:", font=("times new roman", 15)).grid(row=0, column=3)
        Label(self.button_frame, textvariable=self.highest_score, font=("times new roman", 15)).grid(row=0, column=4)

        self.canvas = Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=False)

        # ==== create new game
        self.new_game()

        # ==== add new tiles in python 2048 game

    def new_tiles(self):
        index = random.randint(0, 6)
        x = -1
        y = -1

        # ==== check while game is not over
        while not self.full():
            x = random.randint(0, 3)
            y = random.randint(0, 3)

            if self.game_board[x][y] == 0:
                self.game_board[x][y] = self.new_random_tiles[index]
                x1 = y * 105
                y1 = x * 105
                x2 = x1 + 105 - 5
                y2 = y1 + 105 - 5
                num = self.game_board[x][y]
                if num == 2:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#e0f2f8", tags="rect",
                                                                     outline="", width=0)
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="2")
                elif num == 4:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#b8dbe5", tags="rect",
                                                                     outline="", width=0)
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="4")
            break

        # ==== showing game board in python 2048 game

    def show_board(self):
        cellwidth = 105
        cellheight = 105
        for column in range(4):
            for row in range(4):
                x1 = column * cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth - 5
                y2 = y1 + cellheight - 5
                num = self.game_board[row][column]

                if num == 0:
                    self.show_number0(row, column, x1, y1, x2, y2)
                else:
                    self.show_number(row, column, x1, y1, x2, y2, num)

        # ==== show board block when it is empty

    def show_number0(self, row, column, a, b, c, d):
        self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#f5f5f5", tags="rect", outline="")
        # ==== show board number

    def show_number(self, row, column, a, b, c, d, num):
        bg_color = {'2': '#eee4da', '4': '#ede0c8', '8': '#edc850', '16': '#edc53f', '32': '#f67c5f', '64': '#f65e3b',
                    '128': '#edcf72', '256': '#edcc61', '512': '#f2b179', '1024': '#f59563', '2048': '#edc22e', }
        color = {'2': '#776e65', '4': '#f9f6f2', '8': '#f9f6f2', '16': '#f9f6f2', '32': '#f9f6f2', '64': '#f9f6f2',
                 '128': '#f9f6f2', '256': '#f9f6f2', '512': '#776e65', '1024': '#f9f6f2', '2048': '#f9f6f2', }
        # print(num)

        self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill=bg_color[str(num)], tags="rect",
                                                                outline="")
        self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill=color[str(num)], text=str(num))

    def full(self):
        for row in self.game_board:
            if 0 in row:
                return False
        return True

    def new_game(self):
        self.score = 0
        self.game_score.set("0")
        self.game_board = []
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.game_board[x][y] == 0:
                self.game_board[x][y] = 2
                break

        index = random.randint(0, 6)
        while not self.full():
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.game_board[x][y] == 0:
                self.game_board[x][y] = self.new_random_tiles[index]
                break
        self.show_board()
        self.salveazainFisier()

    # ==== check for game won
    def game_status(self, gameover: list):
        gameover2 = "\n".join([" ".join(inner_list) for inner_list in gameover])
        print(gameover2)
        cellwidth = 105
        cellheight = 105
        self.square = {}
        for column in range(2,3):
            for row in range(2,3):
                a = column * cellwidth
                b = row * cellheight
                c = a + cellwidth - 105
                d = b + cellheight - 50
                self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#ede0c8", tags="rect",
                                                                        outline="")
                self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill="#494949",
                                        text=gameover2)

    def game_over(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if self.game_board[i][j] == 2048:
                    gamewon = [["Y", "O", "U", ""], ["", "", "", ""], ["W", "O", "N", "!"], ["", "", "", ""]]
                    self.game_status(gamewon)
                    self.salveazainFisier()
        for i in range(0, 4):
            for j in range(0, 4):
                if self.game_board[i][j] == 0:
                    return False
        for i in range(0, 4):
            for j in range(0, 3):
                if self.game_board[i][j] == self.game_board[i][j + 1]:
                    return False
        for j in range(0, 4):
            for i in range(0, 3):
                if self.game_board[i][j] == self.game_board[i + 1][j]:
                    return False

        gameover = [["G", "A", "M", "E", ], ["", "", "", ""], ["O", "V", "E", "R"], ["", "", "", ""]]
        self.game_status(gameover)
        self.salveazainFisier()

    # ==== moves by user
    def moves(self, event):

        if event.keysym == 'Down':
            for j in range(0, 4):
                shift = 0
                for i in range(3, -1, -1):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if i - 1 >= 0 and self.game_board[i - 1][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i - 1][j] = 0
                        elif i - 2 >= 0 and self.game_board[i - 1][j] == 0 and self.game_board[i - 2][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i - 2][j] = 0
                        elif i == 3 and self.game_board[2][j] + self.game_board[1][j] == 0 and self.game_board[0][j] == self.game_board[3][j]:
                            self.game_board[3][j] *= 2
                            self.score += self.game_board[3][j]
                            self.game_board[0][j] = 0
                        if shift > 0:
                            self.game_board[i + shift][j] = self.game_board[i][j]
                            self.game_board[i][j] = 0
            self.show_board()
            self.new_tiles()
            self.game_over()
        elif event.keysym == 'Right':
            for i in range(0, 4):
                shift = 0
                for j in range(3, -1, -1):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if j - 1 >= 0 and self.game_board[i][j - 1] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j - 1] = 0
                        elif j - 2 >= 0 and self.game_board[i][j - 1] == 0 and self.game_board[i][j - 2] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j - 2] = 0
                        elif j == 3 and self.game_board[i][2] + self.game_board[i][1] == 0 and self.game_board[0][j] == self.game_board[3][j]:
                            self.game_board[i][3] *= 2
                            self.score += self.game_board[i][3]
                            self.game_board[i][0] = 0
                        if shift > 0:
                            self.game_board[i][j + shift] = self.game_board[i][j]
                            self.game_board[i][j] = 0
            self.show_board()
            self.new_tiles()
            self.game_over()
        elif event.keysym == 'Left':
            for i in range(0, 4):
                shift = 0
                for j in range(0, 4):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if j + 1 < 4 and self.game_board[i][j + 1] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j + 1] = 0
                        elif j + 2 < 4 and self.game_board[i][j + 1] == 0 and self.game_board[i][j + 2] == \
                                self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i][j + 2] = 0
                        elif j == 0 and self.game_board[i][1] + self.game_board[i][2] == 0 and self.game_board[i][3] == self.game_board[i][0]:
                            self.game_board[i][0] *= 2
                            self.score += self.game_board[i][0]
                            self.game_board[i][3] = 0
                        if shift > 0:
                            self.game_board[i][j - shift] = self.game_board[i][j]
                            self.game_board[i][j] = 0
            self.show_board()
            self.new_tiles()
            self.game_over()
        elif event.keysym == 'Up':
            for j in range(0, 4):
                shift = 0
                for i in range(0, 4):
                    if self.game_board[i][j] == 0:
                        shift += 1
                    else:
                        if i + 1 < 4 and self.game_board[i + 1][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i + 1][j] = 0
                        elif i + 2 < 4 and self.game_board[i + 1][j] == 0 and self.game_board[i + 2][j] == self.game_board[i][j]:
                            self.game_board[i][j] *= 2
                            self.score += self.game_board[i][j]
                            self.game_board[i + 2][j] = 0
                        elif i == 0 and self.game_board[1][j] + self.game_board[2][j] == 0 and self.game_board[3][j] == self.game_board[0][j]:
                            self.game_board[0][j] *= 2
                            self.score += self.game_board[0][j]
                            self.game_board[3][j] = 0
                        if shift > 0:
                            self.game_board[i - shift][j] = self.game_board[i][j]
                            self.game_board[i][j] = 0
            self.show_board()
            self.new_tiles()
            self.game_over()

        self.game_score.set(str(self.score))
        if self.score > self.high_score:
            self.high_score = self.score
            self.highest_score.set(str(self.high_score))

    def salveazainFisier(self):
        with open("log.json", "w") as f:
            json.dump({"Data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'scor': self.high_score}, f, indent=4)

    def incarcaScorul(self):
        with open("log.json", "r") as f:
            data = json.load(f)
            return data["scor"]
