import os

#Zuweisung Spieler
spieler_1_symbol = "x"
spieler_2_symbol = "o"
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#Spielereingabe
def input_player(spieler):
    spieler_1 = ""
    while spieler_1.strip() == "":
        spieler_1 = input("Spieler 1 bitte benennen: ")
        spieler.append(spieler_1)
    spieler_2 = ""
    while spieler_2.strip() == "":
        spieler_2 = input("Spieler 2 bitte benennen: ")
        spieler.append(spieler_2)

def generate_board(spielfeld):
    # spielfeld = [[" " for _ in range(7)] for _ in range(6)]
    print("    1   2   3   4   5   6   7")
    for i in range(6):
        print(i+1, " ", spielfeld[i][0], "|", spielfeld[i][1], "|", spielfeld[i][2], "|", spielfeld[i][3], "|", spielfeld[i][4], "|", spielfeld[i][5], "|", spielfeld[i][6])
        if i < 5: 
            print("  ----+---+---+---+---+---+----")