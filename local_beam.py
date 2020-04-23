import secrets
import math
from time import perf_counter
# the new idea is to simplify the code and use only one lest of N length to save space such that each element represent
# the position of the queen in each column
#[1,2,3,4,5,6,7,8]
#[1:1, 2:2...]


def board_printer(board,n_queen):
    locations = list()
    for key in board:
        locations.append(board[key])
    row = 1
    column = 1
    counter = 1
    print(locations)
    while counter <= n_queen:
        if row == locations[counter-1]:
            print(' 1 ', end="")
        else:
            print(" 0 ", end="")
        if counter == n_queen and row != n_queen:
            print()
            counter = 1
            row += 1
            continue
        counter += 1
    print()


def conflicts_getter(board, N_Queens):
    initial_position = list(board.values())
    # now how many conflicts do i have and to what queen
    # there is no vertical conflicts thanks to our initilization and how this code works
    # now let's check for horizontal conflicts
    # conflictH_dict is for horizntal conflicts for each column
    conflictH_dict = dict()
    counter = 1
    while counter <= N_Queens:
        conflictH_dict[counter] = 0
        counter += 1

    number_of_Hconflicts = 0
    counted_columns = set()
    counter = 0
    # becarefull from over counting
    while counter < len(initial_position):
        myPosition = initial_position[counter]
        counted_columns.add(counter)
        innercounter = 0
        while innercounter < len(initial_position):
            if myPosition == initial_position[innercounter] and innercounter != counter and (innercounter not in counted_columns):
                number_of_Hconflicts += 1
                counted_columns.add(innercounter)
            if myPosition == initial_position[innercounter] and innercounter != counter:
                conflictH_dict[counter+1] += 1
            innercounter+=1
        counter +=1

    #print('number_of_hconflicts =' , number_of_Hconflicts)
   # print('horizantal conflict = ', conflictH_dict)

    # now let's check for diagonal conflicts

    conflictV_dict = dict()
    counter = 1
    while counter <= N_Queens:
        conflictV_dict[counter] = 0
        counter += 1

    counter = 1
    number_of_Dconflicts = 0
    counted_columns = set()
    while counter <= len(initial_position):
        myPosition = initial_position[counter-1]
        counted_columns.add(counter -1)
        # my current column
        column = counter-1
        column_counter = 1
        # right search
        column += 1
        while column < N_Queens:
            d1 = initial_position[column]
            if (d1 == myPosition - column_counter or d1 == myPosition + column_counter) and column not in counted_columns:
                number_of_Dconflicts += 1
                conflictV_dict[counter] += 1
                counted_columns.add(column)

            column_counter += 1
            column += 1
        # left search
        column = counter - 1
        column_counter = 1
        column -= 1
        while column >= 0:
            d2 = initial_position[column]
            if (d2 == myPosition - column_counter or d2 == myPosition + column_counter) and column not in counted_columns:
                number_of_Dconflicts += 1
                conflictV_dict[counter] += 1
                counted_columns.add(column)
            column_counter += 1
            column -= 1
        counter +=1
    number_of_Dconflicts = number_of_Dconflicts
    #print('number_of_dconflicts = ', number_of_Dconflicts)
 #   print('diagonal conflict = ', conflictV_dict)
    # total conflict
    total_conflict = number_of_Dconflicts+number_of_Hconflicts
 #   print('total conflicts = ' ,total_conflict)
    hv_conflicts = dict()

    counter = 1
    while counter <= N_Queens:
        hv_conflicts[counter] = conflictV_dict[counter] + conflictH_dict[counter]
        counter += 1
  #  print('digonal + horizantal conflicts = ', hv_conflicts)
    return [total_conflict, hv_conflicts]

#######################################################################


def localbeamStart(N_Queens):
    secretsGenerator = secrets.SystemRandom()
    allboards = list()

    # Temperature = 100
    #Temperature = input('Please Enter temperature in term of integers(100 suggested per 8 queens)')
    #Temperature = int(Temperature)
    #OriginalTemp = int(Temperature)
    # cooling = 0.997
    #cooling = input('Please Enter cooling in term of percentage(0.997)')
    #cooling = float(cooling)

    # N_Queens = 8
   # N_Queens = input("Please Enter the number of queens")
    N_Queens = int(N_Queens)
    # starting time
    start = perf_counter()

    # intilize the board
    initial_position = list()
    board = dict()
    # randomly initialise the board
    # create random positions
    while len(initial_position) < N_Queens:
        x = secretsGenerator.randint(1, N_Queens)
        initial_position.append(x)
    print('initial positions', initial_position)
    # set the position in the board which is a dictionary
    # where the key is the column while the value is the location in that column
    ####################
    #initial_position = [1,2,3,4]
    counter = 0
    while counter < len(initial_position):
        board[counter+1] = initial_position[counter]
        counter += 1
    print('initial board: ', board)
    board_printer(board,N_Queens)
    locations = list()
    for key in board:
        locations.append(board[key])
    allboards.append(locations)
    #################
    #conflictsss
    x = conflicts_getter(board,N_Queens)
    mytotal_conflict = x[0]
    hv_conflicts = x[1]
    #print('my values', total_conflict , hv_conflicts)
    #################
    # now we got all the conflicts so we need to check if we are at best condition or not
    conflict = True
    stuck_counter = 0
    while conflict:

        #if Temperature == 0.001:
        #    print('sorry, possibley unsolveable ')
        locations = list()
        for key in board:
            locations.append(board[key])
        allboards.append(locations)

        if mytotal_conflict == 0:
            conflict = False
            print('solution')
            board_printer(board,N_Queens)
            #print(' Original Temperature: ', OriginalTemp,'Last Temperature: ', Temperature,'Cooling rate: ',1-cooling)
            print((perf_counter() - start), "Seconds")
            condition = True
            break
        else:
            conflict = True

        choice = 0
        while True:
            choice = secretsGenerator.randint(1,N_Queens)
            if hv_conflicts[choice] != 0:
                break
        # create n-1 boards that are different of my current board
        # change the location of the choosen queen column above but don't count the current position
        boards = list()
        counter = 1
        while len(boards) < N_Queens - 1 :
            new_board = dict()
            new_board = dict(board)
            new_board[choice] = counter
            if new_board != board:
                boards.append(new_board)
            counter += 1

        # my new possible boards positions
        '''
        print('The new possible positions')
        for i in boards:
            print(list(i.values()))
        '''
        all_boards_conflicts = list()
        all_boards_HVconflicts = list()
        for i in boards:
            #  board_printer(i,N_Queens)
            x = conflicts_getter(i,N_Queens)
            all_boards_conflicts.append(x[0])
            all_boards_HVconflicts.append(x[1])
        print(' all boards conflicts = ', all_boards_conflicts)

        # now let's choose which board is the minimum and use it if it better
        # or take it by a percentage if it is not

        minimum_conflict = min(all_boards_conflicts)
        randomly_chosen_board_conflicts = 0

        '''
        choice_perecentage = math.exp((minimum_conflict -mytotal_conflict )/Temperature)
        print('choice percentage ', choice_perecentage)
        choice_perecentage *= 100
        choice_perecentage = int(choice_perecentage)
        # 1 = minimum_conflict, 0 = mytotal_conflict
        choosingList = [1] * choice_perecentage + [0]*(100-choice_perecentage)
        print('choice percentage ', choice_perecentage)
        print('choosing list', choosingList)
        '''

        # check if they are equal
        print(f'minimum {minimum_conflict} , total = {mytotal_conflict}')
        '''
        choosed_the_original = False
        if minimum_conflict < mytotal_conflict:
            randomly_chosen_board_conflicts = minimum_conflict
            stuck_counter = 0
        else:
            choosed_the_original = True
            stuck_counter += 1
        if stuck_counter == N_Queens**5:
            print('sorry, possibley unsolveable or stuck at some place')
            break;
        #print("Tempreture ", Temperature)
        '''
        if minimum_conflict == mytotal_conflict:
            stuck_counter += 1
        else:
            stuck_counter = 0
        if stuck_counter == N_Queens**4:
            print('sorry, possibley unsolveable ')
            condition = False
            break;
        #if not choosed_the_original:
        print('chosen board conflicts',minimum_conflict)
        # if we have multiple of the used values just choose randomly of any of them
        indices =0
        indices = [i for i, x in enumerate(all_boards_conflicts) if x == minimum_conflict]
        print('multiple boards for choosen conflict amount: ', indices)
        chosen_board_index = secretsGenerator.choice(indices)
        print(chosen_board_index)
        mytotal_conflict = minimum_conflict
        board = boards[chosen_board_index]
        hv_conflicts = dict(all_boards_HVconflicts[chosen_board_index])
        #print('new hv ', hv_conflicts)
        #print(mytotal_conflict)
        #board_printer(board,N_Queens)

        #Temperature *= cooling
    return allboards,condition




if __name__ == "__main__":
    N_Queens = input("Please Enter the number of queens")
    N_Queens = int(N_Queens)
    localbeamStart(N_Queens)