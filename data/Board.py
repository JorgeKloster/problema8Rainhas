import pygame

from data.Square import Square
from data.pieces.Queen import Queen
from data.OptionsWindow import OptionsWindow
from data.buscas.Busca_largura import Busca_largura
from data.buscas.Busca_profundidade import Busca_profundidade
from data.buscas.Busca_A_estrela import Busca_A_estrela

class Board:
	def __init__(self, wight, height):
		self.wight = wight
		self.height = height
		self.square_wight = wight // 8
		self.square_height = height // 8
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

		self.squares = self.generate_squares()

		self.setup_board()

	def generate_squares(self):
		output = []
		for y in range(8):
			for x in range(8):
				output.append(
					Square(
						x,
						y,
						self.square_wight,
						self.square_height
					)
				)

		return output


	def setup_board(self):
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					square = self.get_square_from_pos((x, y))

					if piece == 'Q':
						square.occupying_piece = Queen(
							(x, y),
							self
						)


	def handle_click(self, mx, my):
		x = mx // self.square_wight
		y = my // self.square_height
		clicked_square = self.get_square_from_pos((x, y))
		if clicked_square.occupying_piece is None:
			clicked_square.occupying_piece = Queen((x, y),self)
			user_choice = self.options_menu.open_options_window()
			print(f"O usuário selecionou: {user_choice}")
			if user_choice == "Busca Largura":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Estado inicial da Busca em Largura: {initial_state}")

				if self.busca_largura.find_solution(initial_state):
					print("Solução com Busca em Largura encontrada!")
				else:
					print("Não foi encontrada solução partindo desse ponto.")
			elif user_choice == "Busca Profundidade":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Estado inicial da Busca em Profundidade: {initial_state}")
				if self.busca_profundidade.find_solution(initial_state):
					print("Solução com Busca em Profundidade encontrada!")
				else:
					print("Não foi encontrada solução partindo desse ponto.")
			elif user_choice == "Busca A*":
				initial_state = [-1] * 8
				initial_state[x] = y
				print(f"Estado inicial da Busca A*: {initial_state}")
				if self.busca_A_estrela.find_solution(initial_state):
					print("Solução com Busca A* encontrada!")
				else:
					print("Não foi encontrada solução partindo desse ponto.")



	def get_square_from_pos(self, pos):
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def draw(self, display):
		if self.selected_piece is not None:
			self.get_square_from_pos(self.selected_piece.pos).highlight = True
			for square in self.selected_piece.get_valid_moves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(display)
