import itertools



def win(current_tictac):

    def all_same(l):

        if l.count(l[0]) == len(l) and l[0] != 0:

            return True

        else:

            return False



    # horizontal win
    for row in tictac:

        print(row)

        if all_same(row):
            
            print(f"Player {row[0]} is the horizontal winner!")
            return True



    # vertical win
    for col in range(len(tictac[0])):

        check = []

        for row in tictac:

            check.append(row[col])

        if all_same(check):

            print(f"Player {check[0]} is the vertical winner!")
            return True



    # / diagonal win
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(tictac)))):
        
        diags.append(tictac[idx][reverse_idx])

    if all_same(diags):

        print(f"Player {diags[0]} is the diagonal winner /")
        return True

    # \ diagonal win
    diags = []
    for ix in range(len(tictac)):

        diags.append(tictac[ix][ix])

    if all_same(diags):

        print(f"Player {diags[0]} is the diagonal winner \\")
        return True

    return False



def tictac_board(tictac_map, player=0, row=0, column=0, just_display=False):

    try:
        if tictac_map[row][column] != 0:

            print("This block is played!")

            return Falsee

        print("   "+"  ".join([str(i) for i in range(len(tictac_map))]))
        if not just_display:

            tictac_map[row][column] = player

        for count, row in enumerate(tictac_map):

            print(count, row)

        return tictac_map
    except IndexError:
        print("you played out of range(index)")
        return False
    except Exception as e:

        print(str(e))

        return False




play = True
players = [1, 2]
while play:
    tictac =[[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    tictac_won = False
    player_cycle = itertools.cycle([1, 2])
    tictac_board(tictac, just_display=True)
    while not tictac_won:

        current_player = next(player_cycle)
        played = False

        while not played:

            print(f"Player: {current_player}")
            column_choice = int(input("Which column? "))
            row_choice = int(input("Which row? "))
            played = tictac_board(tictac, player=current_player, row=row_choice, column=column_choice)

        if win(tictac):

            tictac_won = True
            again = input("Would you like to play again? (y/n) ")

            if again.lower() == "y":

                print("restarting")

            elif again.lower() == "n":

                print("Hello!!")
                play = False

            else:

                print("Hello!!")
                play = False