def main():
    currentPlayer = "O"
    count = 0
    marks = [0,1,2,3,4,5,6,7,8]
    while(True):
        drawBoard(marks)
        if(winner(currentPlayer, marks)):
            print(f"Player {currentPlayer} wins!")
            return
        if(count == 9):
            print("It's a tie")
            return
        currentPlayer = "O" if currentPlayer == "X" else "X"
        mark = promptForMark(currentPlayer, marks)
        marks[mark] = currentPlayer
        count += 1
    
def promptForMark(player, marks):
    while(True):
        try:
            mark = int(input(f"Player '{player}', mark a spot: "))
        except ValueError:
            print("Invalid choice")
            continue
        if(marks[mark] == "X" or marks[mark] == "O"):
            print("That spot is taken")
        else:
            break
    return mark
    
def winner(player, list):
    return (list[0] == player and list[1] == player and list[2] == player) or \
         (list[3] == player and list[4] == player and list[5] == player) or \
         (list[6] == player and list[7] == player and list[8] == player) or \
         (list[0] == player and list[3] == player and list[6] == player) or \
         (list[1] == player and list[4] == player and list[7] == player) or \
         (list[2] == player and list[5] == player and list[8] == player) or \
         (list[0] == player and list[4] == player and list[8] == player) or \
         (list[2] == player and list[4] == player and list[6] == player)


def drawBoard(list):
    count = 0
    for el in list:
        if(count < 2):
            print(el, end=" | ")
            count += 1
        else:
            print(el)
            count = 0
    print()
        
main()