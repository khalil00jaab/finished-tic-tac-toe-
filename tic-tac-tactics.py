import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("TIC-TAC-TOE")

chiffres = list(range(1, 10))

mark = ''

count = 0
panneaux = ['placeholder'] + [''] * 9


def verification(chiffre):
    global count, mark, chiffres

    # 3 à 10. Gestion des valeurs de chiffres différentes de 1 à 9
    if chiffre in chiffres:
        if panneaux[chiffre] == '':
            count += 1
            if count % 2 == 0:
                mark = 'O'
            else:
                mark = 'X'

            # 6. Mise à jour du bouton correspondant sur le plateau de jeu
            panneaux[chiffre] = mark
            update_button(chiffre, mark)

            # 8. Vérification si le joueur actuel a gagné
            if win(mark):
                messagebox.showinfo("Fin de partie", f"Joueur {mark} gagne!")
                window.destroy()

            # 11. Vérification si la partie est terminée par une égalité
            elif count > 8:
                messagebox.showinfo("Fin de partie", "Match nul!")
                window.destroy()
        else:
            messagebox.showerror("Erreur", "La case est déjà occupée!")
    else:
        messagebox.showerror("Erreur", "Chiffre invalide!")

def win(mark):
    # Définition des conditions de victoire
    conditions_victoire = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # lignes
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # colonnes
        [1, 5, 9], [3, 5, 7]  # diagonales
    ]

    # Vérification de chaque condition de victoire
    for condition in conditions_victoire:
        if all(panneaux[position] == mark for position in condition):
            return True
    return False

def update_button(chiffre, mark):
    buttons[chiffre].config(text=mark)

buttons = {}
for i in range(1, 10):
    buttons[i] = tk.Button(window, text='', width=10, height=4, command=lambda i=i: verification(i))
    buttons[i].grid(row=(i - 1) // 3, column=(i - 1) % 3)

window.mainloop()
