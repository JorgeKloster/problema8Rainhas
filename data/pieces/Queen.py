import pygame

from data.Piece import Piece

class Queen(Piece):
	def __init__(self, pos, board):
		super().__init__(pos, board)

		img_path = 'data/imgs/queen.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_wight - 20, board.square_height - 20))

		self.notation = 'Q'
