 #هذا الملف منه يبدأ البرنامج اي يتم تمرير البوردات ليبدأ اما اللاعب باللعب أو خوارزميات البحث الذكية تبدأ بإيجاد الطريق الذي يؤدي الى الفوز او الهدف
 #يسمى main
import copy
import keyboard 

from logic import State, square
from player import Player


array1 = [
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(1, False,0), square(1, False,0),
    square(1, False,0), square(2, True,1), square(0, False,0),
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
    square(1, False,0), square(0, False,0), square(3, True,1),
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
    square(0, False,0), square(0, False,0), square(2, True,1),
    square(1, False,0), square(1, False,0), square(3, True,1),
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
           
 #####________________________________________________________________________________________
 #هذا الملف المسؤول عن تحديد من يقوم باللعب المستخدم ام الكمبيوتر بحيث اذا تم استدعاءالخوارزميات هي ستقوم بإيجاد الطريق للفوز اما المستخدم هو من يلعب باستخدام حلقة 
 # while يستمر بأخذ حركات من الكيبورد للعب  بحيث قمت بتعليق الطريقة 
 # المرادة للعب 
 #كما بإمكانه استخدام الطريقتين اي من خلال الخوارزمية سيعرف الطريق للفوز ومن ثم يطبقه لاختصار الوقت والفوز 
#  كلاس اللعب الذي يحوي طرق اللعب 
#يسمى player
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
        if a.bfs_to_goal(obj):
          print("Game finished successfully!")
        else:
          print("Game over! Could not find a solution.")

       # if a.dfs_to_goal(obj):
       #    print("Game finished successfully!")
       # else:
       #    print("Game over! Could not find a solution.")
       # if a.dfs_to_goal_recursive(obj):
        #      print("Game finished successfully!")
       # else:
       #   print("Game over! Could not find a solution.")
       #اللعب من قبل المستخدم 
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
##________________________________________________________________________________________
#هذا الملف يحوي كامل منطق اللعبة من تحركات بكافة الاتحاهات الى توابع التشييك وتابع الموف المسؤول عن رد كائن بالحركة الجديدة الى تابع يحضر كافة الحالات الممكنة للحالة الحالية 
#وتابع لطباعة الحالة وتابع لتشييك عن الفوز وتابع يحضر المسار للخوارزمية بحيث عند الوصول لحالة الفوز اي الهدف يستدعى هذا التابع لجلب مسار الذي يؤدي للفوز بحيث كل حالة لها 
# attribute يسمى الاب يدل على الحالة التي أدت الى هذه الحالة 
#بحيث الحالة البدائية يكون none
#وكلاس المربع وكلاس الحالة 
#يسمى logic
import copy


class square:  
  def __init__(self, n, is_movable,g):
        self.num = n
        self.is_movable = is_movable
        self.g=g
class State:
    def __init__(self, m, parent=None,cost=0):
        self.m = m
        self.parent = parent  
        self.movable_positions = {
            index: square.num
            for index, square in enumerate(m)
            if square.num not in (0, 1) and square.is_movable
        }
        self.cost=cost
    def move(self, direction):      
     v = 1 
     original_board = [square.num for square in self.m] 

     while v > 0 and self.movable_positions:
        v = 0  
        for pos in list(self.movable_positions.keys()):  
            moved = False  

          
            if direction == 'right':
                moved = self.move_right(pos)
            elif direction == 'left':
                moved = self.move_left(pos)
            elif direction == 'down':
                moved = self.move_down(pos)
            elif direction == 'up':
                moved = self.move_up(pos)

            if moved:
                v += 1 

            self.movable_positions = {
                index: square.num
                for index, square in enumerate(self.m)
                if square.num not in (0, 1) and square.is_movable
            }
            total_sum = sum(square.g for square in self.m if square.is_movable)

     if [square.num for square in self.m] != original_board:
        self.print_board() 
        return State(self.m,original_board,total_sum)
     else:
        print("No movement possible in direction:", direction)
        return None
  
  

    def move_right(self, pos):
        target = pos + 1
        if self.check_move_right(pos, target):
            if self.m[target].num == 0:  
                self.m[pos], self.m[target] = self.m[target], self.m[pos]
                self.m[pos].g+=1 
                return True
            elif self.m[pos].num == self.m[target].num:  
                self.m[pos].num = 0
                self.m[target].num = 0
                self.m[pos].g+=1
                return True
        return False

    def move_left(self, pos):
        target = pos - 1
        if self.check_move_left(pos, target):
            if self.m[target].num == 0:  
                self.m[pos], self.m[target] = self.m[target], self.m[pos] 
                self.m[pos].g+=1 

                return True
            elif self.m[pos].num == self.m[target].num:  
                self.m[pos].num = 0
                self.m[target].num = 0
                self.m[pos].g+=1 

                return True
        return False

    def move_down(self, pos):
        target = pos + 6  
        if self.check_move_down(pos, target):
            if self.m[target].num == 0:  
                self.m[pos], self.m[target] = self.m[target], self.m[pos]
                self.m[pos].g+=1 

                return True
            elif self.m[pos].num == self.m[target].num: 
                self.m[pos].num = 0
                self.m[target].num = 0
                self.m[pos].g+=1 

                return True
        return False

    def move_up(self, pos):
        target = pos - 6 
        if self.check_move_up(pos, target):
            if self.m[target].num == 0: 
                self.m[pos], self.m[target] = self.m[target], self.m[pos]
                self.m[pos].g+=1 

                return True
            elif self.m[pos].num == self.m[target].num: 
                self.m[pos].num = 0
                self.m[target].num = 0
                self.m[pos].g+=1 

                return True
        return False

    def check_move_right(self, pos, target):
        return target < len(self.m) and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_left(self, pos, target):
        return target >= 0 and (self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_down(self, pos, target):
     return target < len(self.m) and pos % 6 == target % 6 and (
        self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def check_move_up(self, pos, target):
     return target >= 0 and pos % 6 == target % 6 and (
        self.m[target].num == 0 or self.m[target].num == self.m[pos].num)

    def print_board(self):
     for i in range(0, len(self.m), 6):
        print(" ".join(f"{square.num}" for square in self.m[i:i + 6]))
     print()

    def check_win_condition(self):
        return all(square.num in (0, 1) for square in self.m)
    
    def next_state(self):
     temp_state = copy.deepcopy(self)
    
     possible_states = []
     for direction in ['up', 'down', 'left', 'right']:
        new_state = temp_state.move(direction)
        if new_state:
            possible_states.append(new_state)
            temp_state = copy.deepcopy(self)
     return possible_states
    def get_path(self):
        path = []
        current = self
        while current is not None:
            path.append(current)
            current = current.parent
        return path[::-1] 

#___________________________________________________________________________________
#هذا الملف خاص بالخوارزميات المستخدمة من BFS , DFS  , RECURSION DFS, UCS
#كلاس الخوارزمية الذي يتم تمرير البورد له لتطبيق عليها الخوارزمية المرادة 
#يسمى algorithm
from collections import deque
import copy

from logic import State
import heapq



class algorithm:
    def __init__(self, board):
        self.board = board
#bfsssss
    def bfs_to_goal(self, initial_state):
        queue = deque([initial_state])
        visited = set()

        while queue:
            current_state = queue.popleft()                        

            if current_state.check_win_condition():
                print("Congratulations! You've won!")
                current_state.print_board()

                path = current_state.get_path()
                print("Path to solution:")
                for step, state in enumerate(path):
                    print(f"Step {step}:")
                    state.print_board()

                return True  

            state_signature = tuple(square.num for square in current_state.m)
            if state_signature in visited:
                continue
            visited.add(state_signature)

            temporary_state=copy.deepcopy(current_state)
            new_boards = temporary_state.next_state()
            if new_boards:
             for board in new_boards:
                  new_state = State(board.m, current_state)
                  queue.append(new_state)

        print("No solution found!")
        return False 
    #dfssssss
    def dfs_to_goal(self, initial_state):
        stack = [initial_state]
        visited = set()

        while stack:
            current_state = stack.pop()

            if current_state.check_win_condition():
                print("Congratulations! You've won!")
                current_state.print_board()

                path = current_state.get_path()
                print("Path to solution:")
                for step, state in enumerate(path):
                    print(f"Step {step}:")
                    state.print_board()

                return True  


            state_signature = tuple(square.num for square in current_state.m)
            if state_signature in visited:
                continue
            visited.add(state_signature)
           
            temporary_state = copy.deepcopy(current_state)
            new_boards = temporary_state.next_state()  

            if new_boards:
                for board in new_boards:
                    new_state = State(board.m, current_state)
                    stack.append(new_state)


        print("No solution found!")
        return False
    #dfs_recursionnnnnnnnn
    def dfs_to_goal_recursive(self, current_state, visited=None):
     if visited is None:
        visited = set()

     if current_state.check_win_condition():
        print("Congratulations! You've won!")
        current_state.print_board()

        path = current_state.get_path()
        print("Path to solution:")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            state.print_board()

        return True

     state_signature = tuple(square.num for square in current_state.m)
     if state_signature in visited:
        return False
     visited.add(state_signature)

     temporary_state = copy.deepcopy(current_state)
     new_boards = temporary_state.next_state()

     if new_boards:
        for board in new_boards:
            new_state = State(board.m, current_state)
            if self.dfs_to_goal_recursive(new_state, visited):
                return True

     return False
    #uniform cost search 
    def ucs_to_goal(self):
        priority_queue = []
        visited = set()  
        heapq.heappush(priority_queue, (self.board.cost, id(self.board), self.board)) 

        while priority_queue:
           
            current_cost, _, current_state = heapq.heappop(priority_queue)

          
            if current_state.check_win_condition():
                print("Solution found with cost:", current_cost)
                solution_path = current_state.get_path() 

            if current_state.check_win_condition():
                print("Solution found with cost:", current_cost)
                solution_path = current_state.get_path() 
                print("Path to solution:")
                for step, state in enumerate(solution_path):
                    print(f"Step {step}:")
                    state.print_board()

                return True  
            state_id = tuple([square.num for square in current_state.m])
            if state_id in visited:
                continue
            visited.add(state_id)

            for next_state in current_state.next_state():
                new_cost = current_cost + next_state.cost
                next_state.parent = current_state  
                heapq.heappush(priority_queue, (new_cost, id(next_state), next_state))

        print("No solution found.")
        return None    
               
