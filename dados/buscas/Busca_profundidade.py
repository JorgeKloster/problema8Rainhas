from dados.pecas.Rainha import Rainha

class Busca_profundidade:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro  # Reference to the Tabuleiro instance
        self.solution = []  # Store the valid solution

    def is_safe(self, state, row, col):
        # Check for threats in previous columns
        for c in range(8):  # Check all columns before the current one
            if state[c] == -1:  # Ignore uninitialized columns
                continue
            if state[c] == row or abs(state[c] - row) == abs(c - col):
                print(f"Conflict detected for queen at ({col}, {row}) with ({c}, {state[c]})")
                return False
        return True

    def dfs_solve(self, state, col=0):
        # Find the next column that needs to be initialized
        if col >= 8 or state.count(-1) == 0:  # Goal test: all columns filled
            self.solution = state[:]
            return True

        if state[col] != -1:  # Skip columns that are already initialized
            return self.dfs_solve(state, col + 1)

        for row in range(8):  # Try all rows in the current column
            if self.is_safe(state, row, col):
                state[col] = row  # Place queen
                if self.dfs_solve(state, col + 1):  # Recursive call for the next column
                    return True
                state[col] = -1  # Backtrack (remove queen)

        return False  # No valid arrangement for this column

    def find_solution(self, initial_state):
        print(f"Starting DFS with initial state: {initial_state}")
        if self.dfs_solve(initial_state):
            # Update Tabuleiro with the solution
            for col, row in enumerate(self.solution):
                if row != -1:  # Only update initialized columns
                    space = self.tabuleiro.get_espaco_from_pos((col, row))
                    space.occupying_piece = Rainha((col, row), self.tabuleiro)
            print(f"Solution found: {self.solution}")
            return True
        print("No solution found.")
        return False
