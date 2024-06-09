def check_result(position_tuple,next_x_coordinate):  # define a function to check whether the result satisfies the three conditions
    next_y_coordinate = len(position_tuple)  # number of next queen y coordinate is the number of elements in used position tuple
    if next_x_coordinate in position_tuple:  # if next queen is in the same column of the last queen
        return False  # not satisfy the condition, return false
    for i in range(next_y_coordinate):
        if position_tuple[i]-(i+1) == next_x_coordinate-(next_y_coordinate+1):  # check whether queens are in the same left diagonal line
            return False
        if position_tuple[i]+(i+1) == next_x_coordinate+(next_y_coordinate+1):  # check wether queens are in the same right diagonal line
            return False
    return True

def arrange_queens(line_number=8,position_tuple=()):  # define a function to arrange the queens on the chessboard
    for queen_position in range(line_number):  # check whether every queen position in the line satisfy the condition
        if check_result(position_tuple,queen_position):
            if len(position_tuple) == line_number - 1:  # get to the last line  
                yield (queen_position,)  # return all results which satisfy the conditions
            else:
                for t in arrange_queens(line_number,position_tuple + (queen_position,)):
                    yield (queen_position,) + t  # otherwise, rearrange the queens until right 

def print_queen(queen_arrangement):  # define a function to print the queens
    def line(queen_position,length=len(queen_arrangement)):
        queen_list=8*[" "]  # initialize every line as a 8 space list
        queen_list[queen_position]="Q"  # replace the queen position space with "Q"
        queen_row="|".join(queen_list)  # plug in "|" between every two spaces
        return "|"+queen_row+"|"  # add "|" at the two ends
    for queen_position in queen_arrangement:
        print(line(queen_position))  # print all 8 lines

import random
print_queen(random.choice(list(arrange_queens(8))))  # display one of the outcomes randomly