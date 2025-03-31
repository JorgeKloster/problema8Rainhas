from data.pieces.Queen import Queen

class Busca_largura:
    def __init__(self, board):
        self.board = board
        self.solution = []

    def is_safe(self, state, row, col):
        for c in range(8):
            if state[c] == -1: # Pula coluna não inicalizada
                continue
            if state[c] == row or abs(state[c] - row) == abs(c - col):
                print(f"Conflito encontrado da rainha em ({col}, {row}) com a ({c}, {state[c]})")
                return False
        return True

    def bfs_solve(self, initial_state):
        queue = [initial_state]

        # Adiciondo estados já visitados para que ele não volte a procurar nos mesmos estados
        visited = set()  # Guarda todos os estados já visitados

        #Adicionado contador de iterações pois a execução travava e suspeitei que fosse um loop, assim posso colocar limite de iterações
        iteration_count = 0
        max_iterations = 1000  # Coloca um limite de iterações

        print(f"Iniciando a Busca em Largura com a fila: {queue}")

        while queue:
            iteration_count += 1
            if iteration_count > max_iterations:
                print("Atingido limite de iterações. Parada a busca para eviar loop infinito.")
                return False
            
            current_state = queue.pop(0)
            state_tuple = tuple(current_state)  # Converte o estado em uma lista ordenada

            # Pula os estados que já foram visitados
            if state_tuple in visited:
                continue
            visited.add(state_tuple)  # Marca estado como já visitado

            print(f"Processando estado: {current_state}")

            if len([pos for pos in current_state if pos != -1]) == 8:
                self.solution = current_state
                print(f"Solução encontrada: {self.solution}")
                return True

            # Exxpande o estado atual procurando a próxima coluna
            try:
                col = current_state.index(-1)  # Procura a próxima coluna não inicializada
            except ValueError:
                continue  # Pula se todas as colunas foram inicializadas

            for row in range(8):
                if col < 8 and self.is_safe(current_state, row, col):
                    new_state = current_state[:]
                    new_state[col] = row

                    # Enfileira só se o estado não foi ainda visitado
                    if tuple(new_state) not in visited:
                        queue.append(new_state)
                        print(f"Enfileira novo estado: {new_state}")

        print("Nenhuma solução encontrada.")
        return False

    def find_solution(self, initial_state):
        if self.bfs_solve(initial_state):
            for col, row in enumerate(self.solution):
                if row != -1:
                    space = self.board.get_square_from_pos((col, row))
                    space.occupying_piece = Queen((col, row), self.board)
            return True
        return False
