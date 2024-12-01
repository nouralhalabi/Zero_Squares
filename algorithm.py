
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
    #A*******
    def a_star_to_goal(self, initial_state):

     open_list = []
     closed_set = set()

     heapq.heappush(open_list, (self.heuristic(initial_state), 0, initial_state))

     while open_list:
        _, g_cost, current_state = heapq.heappop(open_list)

         if current_state.check_win_condition():
            print("Solution found using A*!")
            path = current_state.get_path()
            print("Path to solution:")
            for step, state in enumerate(path):
                print(f"Step {step}:")
                state.print_board()
                return True

        state_signature = tuple(square.num for square in current_state.m)
        if state_signature in closed_set:
            continue  

     
        closed_set.add(state_signature)

      
        for next_board in current_state.next_state():
            next_state = State(next_board.m, current_state)
            new_g = g_cost + 1 
            f_cost = new_g + self.heuristic(next_state)
            heapq.heappush(open_list, (f_cost, new_g, next_state))

     print("No solution found using A*.")
     return False
##heuristic quize
    def heuristic(self, state):
     def manhattan_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)

     total_distance = 0
     for square, target in zip(state.m, self.board.m): 
        if square.num not in (0, 1):  
            square_position = square.position  
            target_position = target.position  
            total_distance += manhattan_distance(square_position, target_position)

        return total_distance
