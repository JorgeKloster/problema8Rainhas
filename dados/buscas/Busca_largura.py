from dados.pecas.Rainha import Rainha

class Busca_largura:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.solution = []

    def is_safe(self, state, row, col):
        for c in range(8):
            if state[c] == -1: # Skip uninitialized columns
                continue
            if state[c] == row or abs(state[c] - row) == abs(c - col):
                print(f"Conflict detected for queen at ({col}, {row}) with ({c}, {state[c]})")
                return False
        return True

    def bfs_solve(self, initial_state):
        queue = [initial_state]
        visited = set()  # Track processed states
        iteration_count = 0  # Initialize the iteration counter
        max_iterations = 1000  # Set a reasonable limit for debugging

        print(f"Starting BFS with queue: {queue}")

        while queue:
            iteration_count += 1  # Increment the counter
            if iteration_count > max_iterations:
                print("Iteration limit exceeded. Terminating search to prevent infinite loop.")
                return False
            
            current_state = queue.pop(0)
            state_tuple = tuple(current_state)  # Convert state to a tuple for set operations

            # Skip the state if it's already been visited
            if state_tuple in visited:
                continue
            visited.add(state_tuple)  # Mark state as visited

            print(f"Processing state: {current_state}")

            if len([pos for pos in current_state if pos != -1]) == 8:
                self.solution = current_state
                print(f"Solution found: {self.solution}")
                return True

            # Expand the current state by finding the next empty column
            try:
                col = current_state.index(-1)  # Find the first uninitialized column
            except ValueError:
                continue  # Skip if all columns are initialized

            for row in range(8):
                if col < 8 and self.is_safe(current_state, row, col):
                    new_state = current_state[:]
                    new_state[col] = row

                    # Enqueue only if the state hasn't been visited
                    if tuple(new_state) not in visited:
                        queue.append(new_state)
                        print(f"Enqueued new state: {new_state}")

        print("No solution found.")
        return False

    def find_solution(self, initial_state):
        if self.bfs_solve(initial_state):
            for col, row in enumerate(self.solution):
                if row != -1:
                    space = self.tabuleiro.get_espaco_from_pos((col, row))
                    space.occupying_piece = Rainha((col, row), self.tabuleiro)
            return True
        return False
