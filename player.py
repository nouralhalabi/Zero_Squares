import pygame
import sys
from logic import State
import copy

class Player:
    def __init__(self, board, movable_positions):
        self.board = board
        self.movable_positions = [index for index, square in enumerate(board) if square.num not in (0, 1) and square.is_movable]

    def game(self):
        # طباعة اللوحة أولاً
        initial_board=State(self.board)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # إنشاء كائن من الكلاس State
                    obj =initial_board
                   # all_states = initial_board.next_state()
                   # for i, state in enumerate(all_states):
                     #   print(f"State {i+1} (after movement in direction {['right', 'left', 'up', 'down'][i]}):")
                      #  state.print_board()
                       # print("-" * 30) 
                    # تنفيذ الحركة بناءً على المدخل
                    if event.key == pygame.K_RIGHT:
                        new_state = obj.move('right')
                    elif event.key == pygame.K_LEFT:
                        new_state = obj.move('left')
                    elif event.key == pygame.K_UP:
                        new_state = obj.move('up')
                    elif event.key == pygame.K_DOWN:
                        new_state = obj.move('down')
                    else:
                        continue  # تجاوز أي مفتاح آخر
                       
                    # تحقق من شرط الفوز
                    if new_state.check_win_condition():
                        print("You win!")
                        new_state.print_board()
                       
                        return True
                    else:
                        print("Keep playing!")
                        new_state.print_board()
                         # تحديث اللوحة
            return False  # يتم الإرجاع False إذا لم يتحقق شرط الفوز

     
