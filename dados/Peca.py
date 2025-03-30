import pygame

class Peca:
	def __init__(self, pos, tabuleiro):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.has_moved = False

	def move(self, tabuleiro, espaco, force=False):

		for i in tabuleiro.espacos:
			i.highlight = False

		if espaco in self.get_valid_moves(tabuleiro) or force:
			prev_espaco = tabuleiro.get_espaco_from_pos(self.pos)
			self.pos, self.x, self.y = espaco.pos, espaco.x, espaco.y

			prev_espaco.occupying_piece = None
			espaco.occupying_piece = self
			tabuleiro.selected_piece = None
			self.has_moved = True

			return True
		else:
			tabuleiro.selected_piece = None
			return False


	def get_moves(self, tabuleiro):
		output = []
		for direction in self.get_possible_moves(tabuleiro):
			for espaco in direction:
				if espaco.occupying_piece is not None:
					if espaco.occupying_piece.color == self.color:
						break
					else:
						output.append(espaco)
						break
				else:
					output.append(espaco)

		return output


	def get_valid_moves(self, tabuleiro):
		output = []
		for espaco in self.get_moves(tabuleiro):
			if not tabuleiro.is_in_check(self.color, tabuleiro_change=[self.pos, espaco.pos]):
				output.append(espaco)

		return output


	# True for all pieces except pawn
	def attacking_espacos(self, tabuleiro):
		return self.get_moves(tabuleiro)