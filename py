import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("300x350")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_mode = "PvP"
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Helvetica", 12))
        self.label.pack(pady=10)

        # Mode buttons
        self.pvp_button = tk.Button(self.root, text="Player vs. Player", command=self.set_pvp_mode)
        self.pvp_button.pack(pady=5, side=tk.LEFT)
        self.pvc_button = tk.Button(self.root, text="Player vs. Computer", command=self.set_pvc_mode)
        self.pvc_button.pack(pady=5, side=tk.RIGHT)

        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = []
        for i in range(3):
            frame = tk.Frame(self.root)
            frame.pack()
            row = []
            for j in range(3):
                button = tk.Button(frame, text="", width=10, height=3, command=lambda row=i, col=j: self.on_button_click(row, col))
                button.pack(side=tk.LEFT)
                row.append(button)
            self.buttons.append(row)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")
                if self.game_mode == "PvC" and self.current_player == "O":
                    self.computer_move()

    def set_pvp_mode(self):
        self.game_mode = "PvP"
        self.reset_game()

    def set_pvc_mode(self):
        self.game_mode = "PvC"
        self.reset_game()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s Turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.on_button_click(row, col)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
