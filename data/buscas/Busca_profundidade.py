from data.pieces.Queen import Queen

class Busca_profundidade:
    def __init__(self, board):
        self.board = board
        self.solution = []  # Guardará a solução

    def is_safe(self, state, row, col):
        # Verifica se tem conflitos em outras colunas
        for c in range(8):  # Verifica todas as colunas antes da que o usuário selecionou
            if state[c] == -1:  # Ignora colunas não utilizadas
                continue
            if state[c] == row or abs(state[c] - row) == abs(c - col): # Conflitos na linha ou diagonal
                print(f"Conflito encontrado da rainha em ({col}, {row}) com a ({c}, {state[c]})")
                return False
        return True

    def dfs_solve(self, state, col=0):

        # Procura a próxima coluna que precisa ser inicializada
        if col >= 8 or state.count(-1) == 0:  # Teste de Estado Final: Todas as colunas com uma Rainha
            self.solution = state[:]
            return True

        if state[col] != -1:  # Pula as colunas que já foram inicializadas
            return self.dfs_solve(state, col + 1)

        for row in range(8):  # Tenta todas as linhas da coluna até encontrar a que pode ser utilizada
            
            if self.is_safe(state, row, col):
                state[col] = row  # Insere a Rainha
                print(f"Inserida rainha em ({col},{row})")
                if self.dfs_solve(state, col + 1):  # Pula para a próxima coluna
                    return True
                state[col] = -1  # Remove rainha

        return False  # Não encontrou uma forma de posicionar as 8 rainhas

    def find_solution(self, initial_state):
        print(f"Iniciando a Busca em Profundidade com o estado inicial: {initial_state}")
        if self.dfs_solve(initial_state):
            # Atualiza o tabuleiro com a solução
            for col, row in enumerate(self.solution):
                if row != -1:
                    space = self.board.get_square_from_pos((col, row))
                    space.occupying_piece = Queen((col, row), self.board)
            print(f"Solução encontrada: {self.solution}")
            return True
        print("Nenhuma solução encontrada.")
        return False
    