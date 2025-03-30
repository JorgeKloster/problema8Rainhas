import pygame

from dados.Espaco import Espaco
from dados.pecas.Rainha import Rainha
from dados.OptionsWindow import OptionsWindow
from dados.buscas.Busca_largura import Busca_largura
from dados.buscas.Busca_profundidade import Busca_profundidade
from dados.buscas.Busca_A_estrela import Busca_A_estrela

class Tabuleiro:
	def __init__(self, largura, altura):
		self.largura = largura
		self.altura = altura
		self.largura_espaco = largura // 8
		self.altura_espaco = altura // 8
		self.selected_piece = None
		self.turn = 'white'
		self.options_menu = OptionsWindow()
		self.busca_largura = Busca_largura(self)
		self.busca_profundidade = Busca_profundidade(self)
		self.busca_A_estrela = Busca_A_estrela(self)

		self.config = [
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
		]

		self.espacos = self.generate_espacos()

		self.setup_board()

	def generate_espacos(self):
		output = []
		for y in range(8):
			for x in range(8):
				output.append(
					Espaco(
						x,
						y,
						self.largura_espaco,
						self.altura_espaco
					)
				)

		return output


	def setup_board(self):
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					espaco = self.get_espaco_from_pos((x, y))

					if piece == 'Q':
						espaco.occupying_piece = Rainha(
							(x, y),
							self
						)


	def handle_click(self, mx, my):
		x = mx // self.largura_espaco
		y = my // self.altura_espaco
		clicked_espaco = self.get_espaco_from_pos((x, y))
		if clicked_espaco.occupying_piece is None:
			clicked_espaco.occupying_piece = Rainha((x, y),self)
			user_choice = self.options_menu.open_options_window()
			print(f"User selected: {user_choice}")
			if user_choice == "Busca Largura":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Initial state passed to BFS: {initial_state}")

				if self.busca_largura.find_solution(initial_state):
					print("Solution found using BFS!")
				else:
					print("No solution found starting from the selected position.")
			elif user_choice == "Busca Profundidade":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Initial state passed to DFS: {initial_state}")
				if self.busca_profundidade.find_solution(initial_state):
					print("Solution found using DFS!")
				else:
					print("No solution found starting from the selected position.")
			elif user_choice == "Busca A*":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Initial state passed to A*: {initial_state}")
				if self.busca_A_estrela.find_solution(initial_state):
					print("Solution found using A*!")
				else:
					print("No solution found starting from the selected position.")



	def get_espaco_from_pos(self, pos):
		for espaco in self.espacos:
			if (espaco.x, espaco.y) == (pos[0], pos[1]):
				return espaco


	def draw(self, display):
		if self.selected_piece is not None:
			self.get_espaco_from_pos(self.selected_piece.pos).highlight = True
			for espaco in self.selected_piece.get_valid_moves(self):
				espaco.highlight = True

		for espaco in self.espacos:
			espaco.draw(display)
