import christina

def move(spielfeld, aktueller_spieler):
    while True:
        try:
            spalte = int(input("welche spalte möchtest du setzen?: "))
            if spalte >0 and spalte <8:
                for zeile in range(5, -1, -1):
                    if spielfeld[zeile][spalte] == " ":
                        spielfeld[zeile][spalte] = aktueller_spieler
                        return
                    
                    else:
                        print("diese spalte ist voll")
                        continue
            else:
                print("nur eine Zahl von 1-7 eingeben!")
                continue
        except ValueError:
            print("nur eine Zahl von 1-7 eingeben!")
            continue


def check_horizontal(spielfeld, aktueller_spieler):
    for zeile in range(6):

        for spalte in range(4): 
            if (spielfeld[zeile][spalte] == aktueller_spieler and
                spielfeld[zeile][spalte+1] == aktueller_spieler and
                spielfeld[zeile][spalte+2] == aktueller_spieler and
                spielfeld[zeile][spalte+3] == aktueller_spieler):
                return True
            
    return False


def check_win():
    check_horizontal()
    christina.check_diagonal_down()
    christina.check_diagonal_up()
    christina.check_vertical()