import christina

def move(spielfeld, aktueller_spieler):
    if aktueller_spieler == 0:
        zeichen = "X"
    elif aktueller_spieler == 1:
        zeichen = "O"
    while True:
        try:
            spalte = int(input("welche spalte möchtest du setzen?: "))
            if spalte >0 and spalte <8:
                for zeile in range(5, -1, -1):
                    if spielfeld[zeile][spalte-1] == " ":
                        spielfeld[zeile][spalte-1] = zeichen
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
    if aktueller_spieler == 0:
        zeichen = "X"
    elif aktueller_spieler == 1:
        zeichen = "O"
    for zeile in range(6):

        for spalte in range(4): 
            if (spielfeld[zeile][spalte] == zeichen and
                spielfeld[zeile][spalte+1] == zeichen and
                spielfeld[zeile][spalte+2] == zeichen and
                spielfeld[zeile][spalte+3] == zeichen):
                return True
            
    return False


def check_win(spielfeld, aktueller_spieler):
    check1 = check_horizontal(spielfeld, aktueller_spieler)
    check2 = christina.check_diagonal_down(spielfeld, aktueller_spieler)
    check3 = christina.check_diagonal_up(spielfeld, aktueller_spieler)
    check4 = christina.check_vertical(spielfeld, aktueller_spieler)
    if check1 == True or check2 == True or check3 == True or check4 == True:
        return True
    else:
        return False