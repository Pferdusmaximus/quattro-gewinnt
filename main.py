import christina
import nils
import Mera

spielfeld = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]

spieler = []


def main():
    aktueller_spieler = 1
    Mera.input_player(spieler)

    Mera.clear_screen()

    while True:
        if aktueller_spieler == 0: 
            aktueller_spieler = 1
        elif aktueller_spieler == 1:
            aktueller_spieler = 0

        Mera.generate_board(spielfeld)
        nils.move(spielfeld, aktueller_spieler)
        Mera.clear_screen()

        check = nils.check_win(spielfeld, aktueller_spieler)
        if check == True:
            print(f"{spieler[aktueller_spieler]} hat gewonnen!")
            break
        elif check == False:
            continue

if __name__ == "__main__":
    main()