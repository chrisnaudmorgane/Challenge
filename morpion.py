# !/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

player = "X"  # Joueur actuel (X ou O)
board = [[" " for _ in range(3)] for _ in range(3)]  # Tableau pour stocker les cases
buttons = []  # Liste pour stocker les instances de boutons

def interface_menu():
    fenetre = tk.Tk()
    fenetre.title("TicTacToe")
    fenetre.geometry("800x600")

    menu_barre = tk.Menu(fenetre)
    menu_file = tk.Menu(menu_barre, tearoff=0)
    menu_barre.add_cascade(label="File", menu=menu_file)
    menu_file.add_command(label="nouveau", command=draw_grid)
    menu_file.add_separator()
    menu_file.add_command(label="Quitter", command=fenetre.quit)
    fenetre.config(menu=menu_barre)
    draw_grid()
    fenetre.mainloop()

def draw_grid():
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                bg="red", command=lambda x=i, y=j: handle_click(x, y))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

def handle_click(row, col):
    global player

    # Vérifier si la case est déjà occupée
    if board[row][col] != " ":
        return
    # Placer le symbole du joueur dans la case
    board[row][col] = player
    # Mettre à jour le texte du bouton correspondant
    buttons[row][col].config(text=player)
    # Vérifier si le joueur a gagné
    if check_win(player):
        messagebox.showinfo("Tic Tac Toe", f"Le joueur {player} a gagné !")
        reset_game()
    # Vérifier s'il y a égalité
    elif check_tie():
        messagebox.showinfo("Tic Tac Toe", "Égalité !")
        reset_game()
    else:
        # Passer au joueur suivant
        player = "O" if player == "X" else "X"

def check_win(player):
    # Vérifier les lignes
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Vérifier les colonnes
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Vérifier les diagonales
    if all(board[i][i] == player for i in range(3)) or \
        all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie():
    for row in board:
        if any(cell == " " for cell in row):
            return False
    return True

def reset_game():
    global player, board
    player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    interface_menu()