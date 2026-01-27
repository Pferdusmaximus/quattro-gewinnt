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
    Mera.input_player(spieler)
    Mera.generate_board(spielfeld)

if __name__ == "__main__":
    main()