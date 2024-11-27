import copy


class square:  
  def __init__(self, n, is_movable,g):
        self.num = n
        self.is_movable = is_movable
        self.g=g
class State:
    def __init__(self, m, parent=None,cost=0):
        self.m = m
        self.parent = parent  # الحالة السابقة
        self.movable_positions = {
            index: square.num
            for index, square in enumerate(m)
            if square.num not in (0, 1) and square.is_movable
        }
        self.cost=cost
    def move(self, direction):      
     v = 1  # بداية الحركات
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