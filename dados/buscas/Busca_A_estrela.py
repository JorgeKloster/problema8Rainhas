from dados.pecas.Rainha import Rainha

class Busca_A_estrela:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro  # Reference to Tabuleiro instance
        self.solution = []  # Store the valid solution

    def is_safe(self, state, row, col):
        # Check for conflicts with already placed queens
        for c in range(col):
            if state[c] == row or abs(state[c] - row) == abs(c - col):  # Diagonal threats
                return False
        return True

    def heuristic(self, state):
        # Calculate the heuristic: count conflicts in the state
        conflicts = 0
        for col1 in range(len(state)):
            if state[col1] == -1:  # Skip uninitialized columns
                continue
            for col2 in range(col1 + 1, len(state)):
                if state[col2] == -1:  # Skip uninitialized columns
                    continue
                if state[col1] == state[col2]:  # Row conflict
                    conflicts += 1
                if abs(state[col1] - state[col2]) == abs(col1 - col2):  # Diagonal conflict
                    conflicts += 1
        return conflicts

    def a_star_solve(self, initial_state):
        # List to store states in priority order
        priority_list = []
        visited = set()

        # Add the initial state to the priority list
        initial_cost = self.heuristic(initial_state) + initial_state.count(-1)
        priority_list.append((initial_cost, 0, initial_state))  # (f(x), depth, state)

        print(f"Starting A* with initial state: {initial_state}")

        while priority_list:
            # Sort the list by cost (f(x)) to simulate priority queue behavior
            priority_list.sort(key=lambda x: x[0])  # Sort by f(x)
            f_cost, depth, current_state = priority_list.pop(0)  # Get the state with the lowest f(x)
            state_tuple = tuple(current_state)

            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            print(f"Processing state: {current_state} with f(x)={f_cost}, g(x)={depth}, h(x)={f_cost - depth}")

            # Goal test: Check if all columns are filled
            if current_state.count(-1) == 0 and self.heuristic(current_state) == 0:
                self.solution = current_state
                print(f"Solution found: {self.solution}")
                return True

            # Expand the current state by finding the next empty column
            try:
                col = current_state.index(-1)  # Find the first uninitialized column
            except ValueError:
                continue  # Skip if all columns are initialized

            for row in range(8):
                if self.is_safe(current_state, row, col):
                    new_state = current_state[:]
                    new_state[col] = row

                    # Calculate f(x) = g(x) + h(x)
                    g_cost = depth + 1
                    h_cost = self.heuristic(new_state)
                    f_cost = g_cost + h_cost

                    if tuple(new_state) not in visited:
                        priority_list.append((f_cost, g_cost, new_state))
                        print(f"Enqueued new state: {new_state} with f(x)={f_cost}")

        print("No solution found.")
        return False

    def find_solution(self, initial_state):
        print(f"Starting A* search with initial state: {initial_state}")
        if self.a_star_solve(initial_state):
            # Update Tabuleiro with the solution
            for col, row in enumerate(self.solution):
                if row != -1:  # Only update initialized columns
                    space = self.tabuleiro.get_espaco_from_pos((col, row))
                    space.occupying_piece = Rainha((col, row), self.tabuleiro)
            return True
        return False
