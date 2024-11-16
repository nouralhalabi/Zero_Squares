
from collections import deque
import copy

from logic import State



class algorithm:
    def __init__(self, board):
        self.board = board

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