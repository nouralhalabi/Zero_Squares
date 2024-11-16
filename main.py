import copy
import keyboard 

from logic import State, square
from player import Player


# إعداد المصفوفات (الرقع)
array1 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(2, True), square(0, False),
    square(0, False), square(2, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False)
]
array2 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(3, True), square(1, False),
    square(0, False), square(1, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(3, False), square(0, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(4, True), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(4, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
]
array3 = [
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(0, False), square(7, True),
    square(5, True), square(6, True), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(0, False), square(1, False),
    square(1, False), square(0, False), square(0, False),
    square(0, False), square(1, False), square(1, False),
    square(1, False), square(7, False), square(0, False),
    square(5, False), square(6, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
    square(1, False), square(1, False), square(1, False),
]

def initialize_player(current_board):
    return Player(current_board)
boards = [array1, array2, array3]
current_board_index = 0

current_board =boards[current_board_index]
player_instance = initialize_player(current_board)



while player_instance and player_instance.game():
       
        
        # الانتقال للرقعة التالية إذا انتهت الحركات
        current_board_index += 1
        if current_board_index >= len(boards):  # إذا انتهت جميع الرقعات
            print("لقد انتهيت من جميع الرقعات!")
           
            break
        else:
            current_board = boards[current_board_index]
            player_instance = initialize_player(current_board)
           
 