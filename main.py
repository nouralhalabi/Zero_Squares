import copy
import keyboard 

from logic import State, square
from player import Player


array1 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(2, True,0), square(0, False,0),
    square(0, False,0), square(2, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0)
]
array2 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(0, False,0), square(0, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(3, False,0)
   , square(0, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(3, True,0),
    square(1, False,0), square(1, False,0), square(0, False,0),
    square(0, False,0), square(0, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0),
]
array3 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(2, False,0), square(0, False,0),
    square(0, False,0), square(0, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0)
   , square(0, False,0), square(3, False,0),
    square(1, False,0), square(1, False,0), square(0, False,0),
    square(0, False,0), square(0, False,0), square(2, True,0),
    square(1, False,0), square(1, False,0), square(3, True,0),
    square(0, False,0), square(0, False,0), square(0, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0),
   

]
array4 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(3, True,1), square(1, False,0),
    square(0, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(3, False,0), square(0, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(0, False,0), square(4, True,1), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(4, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
]
array5 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(7, True,1),
    square(5, True,1), square(6, True,1), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(0, False,0), square(0, False,0), square(1, False,0),
    square(1, False,0), square(0, False,0), square(0, False,0),
    square(0, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(7, False,0), square(0, False,0),
    square(5, False,0), square(6, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
]

def initialize_player(current_board):
    return Player(current_board)
boards = [array1,array2,array3,array4,array5]
current_board_index = 0

current_board =boards[current_board_index]
player_instance = initialize_player(current_board)



while player_instance and player_instance.game():
       
        
       
        current_board_index += 1
        if current_board_index >= len(boards): 
            print("لقد انتهيت من جميع الرقعات!")
           
            break
        else:
            current_board = boards[current_board_index]
            player_instance = initialize_player(current_board)
           
 