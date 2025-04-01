from data.pieces.Queen import Queen

class Busca_A_estrela:
    def __init__(self, board):
        self.board = board
        self.solution = []

    def is_safe(self, state, row, col):
        # Cerifica conflitos com rainhas já colocadas
        for c in range(col):
            if state[c] == row or abs(state[c] - row) == abs(c - col):  # Conflitos na linha ou diagonal
                return False
        return True
    
    def heuristic(self, state):
        # Calcula a heurística: Conta os conflitos naquele estado
        conflicts = 0
        for col1 in range(len(state)): # Verifica todas as colunas do estado atual
            if state[col1] == -1:  # Pula colunas não inicializadas
                continue
            for col2 in range(col1 + 1, len(state)): # Busca a próxima coluna para comparação
                if state[col2] == -1:  # Pula colunas não inicializadas
                    continue
                if state[col1] == state[col2]:  # Conflito na linha
                    conflicts += 1 # Adiciona 1 no valor da heuristica daquele estado
                if abs(state[col1] - state[col2]) == abs(col1 - col2):  # Conflito na diagonal
                    conflicts += 1
        return conflicts

    def a_star_solve(self, initial_state):
        # Lista para guardar estados por ordem de prioridade
        priority_list = []
        visited = set()

        self.iteration_count = 0

        # Adiciona um estado inicial para a lista de prioridade
        initial_cost = self.heuristic(initial_state) + initial_state.count(-1)
        priority_list.append((initial_cost, 0, initial_state))  # (f(x), profundidade, estado)

        print(f"Iniciando A* com o estado inicial: {initial_state}")

        while priority_list:
            self.iteration_count += 1
            # Classifique a lista por custo (f(x)) para simular o comportamento da fila prioritária
            priority_list.sort(key=lambda x: x[0])  # Classifica por f(x)
            f_cost, depth, current_state = priority_list.pop(0)  # Pega o estado com o menor f(x)
            state_tuple = tuple(current_state)

            if state_tuple in visited:
                continue
            visited.add(state_tuple)

            print(f"Processando estado: {current_state} com f(x)={f_cost}, g(x)={depth}, h(x)={f_cost - depth}")

            # Teste de Estado Final: Verifica se todas as colunas estão preenchidas
            if current_state.count(-1) == 0 and self.heuristic(current_state) == 0:
                self.solution = current_state
                print(f"Solução encontrada: {self.solution}")
                print(f"Número de iterações: {self.iteration_count}")
                return True

            # Expande o estado atual para encontrar a próxima coluna vazia
            try:
                col = current_state.index(-1)  # Procura a primeira coluna não inicializada
            except ValueError:
                continue  # Pula se todas as colunas foram inicializadas

            for row in range(8):
                if self.is_safe(current_state, row, col):
                    new_state = current_state[:]
                    new_state[col] = row

                    # Calcula f(x) = g(x) + h(x)
                    g_cost = depth + 1
                    h_cost = self.heuristic(new_state)
                    f_cost = g_cost + h_cost

                    if tuple(new_state) not in visited:
                        priority_list.append((f_cost, g_cost, new_state))
                        print(f"Enfileira novo estado: {new_state} com f(x)={f_cost}")

        print("Nenhuma solução encontrada.")
        return False

    def find_solution(self, initial_state):
        print(f"Iniciando Busca A* com estado inicial: {initial_state}")
        if self.a_star_solve(initial_state):
            # Atualiza tabuleiro com a solução
            for col, row in enumerate(self.solution):
                if row != -1:
                    space = self.board.get_square_from_pos((col, row))
                    space.occupying_piece = Queen((col, row), self.board)
            return True
        return False
