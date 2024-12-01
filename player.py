import copy
import sys
import keyboard
from logic import State
from algorithm import algorithm
class Player:
    def __init__(self, board):
        self.board = board
        self.movable_positions = [index for index, square in enumerate(board) if square.num not in (0, 1) and square.is_movable]

    def game(self):
      
        initial_board = State(self.board)
        initial_board.print_board()
        obj = copy.deepcopy(initial_board)
       # all_states=obj.next_state()
        a=algorithm(obj)
       
       # a.ucs_to_goal()
       # if a.bfs_to_goal(obj):
       #   print("Game finished successfully!")
       # else:
       #   print("Game over! Could not find a solution.")

       # if a.dfs_to_goal(obj):
       #    print("Game finished successfully!")
       # else:
       #    print("Game over! Could not find a solution.")
       # if a.dfs_to_goal_recursive(obj):
        #      print("Game finished successfully!")
       # else:
       #   print("Game over! Could not find a solution.")
        
        while True:
           
            key = keyboard.read_key()

          
            if key == 'right':
                new_state = obj.move('right')
            elif key == 'left':
                new_state = obj.move('left')
            elif key == 'up':
                new_state = obj.move('up')
            elif key == 'down':
                new_state = obj.move('down')
            elif key == 'esc':
                sys.exit()  # إنهاء البرنامج عند ضغط "Esc"
            else:
                continue  # إذا تم ضغط مفتاح آخر، تجاهل
            
            if new_state:
               
             if new_state.check_win_condition():
                        print("Congratulations! You've won!")
                        new_state.print_board()  
                        print("Press ESC to exit.")
                  
                       
                        return True
                        
             else:
                  all_states=new_state.next_state()
                
            
               
